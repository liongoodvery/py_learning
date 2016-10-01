import sys
import os
def test1():
    print(__file__)


def test4():
    def make(label):
        def echo(message):
            print("{} : {}".format(label, message))

        return echo

    m = make('hello')
    m('good')


def test15():
    def func(a):
        b = 'li'
        return b * a

    def handle():
        print('my handle')

    func.h = handle
    func.h()


def test28():
    def inc(x): return x + 10

    L = [1, 2, 3, 4]
    LM = map(inc, L, )
    print(list(LM))


def test37():
    def foo():
        a = 0
        while True:
            a += 1
            print('ddd')
            yield a

    for i in foo():
        print(i)


def test46():
    def gensquares(N):
        for i in range(N):
            yield i ** 2

    for i in gensquares(5):
        print(i)
    pass


def test57():
    print(sys.path)
    pass
