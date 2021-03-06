import os
from os import path
from utils import myutils
from utils.myutils import assert_false as af
from utils.myutils import assert_true as at
import re
import tempfile





def test2():
    assert os.sep == '\\'
    assert os.pardir == '..'
    assert os.curdir == '.'
    assert os.extsep == '.'


def test11():
    assert path.split('/1/2/3') == ('/1/2', '3')
    assert path.split('/1/2/3/') == ('/1/2/3', '')
    assert path.split('/1/2/3.4') == ('/1/2', '3.4')
    assert path.split('.') == ('', '.')
    assert path.split('') == ('', '')


def test19():
    assert path.basename('/1/2/3') == '3'
    assert path.basename('/1/2/3/') == ''
    assert path.basename('/1/2/3.4') == '3.4'
    assert path.basename('.') == '.'
    assert path.basename('') == ''


def test29():
    assert path.dirname('/1/2/3') == '/1/2'
    assert path.dirname('/1/2/3/') == '/1/2/3'
    assert path.dirname('/1/2/3.4') == '/1/2'
    assert path.dirname('.') == ''
    assert path.dirname('') == ''


def test34():
    assert path.splitext('/1/2/3.txt') == ('/1/2/3', '.txt')
    assert path.splitext('3.txt') == ('3', '.txt')
    assert path.splitext('3.tar.gz') == ('3.tar', '.gz')
    assert path.splitext('/1/2/3/') == ('/1/2/3/', '')
    assert path.splitext('.') == ('.', '')
    assert path.splitext('..') == ('..', '')
    assert path.splitext('') == ('', '')


def test45():
    paths = [
        '/1/2/3/4',
        '/1/2/3/',
        '/1/2/3',
        '/1/2/34',
    ]
    assert path.commonprefix(paths) == '/1/2/3'


def test51():
    paths = [
        '/1/2/3/4',
        '/1/2/3/',
        '/1/2/3',
        '/1/2/34',
    ]
    at(path.commonpath(paths), r'\1\2')


def test66():
    assert path.join('1', '2', '3') == r'1\2\3'
    assert path.join(r'/1', '2', '3') == r'/1\2\3'
    assert path.join(r'/1', r'\2', '3') == r'\2\3'


def test72():
    assert path.expanduser('~more') == r'e:\home\more'
    assert path.expanduser('~bad') == r'e:\home\bad'
    assert path.expanduser('~not') == r'e:\home\not'


def test78():
    os.environ['MYVAR'] = 'VALUE'
    assert path.expandvars(r'e:\bin\$MYVAR') == r'e:\bin\VALUE'
    assert path.expandvars(r'e:\bin\%MYVAR%') == r'e:\bin\VALUE'


def test84():
    assert path.normpath(r'z:\\1\\2\\3') == r'z:\1\2\3'
    assert path.normpath(r'z:/1/2/3') == r'z:\1\2\3'
    assert path.normpath(r'z:/../2/3') == r'z:\2\3'
    assert path.normpath(r'z:/1/2/../3') == r'z:\1\3'


def test97():
    os.chdir(r'z:\tmp')
    assert path.abspath('.') == r'z:\tmp'
    assert path.abspath('..') == 'z:\\'
    assert path.abspath('good') == r'z:\tmp\good'
    assert path.abspath('.\good') == r'z:\tmp\good'
    assert path.abspath('..\good') == r'z:\good'


def test106():
    from time import ctime
    print(ctime(path.getatime(__file__)))
    print(ctime(path.getmtime(__file__)))
    print(ctime(path.getctime(__file__)))
    print(path.getsize(__file__))


def test115():
    f = __file__
    assert path.isabs(f) == True
    assert path.isdir(f) == False
    assert path.isfile(f) == True
    assert path.islink(f) == False
    assert path.ismount(f) == False
    assert path.exists(f) == True


def test124():
    import glob

    for name in glob.glob(r'*'):
        print(name, end='\n--------\n')
    for name in glob.glob(r'*.py'):
        print(name, end='\n--------\n')


def test133():
    import linecache
    print(linecache.getline(__file__, 2))
    print('BLANK : %r' % linecache.getline(__file__, 6))
    print(linecache.getlines(__file__))
    pass


def test141():
    import linecache
    file_src = linecache.__file__
    print(file_src)


def test147():
    temp = tempfile.TemporaryFile('w+t')
    temp.write('abc')
    temp.seek(0)
    print(temp.read())
    print(temp)
    temp.close()
    pass


def test159():
    with tempfile.NamedTemporaryFile('w+t') as temp:
        print(temp.name)
        print(temp)


def test166():
    dtmp = tempfile.mkdtemp()
    print(dtmp)
    assert path.exists(dtmp)
    os.removedirs(dtmp)


def test173():
    with tempfile.NamedTemporaryFile(prefix='a', suffix='.txt') as tmp:
        assert re.match(r'a.*\.txt', path.basename(tmp.name))
    pass


def test181():
    print(tempfile.gettempdir())
    print(tempfile.gettempprefix())
    print(tempfile.gettempdirb())


def test184():
    import shutil
    import glob
    print(glob.glob('ch06*'))
    shutil.copyfile(__file__, path.join(path.dirname(__file__), 'ch06.py.copy'))
    print(glob.glob('ch06*'))


def test192():
    pass
