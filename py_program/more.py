def more(text, linenums=15):
    lines = text.splitlines()
    while lines:
        chunk = lines[:linenums]
        lines = lines[linenums:]
        for line in chunk:
            print(line)
        if lines and input('More? ') in ['q', 'Q']: break


if __name__ == '__main__':
    import sys

    more(open(sys.argv[1]).read(), 10)
