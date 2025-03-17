from .history import HOME_PATH
from .animation import new_animation
import os
import git
import requests
import json
from time import time
from datetime import datetime

VERSION = ''

super_fast = False

with open(os.path.join(HOME_PATH, 'VERSION'), 'r') as f:
    VERSION = f.read().strip()

def init_git():
    from .global_var import config
    if not os.path.exists(os.path.join(HOME_PATH, '.git')):
        repo = git.Repo.init(HOME_PATH)
        branch = config.get_config('branch')
        remote = repo.create_remote('origin', config.get_config('remote'))
        remote.fetch()
        repo.git.reset("--hard", f"origin/{branch}")
        repo.git.checkout(branch)

def update_expired():
    from .global_var import config
    if time() - config.get_config('last-auto-update') > config.get_config('interval-update'):
        return True
    else:
        return False

def check_github_connectivity():
    url = "https://github.com/"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return True
    except requests.RequestException:
        return False

def check_update(repo: git.Repo, remote: git.Remote):
    remote.fetch()
    local_branch = repo.active_branch
    from .global_var import config
    config_branch = config.get_config('branch') if not config.get_config('dev') else 'dev'
    remote_branch = repo.remotes.origin.refs[config_branch]
    # 获取本地和远程提交的时间戳
    local_commit_time = local_branch.commit.committed_datetime
    remote_commit_time = remote_branch.commit.committed_datetime
    # 比较时间戳
    if local_commit_time < remote_commit_time:
        return True
    elif config.get_config('dev.simulate-update') and config.get_config('dev'):
        print("You are using simulate update, we will simulate an update.")
        return True
    elif local_commit_time > remote_commit_time:
        print(f"Good! Good! You are faster than \033[1m{get_current_branch()}\033[0m branch!")
        print("At", *get_commit_hash_msg())
        show_notification(get_current_branch())
        global super_fast
        super_fast = True
        return False
    else:
        return False

def _update(remote, repo):
    try:
        from .global_var import config
        if not config.get_config('dev.simulate-update'):
            branch = config.get_config('branch') if not config.get_config('dev') else 'dev'
            repo.git.reset('--hard', f'origin/{branch}')
            repo.git.checkout(branch)
            remote.pull()
            print('\033[1mUpdate Successful\033[0m')
            show_notification(get_current_branch())
        else:
            print('\033[1mSimulate Update Successful\033[0m')
            show_notification(get_current_branch())
    except:
        print('\033[31;1mFailed to Update\033[0m')

def get_current_branch():
    if os.environ.get('CODESPACES'):
        return 'online'
    repo = git.Repo(HOME_PATH)
    current_branch = repo.git.rev_parse("--abbrev-ref", "HEAD")
    return current_branch

def get_commit_hash_msg():
    if os.environ.get('CODESPACES'):
        return '000000', 'Online IDE', '000000', 'Online IDE'
    else:
        repo = git.Repo(HOME_PATH)
        from .global_var import config
        from re import sub
        remote_branch = config.get_config('branch') if not config.get_config('dev') else 'dev'
        latest_commit_hash = repo.rev_parse(f'origin/{remote_branch}').hexsha[:7]
        latest_commit_message = repo.rev_parse(f'origin/{remote_branch}').message.strip()
        local_commit_hash = repo.head.commit.hexsha[:7]
        local_commit_message = repo.head.reference.commit.message.strip()
        return latest_commit_hash, latest_commit_message, local_commit_hash, local_commit_message

def show_notification(_branch):
    f = os.path.join(HOME_PATH, 'notification', 'notification.json')
    with open(f, 'r') as file:
        notification_data = json.load(file)
    if _branch in notification_data['branch']:
        expiry_date_str = notification_data['expiry_date']
        current_time = datetime.now()
        expiry_date = datetime.strptime(expiry_date_str, '%Y-%m-%d')
        if current_time < expiry_date:
            if notification_data['type'] == 'deprecate':
                print(f"\033[1m❗DEPRECATED NOTIFICATION❗\33[1m")
                deprecate_keyword = ', '.join(notification_data['deprecation']['keyword'])
                deprecation_date_str = notification_data['deprecation']['deprecation_date']
                deprecation_date = datetime.strptime(deprecation_date_str, '%Y-%m-%d')
                if current_time > deprecation_date:
                    print(f"👉{deprecate_keyword}👈 has become deprecated since {notification_data['deprecation']['deprecation_date']}\033[0m")
                else:
                    print(f"👉{deprecate_keyword}👈 will be deprecated at {notification_data['deprecation']['deprecation_date']}\033[0m")
            elif notification_data['type'] == 'update':
                print(f"\033[1m🎉UPDATE NOTIFICATION🎉\33[1m")
                print(f"👉{notification_data['content']}\033[0m")
            elif notification_data['type'] == 'add':
                print(f"\033[1m🎉NEW FEATURE NOTIFICATION🎉\33[1m")
                print(f"👉{notification_data['content']}\033[0m")
        else:
            print("🙁No developer notification available.")
    else:
        print("🙁No developer notification available.")

def integrity_protection():
    if not os.environ.get('CODESPACES'):
        # init_git()

        repo = git.Repo(HOME_PATH)
        current_branch = get_current_branch()
        local_commit = repo.head.commit
        remote_branch = repo.remote().refs[current_branch]
        remote_commit = remote_branch.commit
        diff = local_commit.diff(remote_commit)

        if diff or repo.is_dirty():
            repo.git.reset('--hard', remote_commit)
            print("❗INTEGRITY WARNING❗")
            print("Changes have been discarded")
            print("---------------------------------")

def update():
    from .global_var import config
    if os.getenv('CODESPACES'):
        print('You are using a GitHub Codespace, where update function is not allowed.')
        return
    git_remote = config.get_config('remote')
    # 检查是否能连接到 GitHub
    if git_remote == config.get_default_config('remote') and not check_github_connectivity():
        print('Failed to connect to GitHub, switch to Gitee as remote.')
        config.update_config('remote', 'gitee')
        git_remote = config.get_config('remote')
    # 正式开始更新
    repo = git.Repo(HOME_PATH)
    remote = repo.remote()
    if config.get_config('dev'):
        print('In a developer mode, your remote will not be changed by config and branch will be locked in dev.')
        print('You can close the developer mode by using `cpc -c dev false`.')
    else:
        remote.set_url(git_remote)

    #获取提交信息
    latest_commit_hash, latest_commit_message, local_commit_hash, local_commit_message = get_commit_hash_msg()

    if new_animation('Checking Update', 3, check_update, failed_msg='Failed to Check Update', repo=repo, remote=remote):
        # 询问是否更新
        u = input(f'There is a new \033[1m{get_current_branch()}\033[0m version of the program\n{latest_commit_hash}: {latest_commit_message}\nDo you want to update it? [Y/n] ').strip().lower()
        if u == '' or u == 'y':
            if new_animation('Updating', 3, _update, failed_msg='Failed to Update', remote=remote, repo=repo):
                print('\033[1mUpdate Successful\033[0m')
        else:
            print('Stop Updating')
    else:
        if not super_fast:
            print(f'Good! You are using the latest \033[1m{get_current_branch()}\033[0m version!\nAt {local_commit_hash}: {local_commit_message}')
            show_notification(get_current_branch())
