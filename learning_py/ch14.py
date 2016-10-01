import os
import sys


def test1():
    print(__file__)
    pass


def test4():
    p = os.popen('dir')
    for line in p:
        print(line, end='')
    pass


def test15():
    r = range(4)
    pass


def test20():
    [print(line.strip()) for line in open('z:/hosts3') if line[:3] == '127']
    pass


def test25():
    a = zip('abc', 'xyz')
    print(a)
    it = iter(a)
    assert a is it
    pass


def test33():
    r = range(10)
    it = iter(r)
    assert r == it
    pass


def test40():
    os.system("ps > /sdcard/inti_proc ")
    pass


def test45():


    pass
