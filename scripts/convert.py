import sys
import re

if len(sys.argv) != 2:
	sys.exit("usage: convert codepage_file")
	
pattern = re.compile("0x([a-zA-Z0-9]+)\s*0x([a-zA-Z0-9]+)")
bad_pattern = re.compile("0x([a-zA-Z0-9]+)\s*0x([a-zA-Z0-9]+)\s*0x([a-zA-Z0-9]+)")
	
f = open(sys.argv[1], "r")

a = []
for i in range(0, 256):
	a.append(0)
	
assert len(a) == 256

for line in f.readlines():
	if bad_pattern.search(line):
		sys.stderr.write("Uh oh, bad pattern matched!\n")
		continue
	match = pattern.search(line)
	if match != None:
		byte = int(match.group(1), 16)
		ucs = int(match.group(2), 16)
		a[byte] = ucs

n = 0
for ucs in a:
	sys.stdout.write("0x%04x, " % ucs)
	if n == 6:
		sys.stdout.write("\n")
		n = 0
	else:
		n += 1

sys.stdout.write("\n")
