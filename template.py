import logging.config
logging.config.fileConfig('.logging.conf')
logger = logging.getLogger('root')
# logger.debug(f'2+2 = {2+2}')

import os
from dotenv import load_dotenv, set_key, get_key
load_dotenv('.env')

# set_key(dotenv_path='.env', key_to_set="mlflow_runid", value_to_set="Johni")
# get_key('.env','mlflow_runid')
# os.environ['mlflow_runid'] = 'sss'
# os.environ['mlflow_runid'] 