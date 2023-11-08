import os
import json
from .history import HOME_PATH

class _Config:
	def __init__(self, name, default_val, update_func=None):
		self.name = name
		self.default_val = default_val
		self.val = default_val
		self.update_func = update_func

	def to_string(self):
		return str(self.val)

	def update(self, value):
		if self.update_func:
			self.update_func(self, value)
		else:
			self.val = value

	def _init_update(self, value):
		self.val = value

def remote_update(obj, value):
	if value == 'github':
		obj.val = 'https://github.com/iewnfod/CAIE_Code.git'
	elif value == 'gitee':
		obj.val = 'https://gitee.com/ricky-tap/CAIE_Code.git'
	else:
		from .quit import quit
		print(f'Config `{obj.name}` only accept `github` or `gitee`')
		quit(1)

def pip_update(obj, value):
	if value == 'pip':
		obj.val = 'https://pypi.python.org/simple/'
	elif value == 'tuna':
		obj.val = 'https://pypi.tuna.tsinghua.edu.cn/simple/'
	else:
		from .quit import quit
		print(f'Config `{obj.name}` only accept `pip` or `tuna`')
		quit(1)

class Config:
	def __init__(self, config_file_name=".cpc_config.json"):
		self.config_path = os.path.join(HOME_PATH, config_file_name)
		self.config = {
			'remote': _Config('remote', 'https://github.com/iewnfod/CAIE_Code.git', update_func=remote_update),
			'pip': _Config('pip', 'https://pypi.tuna.tsinghua.edu.cn/simple/', update_func=pip_update)
		}
		# 如果已经存在配置文件，那就加载配置文件
		if os.path.exists(self.config_path):
			with open(self.config_path, 'r') as f:
				dict = json.loads(f.read())
				for key, val in dict.items():
					if key in self.config:
						self.config[key]._init_update(val)
					else:
						self.err_config(key)

		self.write_config()

	def write_config(self):
		dict = {}
		for key, val in self.config.items():
			dict[key] = val.to_string()

		with open(self.config_path, 'w') as f:
			f.write(json.dumps(dict))

	def update_config(self, opt_name, value):
		if opt_name in self.config:
			self.config[opt_name].update(value)
			self.write_config()
			print(f'Successfully change `{opt_name}` into `{value}`')
		else:
			self.err_config(opt_name)

	def output_available_configs(self):
		print('Available configs: ')
		for i in self._default_config.keys():
			print(f'\t{i}')

	def err_config(self, opt_name):
		from .quit import quit
		print(f'Unknown config: \033[1m{opt_name}\033[0m')
		self.output_available_configs()
		quit(1)

	def get_config(self, opt_name):
		if opt_name in self.config:
			return self.config[opt_name].to_string()
		else:
			self.err_config(opt_name)
