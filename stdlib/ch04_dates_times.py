import time
import datetime
import calendar
from utils import myutils
from utils.myutils import printf


def test2():
    print(time.time())
    print(time.ctime(time.time()))


def test11():
    import hashlib
    data = open(__file__, 'rt').read()
    for i in range(5):
        h = hashlib.sha1()
        print('ctime={},time={},clock={}'.format(time.ctime(), time.time(), time.clock()))
        for j in range(10000):
            h.update(data.encode('ascii'))
        print(h.digest())
    pass


def test22():
    # windows does not work
    for i in range(6, 1, -1):
        print('ctime={},time={},clock={}'.format(time.ctime(), time.time(), time.clock()))
        print('sleep time {}'.format(i))
        time.sleep(i)


def test30():
    print(time.gmtime())
    print(time.localtime())
    pass


def test38():
    t = datetime.time(1,2,3)
    print(t)
    print(datetime.time.max)
    print(datetime.time.min)


def test45():
    
    pass
