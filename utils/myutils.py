def print_all_attrs(m, outFile=None):
    attrs = dir(m)
    for attr in attrs:
        print('{} -----> {}'.format(attr, getattr(m, attr)), file=outFile)


def assert_true(real, expect):
    if expect != real:
        import sys
        write_error(real, expect)
        assert real == expect


def assert_false(real, expect):
    if expect == real:
        import sys
        write_error(real, expect)
        assert real == expect


def write_error(real, expect):
    import sys
    sys.stderr.write("\n\n--->real={}\n--->expect={}\n\n".format(real, expect))


def printf(format, *args):
    print(format.format(*args))
