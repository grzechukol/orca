from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()


def get_requirements():
    with open('requirements.txt') as requirements:
        return requirements.read().splitlines()


setup(
    name='orca',
    version='0.1.0',
    description='',
    long_description=readme(),
    url='https://github.com/openrca/orca',
    author='',
    license='MIT',
    install_requires=get_requirements(),
    packages=find_packages(),
    zip_safe=False)