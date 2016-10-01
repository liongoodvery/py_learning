import sys
import os
import subprocess

# print(sys.argv)
# print(__file__)
from os import path
import winshell

print(winshell.desktop())


def create_shortcut_to_desktop(*argv):
    target = argv[0]
    title = '我的快捷方式'
    s = path.basename(target)
    fname = path.splitext(s)[0]
    winshell.CreateShortcut(
        Path=path.join(r'e:\bin\all', fname + '.lnk'),
        Target=target,
        Icon=(target, 0),
        Description=title)


create_shortcut_to_desktop(r'e:\bin\iproc')
# a = 1
# iproc = os.getenv('VIPROC', r'e:\bin\iproc\\')
# print(iproc)
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage:{} file_path'.format(__file__))
        input()
        exit()
