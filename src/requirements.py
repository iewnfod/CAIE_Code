requirements = [
    ('ply', 'ply'),
    ('chardet', 'chardet'),
    ('GitPython', 'git'),
    ('colorama', 'colorama'),
    ('requests', 'requests'),
]

tuna = 'https://pypi.tuna.tsinghua.edu.cn/simple/'

def test_requirements():
    import importlib
    import pip
    for package_name, import_name in requirements:
        try:
            importlib.import_module(import_name)
        except:
            print(f'Missing Important Dependence `{package_name}`\nTrying to Install for You...')
            pip.main(['install', package_name, '-i', tuna])
