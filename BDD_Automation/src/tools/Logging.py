import logging
import os
file= os.path.join(os.path.abspath(__file__),'example.log')

logging.basicConfig(filename='tools\example.log', filemode='w+',encoding='utf-8', level=logging.INFO)
logging.info('ini adalah logging info')