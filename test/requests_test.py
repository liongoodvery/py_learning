import requests
from utils.myutils import print_all_attrs
import os


def test1():
    r = requests.get('https://www.zhihu.com/')
    print_all_attrs(r)


def test10():
    r = requests.post('https://httpbin.org/', data={'wd': 'python'})
    print(r.headers)
    print(r.text)
    pass


def test17():
    r = requests.get('http://httpbin.org/', params={'k1': 'v1', 'k2': 'v2', 'k3': ['v4', 'v3']})
    print(r.url)
    print(r.encoding)
    pass


def test25():
    r = requests.get('https://www.baidu.com')
    print(r.url)
    print(r.encoding)
    r.encoding = 'UTF-8'
    print(r.content)
    pass


def test34():
    r = requests.get('https://api.github.com/events')
    print(r.json())


def test38():
    r = requests.get('https://api.github.com/events', stream=True)
    print(r.raw.read(10))


def test43():
    bad_r = requests.get('https://api.github.com/status/404')
    print(bad_r.status_code)
    bad_r.raise_for_status()
    pass


def test50():
    ua = r'Mozilla/5.0 (Linux; U; Android 4.4.4; zh-CN; HM NOTE 1S Build/KTU84P) ' \
         r'AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.4.1.576 ' \
         r'U3/0.8.0 Mobile Safari/534.30'
    r = requests.get('https://api.github.com/', headers={'User-Agent': ua})
    print(r.request.headers)
