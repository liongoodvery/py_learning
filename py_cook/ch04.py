import Const


def test1():
    print(__file__)
    pass


def test5():
    with open(__file__, 'rt') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopIteration as e:
            print(e)


def test15():
    with open(__file__, 'rt') as f:
        while True:
            line = next(f, None)
            if line is None: break
            print(line, end='')


def test23():
    items = [1, 2, 3]
    it = iter(items)
    assert next(it) == 1
    assert next(it) == 2
    assert next(it) == 3
    assert next(it, None) is None
    pass


def test32():
    def frange(start, end, increment):
        x = start
        while x < end:
            yield x
            x += increment

    f = frange(1, 2, 0.25)
    assert next(f) == 1
    assert next(f) == 1.25
    assert next(f) == 1.5
    assert next(f) == 1.75
    assert next(f, None) is None
    assert sum(f) == 0
    pass


def test50():
    def count_down(n):
        print('starting to count down form :', n)
        while n > 0:
            yield n
            n -= 1
        print('done')

    c = count_down(3)
    print(c)
    try:
        while True:
            print(next(c))
    except StopIteration as e:
        print(e)
    c = count_down(3)
    while True:
        nu = next(c, None)
        if nu is None:
            break
        print(nu)


def test76():
    file = open(Const.RD_ONLY_FILE, 'r', encoding='utf-8')
    print(file)
    # for line in file:
    #     print(line, end='')

    for line in reversed(list(file)):
        print(line, end='')

    pass


def test87():
    import json

    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }

    json_str = json.dumps(data)
    print(type(json_str))

    data = json.loads(json_str)

    print(type(data))
    pass


def test105():
    for line in open(Const.RD_ONLY_FILE, 'r'):
        print(line.upper(), end='')
    pass


def test112():
    f = open(Const.RD_ONLY_FILE, 'r')
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    print(lines)
    pass


def test121():
    z = zip('abcd', 'xyzt')
    print(iter(z))
    print(list(z))
    pass


def test127():
    M = map(abs, (-1, 0, 1))
    print(M)
    for m in M: print(m)


def test133():
    assert bool([]) == False
    assert bool(0) == False
    assert bool(False) == False
    assert bool('') == False
    assert bool(()) == False
    assert bool({}) == False
    assert bool(None) == False
    pass


def test143():
    f = filter(bool, ['god', '', ' ', 'small lion'])
    for i in f: print(i, end="|", sep="-----")
    pass


def test151():
    di = {'a': 1, 'b': 2, 'c': 3}
    dk = di.keys()
    for k in dk : print(k)
    print(type(di.keys()))
    pass
