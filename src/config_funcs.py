def q(msg):
	from .quit import quit
	print(msg)
	quit(1)

def _connect_string(l):
	return '\n'.join([f'\t\033[1m{i}\033[0m' for i in l])

class DictConfig:
	def __init__(self, d: dict) -> None:
		self.d = d

	def update(self, obj, val):
		if val in self.d:
			obj.val = self.d[val]
		else:
			q(f'Config `{obj.name}` only accept: \n{_connect_string(self.d.keys())}')

class SetConfig:
	def __init__(self, available_set: set):
		self.available_set = available_set

	def update(self, obj, val):
		if val in self.available_set:
			obj.val = val
		else:
			q(f'Config `{obj.name}` only accept: \n{_connect_string(self.available_set)}')

remote_update = DictConfig({
	'github': 'https://github.com/iewnfod/CAIE_Code.git',
	'gitee': 'https://gitee.com/ricky-tap/CAIE_Code.git',
})

dev_mod = DictConfig({'true': True, 'false': False})

branch_update = SetConfig({'stable', 'nightly', 'dev'})
