people=30
cars=40
buses=15
if cars>people:
	print "we should take the cars"
elif cars<people:
	print "we should not take the cars"
else:
	print "we can't decide"

if buses>cars:
	print "that is too many buses"
elif buses<cars:
	print "maybe we could take the buses"
else:
	print "we still can not decide"

if people>buses:
	print "Alright,let us just take the buses."
else:
	print "file,let us stay home then."