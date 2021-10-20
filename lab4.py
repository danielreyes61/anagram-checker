#Let's write an anagram checker.

#Anagram
#Two words are anagrams of each other if the letters of one can be rearranged to fit the other. e.g. dormitory and dirtyroom.

#Write a program that lets the user enter two strings, and tells them if they are anagrams of each other.

#Convert the strings into lists
#Sort the letters of each list
#Check if the two lists are equal
#>>> enter the first word: dormitory
#>>> enter the second word: dirtyroom
#>>> 'dormitory' and 'dirtyroom' are anagrams
#One potential solution to this lab involves Python's built-in function sorted(), which will sort list items as well as characters in a string. However, please use the list method for sorting the lists in this lab instead.



# Daniel Reyes
# 27JAN2021

firstWord = input("Enter the first word: ")
secondWord = input("Enter the second word: ")
firstWordDictionary = {}
secondWordDictionary = {}
# Put a lot of effort into making it so that the words are evaluated in one pass for efficiency.
# This program adds the letters to the dictionary if they are not already there.
# If they are in the dictionary, it updates the value by 1, when the for loop is over,
# the dictionaries are compared, if they are equal, the program prints that they are anagrams.
# There is no elif at the end because the only other option is they are not anagrams.
if len(firstWord) != len(secondWord):     #  Quick check here to see if they are not even equal,
    print("These words are not anagrams. ") # and most definitely not anagrams.
else:
    for x in range(0,len(firstWord),1):
        if firstWord[x] in firstWordDictionary:

            y = int(firstWordDictionary[firstWord[x]])
            firstWordDictionary[firstWord[x]] = y+1
        else:
            firstWordDictionary[firstWord[x]] = 1

    for x in range(0,len(secondWord),1):
        if secondWord[x] in secondWordDictionary:

            y = int(secondWordDictionary[secondWord[x]])
            secondWordDictionary[secondWord[x]] = y+1
        else:
            secondWordDictionary[secondWord[x]] = 1

if firstWordDictionary == secondWordDictionary:
    print("These are anagrams.")
else:
    print("These are not anagrams.")

print(firstWordDictionary)  #print function left here just to make it easier to check my work
print(secondWordDictionary)
