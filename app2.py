import requests
import logging
logging.basicConfig(level=logging.DEBUG)
r = requests.get('http://httpbin.org')

