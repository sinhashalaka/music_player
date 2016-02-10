import subprocess
from subprocess import check_output 
import curses


out = check_output("ls |grep .mp3",shell=True,stderr=subprocess.STDOUT,)
l = list()
l = out.split("\n")
print (out)
n = len(l)
n = n-1
count = 0 
print ("Enter 's' to start or enter song no. \n ")
c = raw_input("=>")
while True:
	if c == 's':
		count = 0
		print ("playing ... "+l[0])
		return_code = subprocess.call(["afplay", l[count]])
	elif c == 'n':
		if count+1 < n :
			count = count + 1
			print ("playing ... "+l[count])
			return_code = subprocess.call(["afplay", l[count]])
		else :
			print ("Song not available\n")
	elif c == 'p':
		if count-1 >= 0:
			count = count-1
			print ("playing ... "+l[count])
			return_code = subprocess.call(["afplay", l[count]])
		else :
			print ("Song not available")
	elif c.isdigit():
		p = count
		count = int(c)-1
		if count < 0 or count >= n:
			print ("Song not available")
			count = p
		else : 
			print ("playing ... "+l[count])
			return_code = subprocess.call(["afplay", l[count]])
	c = raw_input("Enter 'n' to choose next song , 'p' to choose previous song or song no. \n => ")
import time
time.sleep(50)