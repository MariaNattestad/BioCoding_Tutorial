########################################################################################
##
##                  An intro to Python for biology
##
########################################################################################

########################################################################################
######################## Variables and print statements ################################
########################################################################################

# this is a comment, use these to tell people what your code does

mystring = "Homo sapiens" # a string, letters, words, sentences, anything in quotes
myinteger = 4 # an integer
myfloat = 4.0 # a float (a number with a decimal point)

print "This is a string: %s, this is a float: %f, and this is an integer: %d" % (mystring,myfloat,myinteger)

print "We are %s and there are %d bases in our DNA" % (mystring, myinteger)

# use %s when you need a string
# use %d when you need an integer
# use %f when you need a float (a number with a decimal point)


########################################################################################
################################### Basic Math #########################################
########################################################################################

myfloat = 2.0
yourfloat = 3.0
print myfloat/yourfloat


myint = 2
yourint = 3
print myint/yourint

# The anwer is 2/3 = 0.666666667 but Python and many other programming lanuages have a quirk where they think that any math you do with integers can only output another integer. 
# Let's explore this and see if we can find tricks to deal with it

myint = 2
yourint = 3

# Which of these work and why?

print float(myint)/yourint # 1

print myint/float(yourint) # 2

print (myint+0.0)/yourint # 3

print myint/yourint + 0.0 # 4

print myint*1.0/yourint # 5

print myint/yourint*1.0 # 6


########################################################################################
########################### Lists, strings, and for loops ##############################
########################################################################################


####### LISTS #######
mylist = [6,3,6,7,2,6,2,9,7,0]
print mylist

print mylist[0]
print mylist[1]
print mylist[2]

###### STRINGS ######
# strings are like lists of letters, so you can get individual letters using the bracket notation

mystring = "ACGT"
print len(mystring) ## => 4

print mystring[0]
print mystring[1]
print mystring[2]
print mystring[3]
#print mystring[4] # Error:"string index out of range" 


DNA = "CAACGGGCAATATGTCTCTGTGTG"
print "Your DNA is %d bases long" % (len(DNA))

print DNA[7]

######### lists can contain anything #########

mylist = [1,"anything",2.45,5,10,"Hello world"]

print mylist[4]

####### you can also make lists longer ######
print mylist

mylist.append(56)

print mylist

# this means you can start with an empty list and add to it:
nucleotides = []
nucleotides.append("A")
nucleotides.append("C")
nucleotides.append("G")
nucleotides.append("T")
print nucleotides

########## QUESTION 3: Which of these are correct? Which give errors? ###########



################ indexing lists ###################

mylist = range(10)

print mylist

print mylist[0:10]
print mylist[:]
print mylist[1:10]
print mylist[4:8]
print mylist[3:]
print mylist[0:10:2] # what does the third number do?
print mylist[0:7:3]
print mylist[::-1] # what does this do?





###### Two different versions of a "for loop" #######

for letter in DNA:
    print letter
    
# the variable letter can be anything, try switching it out with tomato

for tomato in DNA:
    print tomato

# we only call it letter so it makes sense. This becomes important when you have many more variables. At that point, naming them after fruits suddenly isn't funny anymore.


# you can also make a for loop like this: 
# xrange gives a list from 0 to len(DNA), so i loops through that list
for i in xrange(len(DNA)):
    print i

# when you do this, you get the bases in the DNA by saying DNA[i]
for i in xrange(len(DNA)):
    print "Letter number %d in your DNA is %s" % (i,DNA[i])
    
# sometimes we really care about the indices, like when we are dealing with 2 or more lists in parallel
DNA = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
RNA = "AGCUUUUCAUUCUGACUGCAACGGGCAAUAUGUCUCUGUGUGGAUUAAAAAAAGAGUGUCUGAUAGCAGC"

length = len(DNA)

for i in xrange(length):
    print "DNA: %s, RNA: %s" % (DNA[i],RNA[i])
    
    
    
# xrange can do many things:

