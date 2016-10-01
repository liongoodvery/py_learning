import socket


def test1():
    hostname = socket.gethostname()
    print(hostname)


def test8():
    try:
        print(socket.gethostbyname('www.baidu.com'))
        print(socket.gethostbyname('lion2016'))
        print(socket.gethostbyname('localhost'))
        print(socket.gethostbyname('nosuchhost'))
    except socket.error as msg:
        print(msg)
        pass


def test19():
    try:
        print(socket.gethostbyname_ex('www.baidu.com'))
        print(socket.gethostbyname_ex('lion2016'))
        print(socket.gethostbyname_ex('localhost'))
        print(socket.gethostbyname_ex('nosuchhost'))
    except socket.error as msg:
        print(msg)
    pass


def test30():
    print(socket.getfqdn('lion2016'))
    pass


def test35():
    print(socket.getservbyport(21))
    pass
