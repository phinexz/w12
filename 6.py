x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#%r = Return a string containing a printable representation of an object.
print "I said: %r." % x #%r used 1
#%s = =string
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" #%r used 2 without any reference

print joke_evaluation % hilarious #%hilarious is used in place of %r

w = "This is the left side of..."
e = "a string with a right side."
# addition of strings
print w + e
