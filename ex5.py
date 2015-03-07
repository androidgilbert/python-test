my_name="zhouchao"
my_age=28
my_height=181
my_weight=190
my_eye="black"
my_teeth="white"
my_hair="black"

print "Let's talk about %r." %my_name
print "He's %r inches tall."%my_height
print "He's %d pounds heavy,"%my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair."%(my_eye,my_hair)
print "His teeth are usually %s depending on the coffee" %my_teeth

#this line is tricky,try to get it exactly right
print "If I add %d,%d,and %d I get %d." %(my_age,my_height,my_weight,my_age+my_height+my_weight)