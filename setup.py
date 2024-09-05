import setuptools
from distutils.core import setup

setup(
    name='task-cli',
    version='0.1',
    description='A simple task manager',
    author='diegarlin',
    author_emails='garcialinaresdiego@gmail.com',
    packages=['task_cli'],
    entry_points={
        'console_scripts': ['task-cli=task_cli.entry:cli_entry_point'],    
    },
    install_requires=[
        'requests',
    ],
)