import sys
import os
import getpass
import subprocess
import time


def sudoRun():
	subprocess.Popen(['xterm', '-e', 'python', location+'/Project.py', suPass])
	return


def sshRun():
	subprocess.Popen(['xterm', '-e', 'python', location+'/ssh.py', suPass, userName, location]) 

def dockerRun():
	subprocess.Popen(['python', location+'/Docker.py', suPass, userName, location]) 
	print "I dont know why i wont run"
def getScriptPath():
	return os.path.dirname(os.path.realpath(sys.argv[0]))


suStart = getpass.getpass("Please Enter your root Password (It wont be stored)")

suPass = suStart

passw = getpass.getpass("Please Enter your user Password (It wont be stored)")

userPass = passw

userName = getpass.getuser()

location = getScriptPath()

#sudoRun()

#time.sleep(3)

#sshRun()

#time.sleep(15)

dockerRun()
