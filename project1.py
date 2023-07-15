## Please enter your name and matric number as a comment below
## Name: KIERON CHAN JAI YONG
## Matric number: U2230673F
## For this project you will need to create a multilingual search tool that
## reads an interlinear corpus from raw text and allows you to search on
## multiple levels. Keep in mind that the raw text will first need to be
## processed and stored in some format before you can develop a search function.
## Below are ten steps using a simple example to get you started.

print("1.") # step one
# this is a single interlinearized sentence from the Pnar corpus in Toolbox format
with open('example.txt', 'r') as example: # open in read mode
    for line in example:
        print(line) # first let's see how our interpreter views it

print("---") # print a separator

print("2.") # step two
# there's extra spaces between lines, so let's try to strip those
with open('example.txt', 'r') as example: # open in read mode
    for line in example:
        print(line.strip())

print("---") # print a separator

# Each line is identified by a marker: \tx corresponds to the text, \mb is the
# morphemes, \ph is phonetic/phonemic transcription, \ge is the English gloss,
# \ps is the part of speech, and \ft is the free translation. We need to clean
# up the text first so we can parse it.

print("3.") # step three
# We can see that some words are broken up as morphemes. In order to create a
# search function, we will need each word to be aligned properly. We can
# observe that the "-" and "=" characters identify morpheme boundaries for
# affixes and clitics, respectively. We can deal with this by splitting each
# line on whitespace, and then joining, then replacing "- " and "= " with "-"
# and "=" respectively.
with open('example.txt', 'r') as example:
    for line in example:
        print(" ".join(line.strip().split()).replace("- ", "-").replace("= ", "="))

print("---") # print a separator

print("4.") # step four
# There is also an extra space between the free translation and the other lines
# so let's get rid of that.
with open('example.txt', 'r') as example:
    for line in example:
        if line != "\n":
            print(" ".join(line.strip().split()).replace("- ", "-").replace("= ", "="))

print("---") # print a separator

print("5.") # step five
# Now we are able to print out the example in the terminal, but in order to
# search through it we need to store it. Let's create a container to do that.
examplelines = []
with open('example.txt', 'r') as example:
    for line in example:
        if line != "\n":
            examplelines.append(" ".join(line.strip().split()).replace("- ", "-").replace("= ", "="))

print(examplelines)
print("---") # print a separator

print("6.") # step six
# We now have this example stored as a list, but how can we organize it so as
# to align each item in a row with its corresponding item in another row?
# Consider what kind of container would be useful here, and how would you store
# it in order to access it with a search function? Once you have managed to
# store a single example, consider how you would extend that functionality to
# multiple interlinearized sentences. Let's try first with a dictionary:
exampledict = {}
with open('example.txt', 'r') as example:
    # we can use the enumerate() function to number the lines
    for num, line in enumerate(example):
        if line != "\n":
            # now we can create keys from the numbers
            exampledict[num] = " ".join(line.strip().split()).replace("- ", "-").replace("= ", "=")

print(exampledict)
print("---") # print a separator

print("7.") # step seven
# Now we have a dictionary with line numbers as keys, but we can't access
# individual tokens on lines. Let's turn the lines into lists.
exampledict = {}
with open('example.txt', 'r') as example:
    for num, line in enumerate(example):
        if line != "\n":
            # create a string variable from the line
            spline = " ".join(line.strip().split()).replace("- ", "-").replace("= ", "=")
            # then split the string on whitespace
            exampledict[num] = spline.split()

print(exampledict)
print("---") # print a separator

print("8.") # step eight
# It might be easier to use line markers as keys, let's try that
exampledict = {}
with open('example.txt', 'r') as example:
    for num, line in enumerate(example):
        if line != "\n":
            # create a string variable from the line
            spline = " ".join(line.strip().split()).replace("- ", "-").replace("= ", "=")
            # then split the string on whitespace
            spline = spline.split()
            # the line marker is always the first item in the split list
            # so use that as the key, and the rest of the list as the value
            exampledict[spline[0]] = spline[1:]

print(exampledict)
print("---") # print a separator

print("9.") # step nine
# let's do it again but remove the '\\' characters at the beginning of the line marker
exampledict = {}
with open('example.txt', 'r') as example:
    for num, line in enumerate(example):
        if line != "\n":
            # create a string variable from the line
            spline = " ".join(line.strip().split()).replace("- ", "-").replace("= ", "=").replace("\\", "")
            # then split the string on whitespace
            spline = spline.split()
            # the line marker is always the first item in the split list
            # so use that as the key, and the rest of the list as the value
            exampledict[spline[0]] = spline[1:]

print(exampledict)
for v in exampledict.values():
    print(len(v))
print("---") # print a separator

print("10.") # step ten
# Now we can access this example via keys and slices in the dictionary.
print(exampledict['tx'][4], exampledict['ps'][4], exampledict['ge'][4])
print("---") # print a separator

# Dictionaries can contain other dictionaries, and these can be embedded
# iteratively. You can extend this example for your use case or figure out
# another way of handling storage, perhaps by using a dataframe. The next step
# is to write a function that will allow you to search for texts based on these
# multiple interlinear levels. Now that you know one way of accessing stored
# text, your task is to figure out the rest. Good luck!

# take in two texts, combine into single corpus
# clean up data
# create function to allow searching by gloss, part of speech, lookahead/behind etc.
# output should be contexts(sentences) that match this criteria
