# This first line is provided for you

# hrs = input("Enter Hours:")
# rate= float(hrs) * 2.75
# print("Pay: " + str(rate))

# hrs = input("Enter Hours:")
# h = float(hrs)
# rate = input("Enter Rate:")
# r = float(rate)
# gross = h * r

# if(h > 40):
#     extrahours = h - 40
#     extrapay = 1.5 * (extrahours * r)
#     normpay =  40 * r
#     print(normpay + extrapay)

# 3.3 Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error. 
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. 
# For the test, enter a score of 0.85. 
# try:
#     score = input("Enter a score: ")

#     float_score = float(score)

#     if(float(score) <= 1):
#         if(float_score >= 0.9):
#             print("A")
#         elif(float_score >= 0.8):
#             print("B")
#         elif(float_score >= 0.7):
#             print("C")
#         elif(float_score >= 0.6):
#             print("D")
#         else:
#             print("F")
#     else:
#         print("error, out of range")
# except ValueError:
#     print("invalid value")

# 4.6 Write a program to prompt the user for hours and rate per hour 
# using input to compute gross pay. Pay should be the normal rate for 
# hours up to 40 and time-and-a-half for the hourly rate for all hours 
# worked above 40 hours. Put the logic to do the computation of pay in a 
# function called computepay() and use the function to do the computation. 
# The function should return a value. Use 45 hours and a rate of 10.50 per 
# hour to test the program (the pay should be 498.75). You should use input to 
# read a string and float() to convert the string to a number. Do not worry 
# about error checking the user input unless you want to - you can assume the user 
# types numbers properly. Do not name your variable sum or use the sum() function. 

# def computepay(hours, rate):
    
#     if(hours > 40):
#         extrahours = hours - 40
#         extrapay = (40 * rate) + 1.5 * (extrahours * rate)
#         return extrapay
#     else:
#         pay = 40 * rate
#         return pay
    
# hours = input("Enter hours: ")
# rate = input("Enter rate: ")
# hours_float = float(hours)
# rate_float = float(rate)

# printpay= computepay(hours_float, rate_float)

# print("Pay", printpay)

# 5.2 Write a program that repeatedly prompts a user for integer numbers 
# until the user enters 'done'. Once 'done' is entered, print out the largest 
# and smallest of the numbers. If the user enters anything other than a valid 
# number catch it with a try/except and put out an appropriate message and ignore 
# the number. Enter 7, 2, bob, 10, and 4 and match the output below. 

# largest = None
# smallest = None

# while True:
#     try:
#         num = input("Give a number: ")
#         if num == "done":
#             break

#         number = int(num)
#     except:
#         print("Invalid input")
#         continue

#     if largest is None and smallest is None:
#         smallest = number
#         largest = number
#     elif number > largest:
#         largest = number
#     elif number < smallest:
#         smallest  = number

# print("Invalid input")
# print("Maximum is ", largest)
# print("Minimum is ", smallest)

# text = "X-DSPAM-Confidence:    0.8475"

# text.strip()
# colon = text.find(":")
# number = text[colon+1:]

# numberfloat = float(number)
# print(numberfloat)

# 9.4 Write a program to read through the mbox-short.txt 
# and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of 
# those lines as the person who sent the mail. The program creates a 
# Python dictionary that maps the sender's mail address to a count of 
# the number of times they appear in the file. After the dictionary is 
# produced, the program reads through the dictionary using a maximum loop 
# to find the most prolific committer.

# filename = input("Enter filename:")
# try:
#     handle = open(filename)
# except:
#     print("file invalid")
#     quit()

# dictionary = dict()
# list = list()

# for line in handle:
#     line = line.rstrip()
#     if line.startswith("From:"):
#         continue
#     if line.startswith("From "):
#         words = line.split()
#         list.append(words[1])

# for word in list:
#     dictionary[word] = dictionary.get(word, 0) + 1

# # print(dictionary)
# largest = None
# value = None

# for k,v in dictionary.items():
#     if largest is None or v > largest:
#         largest = v
#         value = k

# print(value, largest)

# 10.2 Write a program to read through the mbox-short.txt and 
# figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and 
# then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, 
# sorted by hour as shown below.

# filename = input("Enter filename:")
# try:
#     handle = open(filename)
# except:
#     print("file invalid")
#     quit()

# dictionary = dict()
# mylist = list()

# for line in handle:
#     line = line.rstrip()
#     if line.startswith("From:"):
#         continue
#     if line.startswith("From"):
#         line = line.split()
#         time = line[5].split(":")
#         hour = time[0]
#         dictionary[hour] = dictionary.get(hour, 0) + 1

# for k, v in dictionary.items():
#     newtuple= k,v
#     mylist.append(newtuple)

# mylist = sorted(mylist)

# for v,k in mylist:
#     print(v, k)

#get the total
# import re

# handle = open("regex_sum_1984846.txt")
# total = 0
# mylist = list()

# for line in handle:
#     line = line.rstrip()
#     numbers = re.findall('[0-9]+', line)
#     if len(numbers) == 0: continue
#     for number in numbers:
#         mylist.append(int(number))

# for i in mylist:
#     total = total + i
# print(total)

#done in list comprehension
# print( sum( [ int(number) for line in handle for number in re.findall(r'[0-9]+', line.rstrip()) ] ) )

# string = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

# find = re.findall("@\S+", string)
# print(find)

# You are to retrieve the following document using the HTTP protocol 
# in a way that you can examine the HTTP Response headers.

# import socket

# mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysocket.connect(("data.pr4e.org", 80))
# cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n".encode()
# mysocket.send(cmd)

# while True:
#     data = mysocket.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
# mysocket.close()

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl

# #SSL certificate error handler
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input("Enter url: ")
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")

# mylist = list()
# total = 0

# tags = soup("span")
# for tag in tags:
#     contents = tag.contents[0]
#     numbers = contents.split()
#     for number in numbers:
#         mylist.append(int(number))

# for num in mylist:
#     total = total + num
# print(total)

# The program will use urllib to read the HTML from the data files below, extract 
# the href= vaues from the anchor tags, scan for a tag that is in a particular 
# position relative to the first name in the list, follow that link and repeat 
# the process a number of times and report the last name you find.

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input("Enter url: ")
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")

# mylist = list()

# count = input("Enter count: ")
# count = int(count)
# pos = input("Enter position: ")
# pos = int(pos)
# tags = soup("a")

# print(url)

# for i in range(count):  
#     tag = tags[pos-1].get('href', None)
#     print(tag)
#     html = urllib.request.urlopen(tag, context=ctx).read()
#     soup = BeautifulSoup(html, "html.parser")
#     tags = soup("a")

