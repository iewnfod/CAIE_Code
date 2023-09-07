from .history import HOME_PATH
from .animation import new_animation
import os
import git

VERSION = ''

with open(os.path.join(HOME_PATH, 'VERSION'), 'r') as f:
    VERSION = f.read().strip()


def check_update(repo: git.Repo, remote: git.Remote):
    remote.fetch()
    local_branch = repo.active_branch
    remote_branch = repo.remotes.origin.refs[local_branch.name]
    return local_branch.commit != remote_branch.commit


def update():
    repo = git.Repo(HOME_PATH)
    remote = repo.remote()

    if new_animation('Checking Update', 3, check_update, failed_msg='Failed to Check Update', repo=repo, remote=remote):
        # 询问是否更新
        u = input('There is a new version of the program. Do you want to update it? [Y/n] ').strip().lower()
        if u == 'n':
            return
        elif u == '' or u == 'y':
            # 读取历史记录防止被覆盖
            with open(os.path.join(HOME_PATH, '.history'), 'r') as f:
                history = f.read()
            if new_animation('Updating', 3, remote.pull, failed_msg='Failed to Update'):
                # 写入历史记录
                with open(os.path.join(HOME_PATH, '.history'), 'w') as f:
                    f.write(history)
                print('\033[1mUpdate Successful\033[0m')
        else:
            print('Stop Updating')
    else:
        print('You are using the latest version!')
