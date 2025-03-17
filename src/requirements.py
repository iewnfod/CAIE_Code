import importlib
import os
import sys
import subprocess

requirements = [
    ('ply', 'ply'),
    ('chardet', 'chardet'),
    ('GitPython', 'git'),
    ('colorama', 'colorama'),
    ('requests', 'requests'),
]


aliyun = 'https://mirrors.aliyun.com/pypi/simple/'

def check_pip() -> bool:
    process = subprocess.Popen([sys.executable, "-m", "pip"], stdout=subprocess.DEVNULL)
    process.wait()
    return process.returncode == 0

def ensure_pip():
    if check_pip():
        return
    else:
        print("Missing pip. Installing Now...")
        pip_cmd = f'"{sys.executable}" -m ensurepip'
        os.popen(pip_cmd).read()

def test_requirements():
    # ensure_pip()

    for package_name, import_name in requirements:
        try:
            importlib.import_module(import_name)
        except:
            print(f'Missing Important Dependence `{package_name}`\nTrying to Install for You...')
            if os.environ.get('CODESPACES'):
                os.system(f'"{sys.executable}" -m pip install {package_name}')
            else:
                os.system(f'"{sys.executable}" -m pip install {package_name} -i {aliyun}')
