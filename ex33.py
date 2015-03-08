
def test_while(a,b):
	numbers=[]
	i=0
	while i<a:
	    print "At the top is %d"%i
	    numbers.append(i)
	    i=i+b
	    print "numbers now:",numbers
	    print "at the bottom i is %d"%i
	return numbers
def test_for(a):
	numbers=[]
	for i in range(0,a,3):
		print "at the top is %d"%i
		numbers.append(i)
		print "numbers now:",numbers
		print "at the bottom i is %d"%i
	return numbers
tests=test_while(8,3)
abc=test_for(8)
print "the numbers:"
for num in tests:
	print num
print "the abc:"
for a in abc:
	print a