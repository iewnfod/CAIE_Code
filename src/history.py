import os

# 尝试导入 readline，无法导入也不会导致核心功能受损
try:
    import readline
except:
    readline = None

def parent_path(p):
    return os.path.dirname(p)

HOME_PATH = parent_path(parent_path(__file__))

class Cmd:
    def __init__(self, home_path=HOME_PATH, save_path='.history', history_size=1000):
        self.home_path = home_path
        self.save_path = save_path
        self.history_size = history_size
        self.path = os.path.join(self.home_path, self.save_path)

    def preloop(self):
        if readline and os.path.exists(self.path):
            readline.read_history_file(self.path)

    def postloop(self):
        if readline:
            readline.set_history_length(self.history_size)
            readline.write_history_file(self.path)
