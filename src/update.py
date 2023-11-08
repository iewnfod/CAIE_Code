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

def _update(remote, repo):
    try:
        repo.git.reset('--hard', 'origin/master')
        remote.pull()
        print('\033[1mUpdate Successful\033[0m')
    except:
        print('\033[31;1mFailed to Update\033[0m')

def update():
    repo = git.Repo(HOME_PATH)
    remote = repo.remote()
    latest_commit_hash = repo.head.reference.commit.hexsha[:7]
    latest_commit_message = repo.head.reference.commit.message

    if new_animation('Checking Update', 3, check_update, failed_msg='Failed to Check Update', repo=repo, remote=remote):
        # 询问是否更新
        u = input(f'There is a new version of the program({latest_commit_hash}: {latest_commit_message}).\n Do you want to update it? [Y/n] ').strip().lower()
        if u == '' or u == 'y':
            if new_animation('Updating', 3, _update, failed_msg='Failed to Update', remote=remote, repo=repo):
                print('\033[1mUpdate Successful\033[0m')
        else:
            print('Stop Updating')
    else:
        print(f'You are using the latest version!\n At {latest_commit_hash}: {latest_commit_message}')
