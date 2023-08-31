from .history import HOME_PATH
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

    print('Checking Update...', end='\r')
    if check_update(repo, remote):
        # 询问是否更新
        u = input('There is a new version of the program. Do you want to update it? [y/N] ').strip().lower()
        if u == 'y':
            try:
                remote.pull()
                print('\033[1mUpdate Successful\033[0m')
            except Exception as e:
                print(f'\033[1;31mFailed to Update\033[0m\n\t{e}')
        else:
            print('Stop Updating')
    else:
        print('You are using the latest version!')
