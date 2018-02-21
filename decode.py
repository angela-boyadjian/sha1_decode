#!usr/bin/env python3
import sys
import hashlib

if (len(sys.argv) < 3):
	print("Not enough arguments")
	sys.exit()
passwd = sys.argv[1]
list_w = sys.argv[2]
try:
	doc = open(list_w, "r")
except IOError:
        print("Invalid file.")
        sys.exit()
doc = doc.readlines()

def	sha1_decode(doc):
	for word in doc:
		hash = hashlib.sha1(word.encode('utf-8')[:-1])
		value = hash.hexdigest()
		if (passwd == value): 
			print('Password is: {0}'.format(word), end="")
			sys.exit()
	print('Password not found in given list')
	
sha1_decode(doc)