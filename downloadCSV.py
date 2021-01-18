import urllib.request
import logging

format_string = '%(levelname)s: %(asctime)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, filename="log.log", format=format_string)

logging.debug("Beginning file download OntarioCovidData.csv\n")

url = 'https://data.ontario.ca/dataset/.........csv'
urllib.request.urlretrieve(url, '/Users/Katya/Downloads/data.csv')

logging.debug("Success! File download complete for OntarioCovidData.csv \n")




