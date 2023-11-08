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
    # 获取本地和远程提交的时间戳
    local_commit_time = local_branch.commit.committed_datetime
    remote_commit_time = remote_branch.commit.committed_datetime
    # 比较时间戳
    if local_commit_time < remote_commit_time:
        return True
    else:
        print("Good! Good! You are faster than your remote!")
        return False

def _update(remote, repo):
    try:
        repo.git.reset('--hard', 'origin/master')
        remote.pull()
        print('\033[1mUpdate Successful\033[0m')
    except:
        print('\033[31;1mFailed to Update\033[0m')

def get_commit_hash_msg():
    repo = git.Repo(HOME_PATH)
    latest_commit_hash = repo.head.reference.commit.hexsha[:7]
    latest_commit_message = repo.head.reference.commit.message.strip()
    return latest_commit_hash, latest_commit_message

def update():
    from .global_var import config
    git_remote = config.get_config('remote')
    repo = git.Repo(HOME_PATH)
    remote = repo.remote()
    remote.set_url(git_remote)
    # 获取当前commit记录
    latest_commit_hash, latest_commit_message = get_commit_hash_msg()

    if new_animation('Checking Update', 3, check_update, failed_msg='Failed to Check Update', repo=repo, remote=remote):
        # 获取新的commit记录
        latest_commit_hash, latest_commit_message = get_commit_hash_msg()
        # 询问是否更新
        u = input(f'There is a new version of the program\n{latest_commit_hash}: {latest_commit_message}\nDo you want to update it? [Y/n] ').strip().lower()
        if u == '' or u == 'y':
            if new_animation('Updating', 3, _update, failed_msg='Failed to Update', remote=remote, repo=repo):
                print('\033[1mUpdate Successful\033[0m')
        else:
            print('Stop Updating')
    else:
        print(f'Good! You are using the latest version!\nAt {latest_commit_hash}: {latest_commit_message}')
