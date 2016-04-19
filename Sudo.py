import sys
import os
import getpass
import subprocess
import pexpect

from Manager import suStart

from Manager import passw

print suStart
print passw

sudoCheck = raw_input("Have you configured sudo? y/n")

if sudoCheck == "n": 
#	suStart = getpass.getpass("Please Enter your root Password (It wont be stored)")

#python script location
	def getScriptPath():
		return os.path.dirname(os.path.realpath(sys.argv[0]))

	location = getScriptPath()


# spawn a root shell with sudo or su depending on your linux
	proc = pexpect.spawn("su")
	proc.logfile = sys.stdout

# wait until the program finds the string password or Password
	proc.expect("[Pp]assword")
# Send the password to waiting shell
	proc.sendline(suStart)

# wait until command completed (# is a part of next prompt)
	proc.expect("#")
# run whoami
	proc.sendline("whoami")

# wait for next prompt
	proc.expect("#")
#proc.sendline("ls -al")
#proc.expect("#")
	proc.sendline("cd " + location )
	proc.expect("#")
	proc.sendline("gedit sudoers")
	proc.expect("#")
	proc.sendline("cp sudoers /etc")


# remove root password from memore
	suStart = ""

#begin loading next module

	proc.expect("#")
	proc.sendline("cd " + location)
	proc.expect("#")
	proc.sendline("exit")
#	proc.expect("#")
#	proc.sendline("python NextModule.py")

else: 	
	subprocess.Popen(['python', 'NextModule.py']) 





