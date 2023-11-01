import os
import uuid
import socketserver
import threading
import time
import asyncio


# 初始化目录
if not os.path.exists('temp'):
	os.makedirs('temp')


# log
class logger():
	def __init__(self, log_path, log_name):
		self.name = log_name
		self.log_path = os.path.join(log_path, f'{log_name}.log')
		self.type = {0: 'INFO', 1: 'WARNING', 2: 'ERROR', 3: 'FATAL'}
		self.color_type = {0: '', 1: '\033[0;30;43m', 2: '\033[0;37;41m', 3: '\033[0;37;41m'}
		self.color_end = '\033[0m'
		self.time_color = '\x1B[3m'
		self.time_color_end = '\x1B[0m'
		self.max_type_length = 16

		if os.path.exists(self.log_path):
			pass
		else:
			open(self.log_path, 'w').close()

	def get_time(self, _format='%Y-%m-%d %H:%M:%S'):
		return time.strftime(_format, time.localtime())

	def add_log(self, info:str, level:int = 0): # level: 0 普通；1 警告；2 错误；3 致命错误
		if level in self.type.keys():
			current_time = self.get_time()
			log_content = current_time + '    ' + '[' + self.type[level] + '] ' + ' ' * (self.max_type_length - len(self.type[level])) + info + '\n'
			with open(self.log_path, 'a') as f:
				f.writelines(log_content)
			self.output_log(current_time, info, level)
		else:
			self.add_log('Log Error : Not Correct Log Level.', 2)
			self.add_log(f'Log with default level: 0. Content: {info}')

	def add_log_level(self, new_level_index:int, new_level_name:str, color_type:str='\033[0;37;41m'):
		if new_level_index not in self.type.keys()and new_level_name not in self.type.values():
			if len(new_level_name) >= self.max_type_length - 4:
				self.add_log('Log Error : The new Log Name is Too Long. ', 1)

			self.type[new_level_index] = new_level_name
			self.color_type[new_level_index] = color_type
			self.add_log(f'Add New Log Level: "{new_level_name}" with Index: "{new_level_index}"')

		else:
			self.add_log('Log Warning : The new Log Level has already exists!', 2)

	def output_log(self, current_time:str, info:str, level:int):
		# 输出日期
		print(self.time_color + current_time + self.time_color_end, end='')
		print('    ', end='')
		# 输出等级
		print(self.color_type[level] + self.type[level] + self.color_end, end='')
		print(' '*(self.max_type_length-len(self.type[level])) + ' ', end='')
		# 输出内容
		print(info)


# 网络输入模拟
class NetIn:
	def __init__(self):
		self.data = []
		self.index = 0

	def add_input(self, t):
		self.data.append(t)

	def readline(self):
		while self.index >= len(self.data):
			pass

		return self.data[self.index]


# 代码运行
class CodeRunner:
	def __init__(self, uid):
		self.uid = uid
		self.parent_dir = os.path.join('temp', uid)
		if os.path.exists(self.parent_dir):
			os.removedirs(self.parent_dir)

		os.makedirs(self.parent_dir)

		self.file_name = os.path.join(self.parent_dir, 'main.cpc')
		self.output_text = ''
		self.output_stream = open(os.path.join(self.parent_dir, 'output'), 'w+')

	def set_code(self, code):
		with open(self.file_name, 'w') as f:
			f.write(code)

	def run(self, inp):
		try:
			import main
			main.main(
				('cpc', self.file_name),
				input_=inp,
				output_=self.output_stream,
			)
		except Exception as e:
			log.add_log(f'{self.uid} [error] {e}, 2')

	def has_output(self):
		self.output_stream.seek(0)
		return self.output_text != self.output_stream.read()

	def get_output(self):
		old_output = self.output_text
		self.output_stream.seek(0)
		self.output_text = self.output_stream.read()
		return self.output_text[len(old_output):-1]

	def close(self):
		self.output_stream.close()


# 规定：
# 全程使用 utf-8 编码
# 在每次运行时创建 tcp 连接
# 第一条信息为需要运行的代码
# 后续每一条为输入，均为 input 内容
# 当出现需要输出的内容时，服务器也会向客户端发送输出的内容
# 若需要运行新的代码，请建立新的 tcp 连接
class Handler(socketserver.StreamRequestHandler):
	def handle(self):
		self.uid = str(uuid.uuid4())
		self.server.connections[self.uid] = self.request
		log.add_log(f'New Connection: {self.uid}')

		self.runner = CodeRunner(self.uid)
		self.input_ = NetIn()
		self.index = 0

		while 1:
			self.handle_output()

			try:
				data = self.request.recv(1024)
				if data:
					self.handle_data(data.decode('utf-8'))
				else:
					self.close_connection()
					break

			except Exception as e:
				self.close_connection(e)
				break

	def close_connection(self, e=''):
		self.runner.close()
		self.server.connections[self.uid].close()
		del self.server.connections[self.uid]
		if e:
			log.add_log(f'Close Connection: {self.uid} with error \033[1;31m{e}\033[0m')
		else:
			log.add_log(f'Close Connection: {self.uid}')

	def handle_data(self, data):
		if self.index == 0:
			log.add_log(f'{self.uid} [code] {data}')
			self.runner.set_code(data)
			threading.Thread(target=self.runner.run, args=(self.input_, )).run()
		else:
			log.add_log(f'{self.uid} [input] {data}')
			self.input_.add_input(data)

		self.index += 1

	def handle_output(self):
		if self.runner.has_output():
			output = self.runner.get_output()
			self.request.sendall(output.encode('utf-8'))
			log.add_log(f'{self.uid} [output] {output}')


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
	def __init__(self, addr, request_handler_class):
		super().__init__(addr, request_handler_class)
		self.connections = {}


class Server:
	def __init__(self, address="127.0.0.1", port=7788):
		self.addr = address
		self.port = port

	def run(self):
		server = ThreadingTCPServer((self.addr, self.port), Handler)
		log.add_log(f'Start Server at {self.addr}:{self.port}')
		server.serve_forever()


if __name__ == '__main__':
	log = logger('.', 'server')
	Server().run()
