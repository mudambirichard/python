my_name = ('Zed A. Shaw')
my_age = 35
my_height = 74
my_weight = 180
my_eyes = ('blue')
my_teeth = ('white')
my_hair = ('brown')

print ( "Let's talk about %z.") % my_name
print ("He's %d inches tall.") % my_height
print ("He's %d pounds heavy." )% my_weight
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %shair.") % (my_eyes, my_hair)
print ("His teeth are usually %s depending on the coffe.") % my_teeth

print ("If I add %d, %d, and %d I get %d.") % (
    my_age, my_height, my_weight, my_age+my_height+my_weight)
