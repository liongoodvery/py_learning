import re

fin = open('z:/hosts', 'r')
fout = open('z:/hosts2', 'w')

# m=pat.match('127.0.0.1	ads01.com')
# print(m.groups())
lines = fin.readlines()
l127 = []
lothers = []
print('line len={}'.format(len(lines)))
for line in lines:
    line = line.strip()
    if line.startswith('127.0.0'):
        l127.append(line)
    else:
        lothers.append(line)

print('l127 len={}'.format(len(l127)))
print('lothers len={}'.format(len(lothers)))

for line in l127:
    fout.write(line)
    fout.write('\n')
for line in lothers:
    fout.write(line)
    fout.write('\n')

fout.close()
fin.close()
