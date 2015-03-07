from sys import argv
script,filename=argv
print "we will handle the %r file "%filename
target=open(filename,'w')
target.truncate()
line1=raw_input("line 1:")
line2=raw_input("line 2:")
line3=raw_input("line 3:")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "will closed"
target.close()