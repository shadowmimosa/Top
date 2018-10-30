from sys import argv

script, filename = argv

print("We'are going to erase %r." % filename)
print("If you don't want this,hit Ctrl-C (^C).")
print("If you do want this,hit RETURN")

input("?")

print("open the file...")
target = open(filename, 'w')

print("Truncating the file. Good Bye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("Im going to write these to the file")

target.weite(line1)
target.weite("\n")
target.weite(line2)
target.weite("\n")
target.weite(line3)
target.weite("\n")

print("And finally,we close it.")
target.close()
