def test1():
    print(__file__)
    pass


def test5():
    x = 10
    assert bin(x) == '0b1010'
    assert oct(x) == '0o12'
    assert hex(x) == '0xa'

    assert format(x, 'b') == '1010'
    assert format(x, 'o') == '12'
    assert format(x, 'x') == 'a'

    int('0xa', 16) == 10
    int('a', 16) == 10
    int('12', 8) == 10


def test20():
    a = complex(3, 2)
    assert a.real == 3
    assert a.imag == 2

    b = 3 + 2j
    assert b.real == 3
    assert b.imag == 2

    assert a + b == 6 + 4j
    assert a - b == 0


def test33():
    a = float('inf')
    b = float('inf')
    c = float('-inf')
    d = float('nan')
    assert a + b == a
    assert a * 2 == a
    assert a + 10 == a
    assert 10 / a == 0.0
    assert 10 / -a == -0.0
    pass
