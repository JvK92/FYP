import sys
import os
import getpass
import subprocess
import pexpect
import fileinput

user = "jai"

f = open('sudoers', 'r')
filedata = f.read()
f.close()
sudoChange = filedata.replace("<insert name here>", user)
f = open('sudoers','w')
f.write(sudoChange)
f.close()
