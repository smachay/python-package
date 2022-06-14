from setuptools import setup, find_packages

setup(
    name='interpolation-package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.md').read(),
    url='https://github.com/smachay/python-package',
    author='Stefan Machay',
    author_email='myemail@example.com'
)