requirements = [
    ('ply', 'ply'),
    ('chardet', 'chardet'),
    ('GitPython', 'git')
]

def config():
    import importlib
    import pip
    for package_name, import_name in requirements:
        try:
            importlib.import_module(import_name)
        except:
            print(f'\033[1mMissing Important Dependence `{package_name}`\nTrying to Install for You...\033[0m')
            pip.main(['install', package_name])
