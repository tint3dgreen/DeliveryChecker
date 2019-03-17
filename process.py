import Math
import time
while True:
	time.sleep(10)
	data = open("kiddo.txt","r")
	hJerk = 0
	numShock = 0
	prev = 1
	current = 0
	for x in file1:
		prev = current
		current = x
		val = (Math.abs(double(current) - double(prev))
		if val > hJerk:
			hJerk = val
		if val > .5:
			hShock ++
	j.open("data.json","w")
	j.write("{hJerk:%d,numShock:%d}"%(hJerk,numShock))




