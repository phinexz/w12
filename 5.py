name = 'Writik Saha'
age = 23 # not a lie
height = 187.96 # inches
weight = 81.6466 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %f, and %f I get %f." % (
    age, height, weight, age + height + weight)
