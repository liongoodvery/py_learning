from urllib import request

with request.urlopen("https://api.douban.com/v2/book/2129650") as f:
    read = f.read()
    print(type(f))
    print("Status:", f.status, f.reason)
    for k, v in f.getheaders():
        print("%s:%s" % (k, v))
from http.client import HTTPResponse
dir(HTTPResponse)