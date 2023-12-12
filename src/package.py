import os
from .history import HOME_PATH
from .global_var import config
from wget import download
PKG_PATH = config.get_config('default-package-path')
REMOTE_REPO = config.get_config('remote-package-repo')
ALLOWED_PKG_SUFFIX = '.cpg'
DIS_FOLDER = ".disabled"


def get_enabled():
    enabled = []
    for d in os.listdir(PKG_PATH):
        if os.path.isfile(os.path.join(PKG_PATH, d)):
            # is a file, check suffix
            if d.endswith(ALLOWED_PKG_SUFFIX):
                # identified package
                enabled.append(".".join(d.split(".")[:-1]))
    return enabled


def get_disabled():
    disabled = []
    for d in os.listdir(os.path.join(PKG_PATH, DIS_FOLDER)):
        
        if os.path.isfile(os.path.join(PKG_PATH, DIS_FOLDER, d)):
            # is a file, check suffix
            if d.endswith(ALLOWED_PKG_SUFFIX):
                # identified package
                disabled.append(".".join(d.split(".")[:-1]))
    return disabled


def install_remote(packagename):
    # install from remote repo
    # default: REMOTE_REPO
    print(download)
    


def show_info():
    enabled = get_enabled()
    disabled = get_disabled()
    print(len(enabled), "package(s) are enabled:", end="\n\t")
    for e in enabled:
        print(e, end="\n\t")
    print(end="\r")
    print(len(disabled), "package(s) are disabled:", end="\n\t")
    for d in disabled:
        print(d, end="\n\t")
    print(end="\r")

def enable(name):
    name += ALLOWED_PKG_SUFFIX
    os.replace(
        os.path.join(PKG_PATH, DIS_FOLDER, name),
        os.path.join(PKG_PATH, name))

def disable(name):
    name += ALLOWED_PKG_SUFFIX
    os.replace(
        os.path.join(PKG_PATH, name),
        os.path.join(PKG_PATH, DIS_FOLDER, name))


def help():
    # print out information about this command
    print("""
This tool is used to manage your packages in CPC.
COMMANDS:
    install     To install a package from remote official repository
    uninstall   To remove a package from your local files
    enable      To enable a disabled package
    disable     To disable a enabled package
    list/l/ls   To list all enabled and disabled packages
    help        To show this help page

Example: `cpc -g install linear`
""")


def option_package(option_name = None, *pkgs): 
    """
    Entrance procedure of `cpc -p`
    Accepts two parameters
    @option_name: ONE from :
        - install       NYI
        - uninstall
        - enable
        - disable
        - list
        - l
        - ls
        - help
        - NULL
    @*pkgs: the name of package(s)
    """
    if option_name:
        # prevents NoneType error
        option_name = option_name.lower()
    
    print("CPC official package manager")
    # first, handle .disabled folder
    # always create one if not exist
    if not os.path.exists(os.path.join(PKG_PATH, DIS_FOLDER)):
        os.mkdir(os.path.join(PKG_PATH, DIS_FOLDER))

    if not option_name:
        # if no option name, show help an list.
        show_info()
        help()

    # casewise opt names
    if option_name in ("l", "ls", "list"):
        # to show all packages information
        show_info()
    elif option_name == "help":
        # show possible commands
        help()
    elif option_name == "uninstall":
        print("\033[2mTIP: you can use `yes|<command>` to skip [y/n] choices\033[0m")
        if not pkgs:
            # no package specified!
            print("Please input package names.")
            return
        for pkg in pkgs:
            chroma = f"\033[32m{pkg}\033[0m"
            # must check where it is, or does not exist
            if pkg in get_enabled():
                print(chroma, "is currently enabled.")
                confirm = input(f"Confirm to uninstall {chroma}? [y/n] ").lower()
                if confirm == 'y':
                    os.remove(os.path.join(PKG_PATH,pkg))
                    print(f"Uninstalled package {chroma}.")
                else:
                    # cancel
                    print("Uninstallation cancelled.")
            elif pkg in get_disabled():
                print(chroma, "is currently disabled.")
                confirm = input(f"Confirm to uninstall {chroma}? [y/n] ").lower()
                if confirm == 'y':
                    os.remove(os.path.join(PKG_PATH,DIS_FOLDER,pkg))
                    print(f"Uninstalled package {chroma}.")
                else:
                    # cancel
                    print("Uninstallation cancelled.")
            else:
                # do not exist, nothing to uninstall
                print("Package", chroma, "not found. Nothing to uninstall.")
    elif option_name == "enable":
        for pkg in pkgs:
            chroma = f"\033[32m{pkg}\033[0m"
            if pkg in get_disabled():
                # OK to enable it
                enable(pkg)
                print(f"Enabled package {chroma}.")
            else:
                print(chroma, "not found in disabled packages.")
                print("Try: `cpc -g l` to list all packages.")
    elif option_name == "disable":
        for pkg in pkgs:
            chroma = f"\033[32m{pkg}\033[0m"
            if pkg in get_enabled():
                # OK to disable it
                disable(pkg)
                print(f"Disabled package {chroma}.")
            else:
                print(chroma, "not found in enabled packages.")
                print("Try: `cpc -g l` to list all packages.")
            