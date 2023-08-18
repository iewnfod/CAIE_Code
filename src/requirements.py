requirements = [
    "ply",
    "chardet",
]

def config():
    import importlib
    import pip
    for require in requirements:
        try:
            importlib.import_module(require)
        except:
            print(f'\033[1mMissing Important Dependence `{require}`\nTrying to Install for You...\033[0m')
            pip.main(['install', require])
