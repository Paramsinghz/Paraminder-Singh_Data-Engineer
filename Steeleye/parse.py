import xml.etree.ElementTree as ET

# parse the XML file
tree = ET.parse('D:/Steeleye/DLTINS_20210117_01of01.xml')

# get the root element
root = tree.getroot()

# print the tag of the root element
print(root.tag)

# iterate over child elements
for child in root:
    print(child.tag, child.attrib)

# access elements by their tag
element = root.find('tag_name')
if element is not None:
    print(element.text)
