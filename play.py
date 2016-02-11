import subprocess
from subprocess import check_output 
import psutil
import time


#check for mp3 files
out = check_output("ls |grep .mp3",shell=True,stderr=subprocess.STDOUT,).decode("utf-8")
l = list()
l = out.split("\n")
#list of mp3 files in the folder
print (out)
n = len(l)
n = n-1
count = 0 
print ("Enter 's' to start or enter song no. \n ")
c = input("=>")
while True:
	if c == 's':
		#start music player
		count = 0
		print ("playing ... "+l[0])
		return_code = subprocess.Popen(["afplay", l[count]]).pid
	elif c == 'n':
		#play next song
		if count+1 < n :
			count = count + 1
			print ("playing ... "+l[count])
			return_code = subprocess.Popen(["afplay", l[count]]).pid
		else :
			count = 0
			print ("playing ... "+l[count])
			return_code = subprocess.Popen(["afplay", l[count]]).pid
	elif c == 'p':
		#play previous song
		if count-1 >= 0:
			count = count-1
			print ("playing ... "+l[count])
			return_code = subprocess.Popen(["afplay", l[count]]).pid
		else :
			count = n-1
			print ("playing ... "+l[count])
			return_code = subprocess.Popen(["afplay", l[count]]).pid
	elif c.isdigit():
		#play the song having song no. 'c'
		p = count
		count = int(c)-1
		if count < 0 or count >= n:
			print ("Song not available")
			count = p
		else : 
			print ("playing ... "+l[count])
			return_code = subprocess.Popen(["afplay", l[count]]).pid
	elif c == 'r':
		#repeat the current song
		print ("playing ..."+l[count])
		return_code = subprocess.Popen(["afplay" , l[count]]).pid
	c = input("Enter 'n' to choose next song , 'p' to choose previous song  , 'r' to repeat or song no. \n => ")
	if c == None:
		c = 'n'
	p = psutil.Process(return_code)
	#terminate the current process(stop the current song) and start the chosen one
	p.terminate() 
time.sleep(50)
