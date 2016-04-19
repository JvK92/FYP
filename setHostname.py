import fileinput 
import getpass

user = getpass.getuser()

f1 = open('/etc/hostname', 'r')
hostname = ""

with f1 as f:
	hostname = f.read()


