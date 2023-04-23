import csv
import xml.etree.ElementTree as ET
import logging

# Configure logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)

try:
    # Parse the XML file
    tree = ET.parse('DLTINS_20210117_01of01.xml')
    root = tree.getroot()

    # Extract data from <FinInstrm> elements
    data = []
    header = ['Id', 'FullNm', 'ClssfctnTp', 'CmmdtyDerivInd', 'NtnlCcy', 'Issr']
    data.append(header)

    for fininstrm in root.findall('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}FinInstrm'):
        record = []
        fininstrm_gnl_attrbts = fininstrm.find('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}FinInstrmGnlAttrbts')
        record.append(fininstrm_gnl_attrbts.findtext('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}Id'))
        record.append(fininstrm_gnl_attrbts.findtext('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}FullNm'))
        record.append(fininstrm_gnl_attrbts.findtext('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}ClssfctnTp'))
        record.append(fininstrm_gnl_attrbts.findtext('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}CmmdtyDerivInd'))
        record.append(fininstrm_gnl_attrbts.findtext('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}NtnlCcy'))
        termn = fininstrm.find('.//{urn:iso:std:iso:20022:tech:xsd:auth.036.001.02}Issr')
        record.append(termn.text if termn is not None else '')
        data.append(record)

    # Create and write data to CSV file
    with open('example.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
except Exception as e:
    logging.exception("An error occurred: %s", e)
