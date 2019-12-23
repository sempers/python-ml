import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
f.close()
lines1 = []
for line in lines:
	lines1.append(line.strip())
lines1.sort()
outF = open(sys.argv[1] + ".new", "w")
for line in lines1:
  # write line to output fil
    outF.write(line+"\n")
outF.close()