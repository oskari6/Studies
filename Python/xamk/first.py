##get the average of the floating point numbers of this file

# filename = input("give a file name: ")
# try:
#     openfile = open(filename)
# except:
#     print("file name is invalid")
#     quit()

# count = 0
# sum = 0
# for line in openfile:
#     if line.startswith("X-DSPAM-Confidence:"):
#         floatnum = line[20:27]
#         sum = sum + float(floatnum)
#         count = count + 1
# average = sum / count
# print("Average spam confidence:", average)

#8.4 Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split() 
# method. The program should build a list of words. 
# For each word on each line check to see if the word is already in the 
# list and if not append it to the list. When the program completes, 
# sort and print the resulting words in python sort() order as shown 
# in the desired output.

# filename = input("Enter filename:")
# try:
#     openfile = open(filename)
# except:
#     print("file invalid")
#     quit()

# mylist = list()

# words = openfile.read()
# wordlist = words.split()

# for word in wordlist:
#     if word not in mylist:
#         mylist.append(word)
#     else:
#         continue

# mylist.sort()
# print(mylist)

# 8.5 Open the file mbox-short.txt and read it line by line. 
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second 
# word in the line (i.e. the entire address of the person who sent the 
# message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. 
# Also look at the last line of the sample output to see how to print the 
# count.

# filename = input("Enter filename:")
# try:
#     openfile = open(filename)
# except:
#     print("file invalid")
#     quit()

# count = 0

# for line in openfile:
#     line.rstrip()
#     if line.startswith("From:"):
#         continue
#     if line.startswith("From "):
#         words = line.split()
#         print(words[1])
#         count = count + 1

# print(f"There were {count} lines in the file with From as the first word")

# 9.4 Write a program to read through the mbox-short.txt 
# and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of 
# those lines as the person who sent the mail. The program creates a 
# Python dictionary that maps the sender's mail address to a count of 
# the number of times they appear in the file. After the dictionary is 
# produced, the program reads through the dictionary using a maximum loop 
# to find the most prolific committer.

filename = input("Enter filename:")
try:
    handle = open(filename)
except:
    print("file invalid")
    quit()

dictionary = dict()

for line in handle:
    line = line.rstrip()
    if line.startswith("From:"):
        continue
    if line.startswith("From "):
        words = line.split()

    for word in words:
        if word is words[1]:
            dictionary[word] = dictionary.get(word, 0) + 1

largest = -1
value = None

for k,v in dictionary.items():
    if v > largest:
        largest = v
        value = k

print(value, largest)