import os
import sys


def test1():
    os.environ['USER'] = 'lion'
    print(os.environ.get('USER'))
    import getpass
    user = getpass.getuser()
    passwd = getpass.getpass()
    print(user, passwd)
    pass


def test14():
    print(os.get_terminal_size())
    pass


def test19():
    print(os.getenv('PYTHONPATH'))
    pass


def test23():
    m = __import__('ch13')
    print(m)
    pass
