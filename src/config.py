import os
import json
from .history import HOME_PATH
from .config_funcs import *

class _Config:
	def __init__(self, name, default_val, update_func=None):
		self.name = name
		self.default_val = default_val
		self.val = default_val
		self.update_func = update_func

	def to_string(self):
		return self.val

	def update(self, value):
		if self.update_func:
			self.update_func(self, value)
		else:
			self.val = value

	def _init_update(self, value):
		self.val = value

class Config:
	def __init__(self, config_file_name=".cpc_config.json"):
		self.config_path = os.path.join(HOME_PATH, config_file_name)
		self.config = {
			'remote': _Config('remote', 'https://github.com/iewnfod/CAIE_Code.git', update_func=remote_update),
			'dev': _Config('dev', False, update_func=dev_mod),
			'branch': _Config('branch','stable', update_func=branch_update),
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
		for i in self.config.keys():
			print(f'\t{i}')

	def err_config(self, opt_name):
		from .quit import quit
		print(f'Unknown config: {opt_name}')
		self.output_available_configs()
		quit(1)

	def get_config(self, opt_name):
		if opt_name in self.config:
			return self.config[opt_name].to_string()
		else:
			self.err_config(opt_name)
