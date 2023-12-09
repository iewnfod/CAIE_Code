

def get_enabled():
    ...

def get_disabled():
    ...

def install_remote(packagename):
    ...




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
    print("CPC official package manager ")