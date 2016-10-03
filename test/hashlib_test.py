import hashlib

md5 = hashlib.md5()
md5.update("hello".encode('utf-8'))
print(md5.hexdigest())

sha512 = hashlib.sha512()
sha512.update("hello".encode('utf-8'))
print(sha512.hexdigest())
