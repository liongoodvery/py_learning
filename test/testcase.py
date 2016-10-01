import re
import time
import importlib

# write every test time
wtime = False
# test_mode=0 test all
# test_mode=1 test last
tm = 1


def methon_test(method, testfile):
    func = eval('testfile.' + method)
    if wtime:
        print('>>> starting test function {}() <<<'.format(method), flush=True)
    sta = time.clock()
    func()
    tt = time.clock() - sta
    if wtime:
        print('>>> test passed time = {:.4f}ms<<<\n'.format(10 ** 3 * tt), flush=True)


def get_module_name():
    with open('config', 'rt') as f:
        name = f.read()
    print("test_file: {}\n{}".format(name, '- ' * 15))
    return name


def main():
    sta = time.clock()
    testfile = importlib.import_module(get_module_name())
    with open(testfile.__file__) as fin:
        text = fin.read()

    pat = re.compile(r'def (test.*)\(\):.*')
    r = pat.findall(text)
    if tm == 0:
        for method in r:
            methon_test(method, testfile)
    elif tm == 1:
        methon_test(r[-1], testfile)

    print('>>>>>total time {:.3f} ms <<<<<'.format(10 ** 3 * time.clock() - sta))


if __name__ == '__main__':
    main()
