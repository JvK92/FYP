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
location = location+"/fileout"
# spawn a root shell with sudo or su depending on your linux
proc = pexpect.spawn("su")
proc.logfile = sys.stdout
# wait until the program finds the string password or Password
proc.expect("[Pp]assword")
# Send the password to waiting shell
proc.sendline(suPass)
# wait until command completed (# is a part of next prompt)
proc.expect("#")
#install the ssh client
proc.sendline("apt-get install -y openssh-client")
proc.expect("#")
time.sleep(5)
#install the ssh server
proc.sendline("apt-get install -y openssh-server")
proc.expect("#")
time.sleep(5)
#Delete and regenerate keys
proc.sendline("rm /etc/ssh/ssh_host_*")
proc.expect("#")
proc.sendline("dpkg-reconfigure openssh-server")
proc.expect("#")
time.sleep(5)
#ensure script is closed and overwrite suPass here.
suPass = " "
proc.sendline("exit")
proc.expect("#")
proc.sendline("exit")
