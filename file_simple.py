import sys

filename = sys.argv[1]
file = open(filename,'w') #open file for write
content = file.write("My first File\n")
content = file.write("Second line\n")
file.close()

# read the whole file
file = open(filename,'r')
read_content = file.read()
print read_content
file.close()

# read line
file = open(filename,'r')
while True:
    line = file.readline()
    if not line: break
    print line
file.close()

file = open(filename,'r')
for line in file.readlines():
    if not line: break
    print line
file.close()
