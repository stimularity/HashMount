#!/usr/bin/python

#Mounts a truecrypt volume with a hashed password

import hashlib
import getpass
import sys
import os

#Path to truecrypt application
tcpath = "/Applications/TrueCrypt.app/Contents/MacOS/Truecrypt --text"

#Unique Name for the volume
volname = ""
#Location of the volume to open
vollocation = ""

#Volume Password
password = getpass.getpass()

#Volume Location
try:
	vollocation = sys.argv[1]
except IndexError:
	vollocation = raw_input("Enter Volume Location: ")

#Take the realitive location and get the exact location of volume
vollocation = os.path.realpath(vollocation)

#Volume Name
tname = vollocation.split(" ", 1)
volname = tname[len(tname)-1] #takes the last one, which it should be

#Hash the password a whole lot.
h = hashlib.sha512(password)
for i in range(0, 100):
		h.update(h.digest())

for i in range(0, 100):
		h.update(h.digest() + volname)

for i in range(0, 1000):
		h.update(h.digest() + h.digest())

password = h.hexdigest()[:64]
#print(password)

os.system(tcpath+" --mount /Users/stimularity/Dropbox/SecureFiles\ fizzix /Volumes/Secure -p "+password+" --explore --protect-hidden=no --keyfiles=")
