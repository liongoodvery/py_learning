def test1():
    raise SystemExit('Something wrong')
    pass


def test5():
    import sys
    sys.stderr.write('')
    raise SystemExit(1)
    pass


if __name__ == '__main__':
    pass

