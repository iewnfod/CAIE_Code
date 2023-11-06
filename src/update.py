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

def _force_update(remote, repo):
    # 清除本地修改
    repo.index.checkout(force=True)
    # 获取新的内容
    remote.pull()

def _update(remote, repo):
    try:
        repo.git.reset('--hard', 'origin/master')
        remote.pull()
        print('\033[1mUpdate Successful\033[0m')
    except:
        print('Failed to Update')

def update():
    repo = git.Repo(HOME_PATH)
    remote = repo.remote()

    if new_animation('Checking Update', 3, check_update, failed_msg='Failed to Check Update', repo=repo, remote=remote):
        # 询问是否更新
        u = input('There is a new version of the program. Do you want to update it? [Y/n] ').strip().lower()
        if u == '' or u == 'y':
            if new_animation('Updating', 3, _update, failed_msg='Failed to Update', remote=remote, repo=repo):
                print('\033[1mUpdate Successful\033[0m')
        else:
            print('Stop Updating')
    else:
        print('You are using the latest version!')
