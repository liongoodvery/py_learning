import zlib


def test1():
    original_data = b'This is the original text.'
    print(original_data)
    print('original: len={}'.format(len(original_data)))
    compressed = zlib.compress(original_data)
    decompress = zlib.decompress(compressed)
    print(decompress)


def test12():
    original_data = b'This is the original text.'
    fm = r'{:15}{:15}'
    print(fm.format('len(data)', 'len(compressed)'))
    for i in range(5):
        compressed = zlib.compress(original_data * i)
        h = '*' if len(compressed) > len(original_data) * i else ''
        print(fm.format(len(original_data) * i, len(compressed)), h)


