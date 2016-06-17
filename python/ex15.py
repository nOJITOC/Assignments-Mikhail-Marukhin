from sys import argv # import argv from module "sys"

script, filename = argv # variables , than put information from comand line

txt = open(filename) # open file with name "filename"

print "Here's your file %r:" % filename # output to screen string with filename
print txt.read() # output text from file with name "filename"

#print "Type the filename again:"
#file_again = raw_input("> ") # input name of file

#txt_again = open(file_again)# reopen file

#print txt_again.read() # output file again