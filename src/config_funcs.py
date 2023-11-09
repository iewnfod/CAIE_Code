def q(msg):
	from .quit import quit
	print(msg)
	quit(1)

def remote_update(obj, value):
	if value == 'github':
		obj.val = 'https://github.com/iewnfod/CAIE_Code.git'
	elif value == 'gitee':
		obj.val = 'https://gitee.com/ricky-tap/CAIE_Code.git'
	else:
		q(f'Config `{obj.name}` only accept `github` or `gitee`')

def pip_update(obj, value):
	if value == 'pip':
		obj.val = 'https://pypi.python.org/simple/'
	elif value == 'tuna':
		obj.val = 'https://pypi.tuna.tsinghua.edu.cn/simple/'
	else:
		q(f'Config `{obj.name}` only accept `pip` or `tuna`')

def dev_mod(obj, value):
	value = value.lower()
	if value == 'true':
		obj.val = True
	elif value == 'false':
		obj.val = False
	else:
		q(f'Config `{obj.name}` only accept `true` or `false`')

def branch_update(obj, value):
	if value == 'master':
		obj.val = 'master'
	elif value == 'stable':
		obj.val = 'stable'
	elif value == 'nightly':
		obj.val = 'nightly'
	else:
		q(f'Config `{obj.name}` only accept `master`, `stable`,`nightly`')
