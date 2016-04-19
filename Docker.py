import sys
import os
import getpass
import subprocess
import pexpect
import fileinput
import time

suPass = sys.argv[1]
userName = sys.argv[2]
location = sys.argv[3]
# spawn a root shell with sudo or su depending on your linux
proc = pexpect.spawn("su")
proc.logfile = sys.stdout
# wait until the program finds the string password or Password
proc.expect("[Pp]assword")
# Send the password to waiting shell
proc.sendline(suPass)
# wait until command completed (# is a part of next prompt)
proc.expect("#")
# ensure that the working directory is the main folder location
proc.sendline('cd ' + location)
proc.expect("#")
#apt update
proc.sendline('apt-get update')
time.sleep(3)
proc.expect("#")
#ensure CA certificates are installed
proc.sendline('apt-get install apt-transport-https ca-certificates')
proc.expect("#")
time.sleep(5)
proc.sendline('apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D')
proc.expect("#")
time.sleep(5)
#add docker repo location to docker.list
f = open('docker.list', 'w')
f.write('deb https://apt.dockerproject.org/repo debian-jessie main')
f.close
proc.sendline('mv docker.list /etc/apt/sources.list.d/')
proc.expect('#')
time.sleep(5)
#move docker.list to required directory
#update apt again
proc.sendline('apt-get update')
proc.expect('#')
#verify that the docker repository is included
proc.sendline('apt-cache policy docker-engine')
proc.expect('#')

time.sleep(10)
