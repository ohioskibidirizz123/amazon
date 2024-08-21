import subprocess
import sys
import importlib.util

def install_package(package_name):
    """Installs a package using pip."""
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])

def is_package_installed(package_name):
    """Checks if a package is installed."""
    return importlib.util.find_spec(package_name) is not None

def main():
    packages = ['colarama', 'times', 'random-number']  # Add your packages here
    
    for package in packages:
        if not is_package_installed(package):
            print(f'{package} not found. Installing...')
            install_package(package)
        else:
            print(f'{package} is already installed.')

if __name__ == '__main__':
    main()
