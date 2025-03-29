import xml.etree.ElementTree as ET

tree = ET.parse("sample.xml")
root = tree.getroot()

for item in root.findall("item"):
    name = item.find("name").text
    price = item.find("price").text
    print(name, price)