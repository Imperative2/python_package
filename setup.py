from setuptools import setup, find_packages

setup(
    name='python_package',
    version='1.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Imperative2/python_package',
    author='Karol masluch',
    author_email='myemail@example.com'
)