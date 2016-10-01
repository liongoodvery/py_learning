import os
import subprocess

procs = [line.split()[-1] for line in open('/sdcard/init_proc') if len(line) > 10][1:]
p = os.popen('ps')
procs2 = [line for line in p
          if (len(line) > 10) &
          ('/system/bin/sh' not in line)&
          ('com.hipipal.qpy3' not in line)&
          ('/data/data/com.hipipal.qpy3/files/bin/python' not in line)][1:]

pids = [line.split()[1] for line in procs2 if line.split()[-1] not in procs]
kill = subprocess.Popen('su', shell=True)
for pid in pids:
    print(kill.communicate('kill {}'.format(pid)))
print(len(pids))
