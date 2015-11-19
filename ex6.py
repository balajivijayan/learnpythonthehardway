x = "There are %d types of people in the world" %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who know %s" %(binary, do_not)

print x
print y

print "I said: %r." %x
print "I also said: '%s'." %y

hilarious = False
joke_evaluation = "Isn't this joke funny ?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "A string with right side"

print w + e