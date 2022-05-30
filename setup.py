from setuptools import setup, find_packages

setup(
    name='python-package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Python REST API',
    long_description=open('README.md').read(),
    install_requires=['requests'],
    url='https://github.com/smachay/python-package',
    author='Stefan Machay',
    author_email='myemail@example.com'
)