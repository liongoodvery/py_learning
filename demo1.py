import re

fin = open('c:/windows/system32/drivers/etc/hosts', 'r')
fout = open('z:/hosts', 'w')


pat = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+((?:[\w-]+\.)*\w+)')
# m=pat.match('127.0.0.1	ads01.com')
# print(m.groups())
lines=fin.readlines()
print('line len={}'.format(len(lines)))
for line in lines:
    line = line.strip()
    m=pat.match(line)
    if m:
        fout.write(m.group(1))
        fout.write(' ')
        fout.write(m.group(2))
        fout.write('\n')


def test22():
    d={}
    d.keys()
    pass
