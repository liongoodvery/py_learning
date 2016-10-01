import os
import subprocess


def test1():
    subprocess.call(['ls', '-l'])
    pass


def test9():
    subprocess.call('echo $VHOME', shell=True)
    subprocess.call('echo $VHOME', shell=False)
    subprocess.call('echo %VHOME%', shell=True)
    subprocess.call('echo %VHOME%', shell=False)
    pass


def test17():
    try:
        subprocess.check_call('False')
    except Exception as err:
        print(err)
    pass


def test25():
    output = subprocess.check_output('ls -l')
    print(type(output), output, sep='\n')
    pass


def test31():
    try:
        output = subprocess.check_output(
            'echo to stdout; echo to stderr 1>&2; exit 1',
            shell=True,
        )
    except Exception as e:
        print(e)
    else:
        print(len(output))
    pass


def test44():
    try:
        output = subprocess.check_output(
            'echo to stdout; echo to stderr 1>&2; exit 1',
            shell=True,
            stderr=subprocess.STDOUT
        )
    except Exception as e:
        print(e)
    else:
        print(len(output))
        print(output)
    pass


def test59():
    proc = subprocess.Popen(['ls'], stdout=subprocess.PIPE)
    print(proc.communicate()[0])


def test64():
    proc = subprocess.Popen(['cat', '-'], stdin=subprocess.PIPE)
    proc.communicate(b'\thello\n')
    pass


def test70():
    proc = subprocess.Popen(['cat', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    print(proc.communicate(b'\nhello word'))


def test75():
    ls = subprocess.Popen('ls -l', stdout=subprocess.PIPE)
    grep = subprocess.Popen('grep -E .*py', stdin=ls.stdout, stdout=subprocess.PIPE)
    end_out = grep.stdout
    print(end_out)
    for line in end_out:
        print('\t', str(line.strip()))
    pass


def test85():
    proc = subprocess.Popen('python e:\\bin\\iproc\\repeater.py',
                            shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)
    print(b'a\n')
    for i in range(5):
        proc.stdin.write(b'a\n')

        output = (proc.stdout.readline())
        print(output.rstrip())
    print(proc.communicate()[0])

    print('-' * 15)
    for i in range(5):
        proc.stdin.write('%d' % i)
    print(proc.communicate()[0])

    pass


def test106():
    print()
    'One line at a time:'
    proc = subprocess.Popen('python repeater.py',
                            shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            )
    for i in range(5):
        proc.stdin.write('{}\n'.format(i).encode('ascii'))
        output = proc.stdout.readline()
        print(output.rstrip())
    remainder = proc.communicate()[0]
    print(remainder)

    print()
    print('All output at once:')
    proc = subprocess.Popen('python repeater.py',
                            shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            )
    for i in range(5):
        proc.stdin.write('%d\n' % i)

    output = proc.communicate()[0]
    print(output)


if __name__ == '__main__':
    test106()
