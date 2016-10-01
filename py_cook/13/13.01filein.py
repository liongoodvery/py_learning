import fileinput


def test():
    with fileinput.input() as f:
        for line in f:
            print(line, ' ')


def test10():
    with fileinput.input(r'z:/hosts') as f:
        for line in f:
            print(fileinput.filelineno(), line,end='')


if __name__ == '__main__':
    test10()
