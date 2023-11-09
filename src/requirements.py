requirements = [
    ('ply', 'ply'),
    ('chardet', 'chardet'),
    ('GitPython', 'git'),
    ('colorama', 'colorama'),
]


def test_requirements():
    import importlib
    import pip
    from .global_var import config
    for package_name, import_name in requirements:
        try:
            importlib.import_module(import_name)
        except:
            print(f'Missing Important Dependence `{package_name}`\nTrying to Install for You...')
            pip.main(['install', package_name, '-i', config.get_config('pip')])
