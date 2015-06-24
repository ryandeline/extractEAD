from lxml import etree
import xml.etree.ElementTree as et
import os

parser = etree.XMLParser(remove_comments=False)

inpath = '/Users/admin/Documents/pyEAD/in'
outpath = '/Users/admin/Documents/pyEAD/out'

for filename in os.listdir(inpath):
	if not filename.endswith('.xml'): continue
	fullname = os.path.join(inpath, filename)
	tree = etree.parse(fullname)
	root = tree.getroot()
	# root.append(etree.Comment('Microsoft Photogrammetry'))
	for image_number in root.iter('image_number'):
		new_name = int(image_number.text) + 3000
		image_number.text = str(new_name)
	for exposure_number in root.iter('exposure_number'):
		new_name = int(exposure_number.text) + 3000
		exposure_number.text = str(new_name)

	outname = os.path.join(outpath, filename)
	tree.write(outname,xml_declaration=True, encoding="utf-8",)
	# print(len(parser.error_log))