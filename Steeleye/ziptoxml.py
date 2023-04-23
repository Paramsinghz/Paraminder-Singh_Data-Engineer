import logging
import zipfile

# specify the name of the ZIP archive file
zip_filename = 'DLTINS_20210117_01of01.zip'

# specify the name of the XML file you want to extract
xml_filename = 'DLTINS_20210117_01of01.xml'

# create a logger
logger = logging.getLogger(__name__)

try:
    # open the ZIP archive file for reading
    with zipfile.ZipFile(zip_filename, 'r') as zip_file:
        # check if the specified XML file exists in the archive
        if xml_filename in zip_file.namelist():
            # extract the XML file to the current directory
            zip_file.extract(xml_filename)
        else:
            logger.warning(f"{xml_filename} not found in {zip_filename}")
except Exception as e:
    logger.error(f"Error occurred: {e}", exc_info=True)
