#!/usr/bin/python

# Copyright (c) 2018 by Martin Willner <mjw@mjw.co.at>


# sudo hciconfig hci0 up
# sudo rfcomm connect hci0 00:90:72:56:93:94
#

import serial, time,sys

if len(sys.argv) == 2:
	sleeptime=float(sys.argv[1])
else:
	sleeptime=0.5
	
rfcomm=serial.Serial("/dev/rfcomm0", 9600)
rfcomm.flushInput()


print "#record steps: "+str(sleeptime)+"s"
print "#V	A	W	C"
while True:
	rfcomm.write("\xf0")
	s =rfcomm.read(130)
	#print ":".join("{:02x}".format(ord(c)) for c in s) # raw packet
	voltage=int((ord(s[2]) <<8)| ord(s[3])) 
	current=int((ord(s[4]) <<8)| ord(s[5]))
	power=int((ord(s[6]) <<24)| (ord(s[7]) <<16)| (ord(s[8]) <<8)|ord(s[9]))
	tempC=int((ord(s[10]) <<8)| ord(s[11])) 
	print str(voltage/100.0)+"\t"+str(current/1000.0)+"\t"+str(power/1000.0)+"\t"+str(tempC)
	time.sleep(sleeptime)
rfcomm.close()
