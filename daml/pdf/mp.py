from sys import argv
import os

prefix = argv[1]
print(prefix)
files = os.listdir('.')
for file in files:
	if file != "mp.py":
		os.rename(file, prefix+file)
