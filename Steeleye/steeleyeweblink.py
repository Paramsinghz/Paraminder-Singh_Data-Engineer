import logging
import requests
import xml.etree.ElementTree as ET
import urllib

url = "https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100"
response = requests.get(url)

# Download the zip file from the link
# The first link would be Fetched

# create a logger
logger = logging.getLogger(__name__)

try:
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        download_link = root.find(".//str[@name='download_link']")
        if download_link is not None:
            url = download_link.text
            file_name = url.split("/")[-1]
            urllib.request.urlretrieve(url, file_name)
except Exception as e:
    logger.error(f"Error occurred: {e}", exc_info=True)