for b in xrange(0,4,1): #  start=0,stop=4,step=1
    print b

for j in xrange(2,10,2):
    print j

########## Now you try to print (1,3,5,7,9) using a for loop ###########


########### You can also make empty strings and add to them #############

DNA = "AGCTTTTCATTC"

# just like lists, you can also add to strings:
mystring = str() # makes an empty string, just like mylist = [] makes an empty list

for i in xrange(len(DNA)):
    mystring+=DNA[i]

print mystring


# how is this different from making a list?

mylist = []

for i in xrange(len(DNA)):
    mylist.append(DNA[i])

print mylist

# if you do make a list and want it to be a string, you can always just do this:

mystring = str()
for item in mylist:
    mystring+=item
print mystring





########################################################################################
################################## If statements #######################################
########################################################################################

    
#What do you think this does?

correct=True # this is another kind of variable, called a boolean: it can only be True or False

if correct==True:
    print "You are right!"
else:
    print "You are wrong!"
    

# You can set as many cases as you want using elif (short for "else if")
    
mystring = "ABCYSGD"
for letter in mystring:
    if letter == "A":
        print "Alpha"
    elif letter == "B":
        print "Bravo"
    elif letter == "C":
        print "Charlie"
    elif letter == "D":
        print "Delta"
    else:
        print "Ummm, I don't know what %s is in military speak" % (letter)


# You can also use these if statements for input validation
# If you ask the user for a string of DNA, it would be nice to check that the string looks like DNA before you do a lot of work with it

############### Challenge: Loop through this string of DNA and output a message to the user for every letter that isn't A, T, C, or G

DNA = "AGCUUUUCATKCTGACUUNNNAACGGGCAATAUGTCTCTGTHTGGATTAAAAAAAGAGTGTCMGATAGCAGC"



# This is called "Input validation"

# Now that you can validate a user's input, let's learn how to actually ask the user for input. It's pretty simple:


DNA = raw_input('Enter your DNA: ')

# whatever the user writes before pressing enter gets stored in the variable DNA

######## We can also check multiple things at once #########

letter = "A"

if letter=="A" or letter=="G":
    print "Purine"
elif letter=="U" or letter=="T" or letter=="C":
    print "Pyrimidine"
else:
    print "Not a nucleotide"



########################################################################################
##################################### Functions ########################################
########################################################################################
mylist = [1,2,3,4,100]

#built-in functions:
min(mylist)
max(mylist)
sum(mylist)


# General syntax for making your own functions:

def function_name(argument1,argument2,etc): # don't forget the colon
    # do something with the arguments
    something = argument1+argument2*etc
    return something

result = function_name(3,4,2)
# an example:

def double(mylist):
    doubled = []
    for item in mylist:
        doubled.append(item*2)
    return doubled
    
result = double(mylist)
print result
# What happens if we call double() and pass it a string?
# Try it!


# write a function that takes in a list, loops through it, and adds each item to a string
# we saw some code that did that already, so just turn it into a function 
# make sure to return the string at the end


########################################################################################
################################### Dictionaries #######################################
########################################################################################



# a dictionary is very useful, it is a data structure (meaning it keeps data organized)
# it has a bunch of key:value pairs just like a real dictionary, every word has a definition
# you can also think of it as a decoder, every key is a code, and every value
# stored with the code is what that code means

my_dictionary = {"key":"value","secondkey":"secondvalue","thirdkey":"thirdvalue"}

print my_dictionary["secondkey"]
print my_dictionary.keys()

print my_dictionary.values()

for key in my_dictionary:
    print "Key: %s, Value: %s" % (key,my_dictionary[key])

# notice that the order of the dictionary isn't how we started it
# dictionaries are automatically sorted so they are really fast to search
# we use a key in a dictionary just like we normally use an index in a list or array

# the useful part is when we use the dictionary as a decoder:
mystring = "ABCYSGD"

military = {"A":"Alpha", "B":"Bravo", "C":"Charlie", "D":"Delta"}

