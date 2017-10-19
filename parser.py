import sys
import re

path=open(sys.argv[1], "r")
parsed=open(sys.argv[2], "w")

lines = path.readlines()

for line in lines:
	if re.search("\w*:", line):
		parsed.write("\r\n\r\n"+str(line).rstrip('\n')[:-1]+",")
	else:
		parsed.write(str(line).rstrip('\n') +",")