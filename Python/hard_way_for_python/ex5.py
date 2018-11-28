my_name = 'Zed A. Shaw'
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'bule'
my_teech = 'White'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pound heavy." % my_weight)
print("That's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("He's teech are usually %s depenging on the coffee." % my_teech)

# this line is tricky,try to get it exactry right
print("If I add %d,%d,and %d I get %d." % (my_age, my_height, my_weight,
                                           my_age + my_height + my_weight))


# 英寸和磅转化为厘米和千克

inch = float(input("please input inch:"))
pound = float(input("please input pound:"))
print("%s is %rcm" % (inch, inch * 2.54))
print("%s is %rkg" % (pound, pound * 0.4535924))
