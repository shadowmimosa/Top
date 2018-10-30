from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copy from %s to %s." % (from_file, to_file))

# we could do these two on one line too,how?
input = open(from_file)
indata = input.read()

print(" Does the output file exist?%r" % exists(to_file))
print("Ready,hit RETURN to continue,Ctrl^C to abort")
# input()

output = open(to_file, 'w')
output.write(indata)

print("Alright,all done.")

output.close()
input.close()
