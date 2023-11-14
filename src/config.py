import os
import json
from .history import HOME_PATH
from .config_funcs import *

class _Config:
	def __init__(self, name, default_val, update_obj=None):
		self.name = name
		self.default_val = default_val
		self.val = default_val
		self.update_obj = update_obj

	def update(self, value):
		if self.update_obj:
			self.update_obj.update(self, value)
		else:
			self.val = value

	def _init_update(self, value):
		self.val = value

class Config:
	def __init__(self, config_file_name=".cpc_config.json"):
		self.config_path = os.path.join(HOME_PATH, config_file_name)
		self.config = {
			'remote': _Config('remote', 'https://github.com/iewnfod/CAIE_Code.git', remote_update),
			'dev': _Config('dev', False, dev_mod),
			'branch': _Config('branch', 'stable', branch_update),
			'rl': _Config('recursion-limit', 1000, recursive_limit),
			'dev.simulate-update': _Config('dev.simulate-update', False, simulate_update),
			'auto-update': _Config('auto-update', True, auto_update)
		}
		# 如果已经存在配置文件，那就加载配置文件
		if os.path.exists(self.config_path):
			with open(self.config_path, 'r') as f:
				d = json.loads(f.read())
				for key, val in d.items():
					if key in self.config:
						self.config[key]._init_update(val)

		self.write_config()

	def write_config(self):
		d = {}
		for key, val in self.config.items():
			d[key] = val.val

		sd = sorted(d, key=lambda x:x[0])
		result = {}
		for key in sd:
			result[key] = d[key]

		with open(self.config_path, 'w') as f:
			f.write(json.dumps(result, indent=4))

	def update_config(self, opt_name, value):
		if opt_name in self.config:
			self.config[opt_name].update(value.lower())
			self.write_config()
			print(f'Successfully change `{opt_name}` into `{value}`')
		else:
			self.err_config(opt_name)

	def reset_config(self):
		try:
			os.remove(self.config_path)
			print('Successfully reset all configs.')
		except Exception as e:
			print(f"Error deleting config file: {e}")

	def output_available_configs(self):
		print('Available configs: ')
		for i in self.config.keys():
			print(f'\t{i}')

	def err_config(self, opt_name):
		print(f'Unknown config: {opt_name}')
		self.output_available_configs()

	def get_config(self, opt_name):
		if opt_name in self.config:
			return self.config[opt_name].val
		else:
			self.err_config(opt_name)

	def get_default_config(self, opt_name):
		if opt_name in self.config:
			return self.config[opt_name].default_val
		else:
			self.err_config(opt_name)
