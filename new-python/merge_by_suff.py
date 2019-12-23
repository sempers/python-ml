import sys
import os

_suff = "FN_" #sys.argv[1] or "FN_"

resulting = []

for f in os.listdir("."):
	if not os.path.isdir(f) and f.startswith(_suff):
		h = open(f, "r")
		lines = h.readlines()
		h.close()
		resulting = resulting + lines + ["\n"]
h = open(_suff + "_ALL.txt", "w")
h.writelines(resulting)

print("OK")