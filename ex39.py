ten_things="Apples Oranges crows telephone light sugar"
print "wait there is not 10 things in that list,let us fix that"
stuff=ten_things.split(' ')
more_stuff=['day','night','song','frisbee','corn','banana','girl','boy']
while len(stuff)!=10:
	next_one=more_stuff.pop()
	print "Adding",next_one
	stuff.append(next_one)
	print "there is %d items now."%len(stuff)
print "there we go.",stuff
print "let us do some things with stuff."
print stuff[1]
print stuff[-1]#whoa!fancy
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])