import platform
import os

def get_os_system():
    return platform.platform()

def get_py_version():
    return platform.python_version()

def requirement_install(func, func2):
    if 'Window' in get_os_system():
        os.system('Install-Package git -A')
    elif 'Linux' in get_os_system():
        os.system('sudo dnf install -y ')

def main():
    os = get_os_system()
    py_ver = get_py_version()

if __name__ == '__main__':
    main()
