import xml.etree.ElementTree as ET

tree=ET.parse('config.xml')
print(tree)
root=tree.getroot()
print(root)

db_config = root.find('database')
print(db_config.find('host').text)
print(db_config.find('port').text)
logging=root.find('logging')
print(logging.find('level').text)
print(logging.find('file').text)