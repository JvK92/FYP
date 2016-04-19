import sys
import os
import getpass
import subprocess
import pexpect
import fileinput

suPass = sys.argv[1]

user = getpass.getuser()

sudoCheck = "n"

#sudoCheck = raw_input("Have you configured sudo? y/n")

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
	proc.sendline(suPass)

# wait until command completed (# is a part of next prompt)
	proc.expect("#")
#move working directory to script location
	proc.sendline("cd " + location )
	proc.expect("#")
#install sudo
	proc.sendline("apt-get install sudo")
	proc.expect("#")
#sudoers is protected against non root edits, script isn't running as root so chmod it.
	proc.sendline("chmod 0777 sudoers")
	proc.expect("#")
#add current user to sudoers
	f = open('sudoers', 'r')
	filedata = f.read()
	f.close()
	sudoChange = filedata.replace("<insert name here>", user)
	f = open('sudoers','w')
	f.write(sudoChange)
	f.close()
#change sudoers permissions back to only root r/w
	proc.sendline("chmod 0400 sudoers")
	proc.expect("#")
#move sudoers to /etc
	proc.sendline("scp sudoers /etc")


# remove root password from this script's memory
	suPass = " "

#ensure working directory has not changed

	proc.expect("#")
	proc.sendline("cd " + location)
	proc.expect("#")
	proc.sendline("exit")
	proc.expect("#")
	proc.sendline("exit")

#move to next script (via Manager)
	
	