for letter in mystring:
    print military.get(letter,"Ummm, I don't know what %s is in military speak" % letter)


# remember we did the same thing with if statements before?
# military is a dictionary: the perfect decoder
# .get() is a method that all dictionaries have when they are created, 
# the first argument is the key (or the code) and the second is the default 
# the default is when the key isn't found 
# military["Y"] # gives an error: you can try it
# but military.get("Y","?") # doesn't crash your application




# DNA has a recipe for proteins with the code being each set of three nucleotides 
# then this is made into RNA (all the T's become U's)
# (bases or letters: AGA, ACU, GUU, etc.)
# the code "UUA" means the amino acid "L" or "Leucine"



# this website has all the codes, can you make them into a dictionary?
# https://www.manylabs.org/file/lessonMedia/69/geneticCode.png
# Hint: we are gonna use this for the third project!


########################################################################################
##############################  File input/output  #####################################
########################################################################################

############## INPUT ###############

# open a file
f = open("filename",'r') # 'r' means read
for line in f:
    print line

f.close() 


############## OUTPUT ###############
f2 = open("filename",'w') # 'w' means write, so you overwrite the file
f2.write("Hello world")
f2.write("\n") # \n means newline, as in pressing enter
for i in xrange(10):
    f2.write("%d\t" % i) # \t means tab

f2.close()# close the file safely to make sure the last part you wrote is saved

# once f2 is closed, you can reuse the name

f2 = open("filename2",'a') # 'a' means append, so you add to the file each time
f2.write("Hello world")
f2.write("\n") # \n means newline, as in pressing enter

for i in xrange(10):
    f2.write("%d\t" % i) # \t means tab

f2.close()




########################################################################################
######################################  Numpy  #########################################
########################################################################################

# Try to find a function that would take the average, like mean(), average(), or avg() can you find one?
# If you want to do something simple and can't find a function for it, you can search online.
# Many of the simple math and science functions are in a module named numpy:

import numpy as np 
# np is a common nickname for numpy, so now when you want to use it, you say:
print np.mean(mylist)

# Modules are packages of functions and other useful things, including something called an array
# arrays are a bit like lists, but they are only for numbers, 
# that way you can do math on an entire array at once instead of looping through the list and doubling every element like we did before

mylist = [1,2,3,4,100]
myarray = np.array(mylist) # this takes mylist and makes it into an array, once again np is just the nickname for numpy

print "doubling a list:"
print mylist*2
print "doubling an array:"
print myarray*2

# many things we do are easier with arrays, including anything involving math
# An important thing to keep in mind is how to start an empty array if you don't want to just make a list into an array

# if you have a sentence, and you want to save the lengths of all the words:

sentence = "if you have a sentence, and you want to save the lengths of all the words"

# one of many built-in tricks: 
words = sentence.split()
# this one looks like a function but flipped around. This is because it's a built-in method for a string. 
# sentence is a string, and all strings have a bunch of methods that you can call by doing sentence.methodname()
# Methods are functions that belong to objects, so split() is a method that all strings have when they are created, and you can use them whenever you need to
# Other functions we made don't belong to any particular object, so they are very flexible. 

# using a list:
lengths=[]
for word in words:
    lengths.append(len(word))
print lengths

# you can then convert this to an array:
lengths=np.array(lengths)


# using an array:
lengths = np.zeros(len(words))
for i in xrange(len(words)):
    lengths[i]=len(words[i])
print lengths

# using the array seems harder in this case, but sometimes it might come in handy. 

# I usually start with lists and convert them to arrays right before I have to do math on them


######## useful numpy functions ###########

print np.std(myarray)
print np.random.rand(10) # multiply, add, or round to get the random numbers you need

# I want 100 random numbers from 10 up to and including 15, but only integers
print np.floor(np.random.rand(100)*6+10)  

# np.floor() rounds down, you can also use np.ceil() to round up, or np.around() to round up or down, whichever is closest (like you learn in school)

# There are tons of numpy modules, just search online.
# Anything you have ever seen in a math class will probably exist in numpy








