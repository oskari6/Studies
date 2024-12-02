#The program will prompt for a URL, read the XML data from that 
# URL using urllib and then parse and extract the comment counts from the XML data, 
# compute the sum of the numbers in the file.

# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET
# import ssl

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# total = 0
# mylist = list()

# while True:
#     url = input("Enter url: ")
#     if len(url) < 1:
#         break

#     print('Retrieving', url)

#     uh = urllib.request.urlopen(url, context=ctx)
#     data = uh.read()
#     print('Retrieved', len(data), "characters")

#     tree = ET.fromstring(data)
#     lst = tree.findall("comments/comment")
#     count = len(lst)

#     for item in lst:
#         mylist.append(item.find("count").text)

#     print("Count:", count)

#     for num in mylist:
#         num = int(num)
#         total = total + num
#     print("Sum:", total)

#URL using urllib and then parse and extract the comment counts from the JSON data, 
# compute the sum of the numbers in the file and enter the sum below:

# import urllib.request, urllib.parse, urllib.error
# import json
# import ssl

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# total = 0
# count = 0
# mylist = list()

# while True:
#     url = input("Enter url: ")
#     if len(url) < 1:
#         break

#     print('Retrieving', url)

#     uh = urllib.request.urlopen(url, context=ctx)
#     data = uh.read()
#     print('Retrieved', len(data), "characters")

#     info = json.loads(data)
    
#     for item in info["comments"]:
#         mylist.append(item["count"])
#         count = count + 1

#     print("Count:", count)

#     for num in mylist:
#         num = int(num)
#         total = total + num
#     print("Sum:", total)

#The program will prompt for a location, contact a web service and retrieve 
# JSON for the web service and parse that data, and retrieve the first place_id 
# from the JSON. A place ID is a textual identifier that uniquely identifies a 
# place as within Google Maps.

# import urllib.request, urllib.parse, urllib.error
# import json
# import ssl

# api_key = "AIzaSyDXCR18bDmqoqZr0-FhvVMKwJRUaBPUSwo"

# serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# while True:
#     address = input("Enter location: ")
#     if len(address) < 1:
#         break

#     parms = dict()
#     parms["address"] = address
#     parms["key"] = api_key
#     url = serviceurl + urllib.parse.urlencode(parms)

#     print("Retriveing", url)
#     uh = urllib.request.urlopen(url, context = ctx)
#     data = uh.read().decode()
#     print("Retrieved", len(data), "characters")

#     try:
#         js = json.loads(data)
#     except:
#         js = None

#     if not js or "status" not in js or js["status"] != "OK":
#         print("Failure to Retrieve")
#         print(data)
#         continue

#     print(json.dumps(js, indent = 2))

#     id = js['results'][0]['place_id']

#     print(id)