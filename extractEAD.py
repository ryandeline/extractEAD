import csv ,os
from lxml import etree
import xml.etree.ElementTree as et

parser = etree.XMLParser(remove_comments=False)
inpath = '/Users/admin/Documents/extractEAD/in'
outpath = '/Users/admin/Documents/extractEAD/out'

for filename in os.listdir(inpath):
	if not filename.endswith('.xml'): continue
	fullname = os.path.join(inpath, filename)
	tree = etree.parse(fullname)
	root = tree.getroot()

	NS = "urn:schemas-microsoft-com:datatypes"
	header = ('Exposure', 'Latitude', 'Longitude', 'Altitude', 'Date', 'Time')
	
	with open('output.csv', 'w') as f:
		writer = csv.writer(f)
		writer.writerow(header)
		for exposure_number in root.iter('exposure_number'):
			exp = int(exposure_number.text)
			exposure_number.text = str(exp)
			# exposure_number = exposure_number.get('exposure_number')
		for latitude in root.iter('latitude'):
			latitude = latitude.get('latitude')
			
			row = exposure_number, latitude
			writer.writerow(row)


			# Write XML
			# outname = os.path.join(outpath, filename)
			# tree.write(outname,xml_declaration=True, encoding="utf-8",)
			
			
			



	# print(len(parser.error_log))