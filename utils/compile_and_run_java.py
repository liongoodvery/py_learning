import sys
import subprocess
import os

assert len(sys.argv) == 2
javafile = sys.argv[1]
dirname = os.path.dirname(javafile)
basename = os.path.basename(javafile)
classname = os.path.splitext(basename)[0]
subprocess.Popen('javac {}'.format(javafile))
p = subprocess.Popen('java -classpath {} {}'.format(dirname, classname), shell=True)
p.communicate()
