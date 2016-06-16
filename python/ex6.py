# variables type of string
x = "There are %d types of people." % 10#number include to x
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)#puts 1.two variables(string) is put inside the y(string)

print x
print y

print "I said: %r." % x# puts 2.
print "I also said: '%s'." % y #puts 3.

hilarious = False# boolean variable
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious# puts boolean variable hilarious int string variable 

w = "This is the left side of..."
e = "a string with a right side."

print w + e #puts 4.