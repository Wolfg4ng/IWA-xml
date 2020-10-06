import xml.etree.ElementTree as ET
tree = ET.parse('test.xml')
root = tree.getroot()

for i in root.findall(".//module"):
    print(i)