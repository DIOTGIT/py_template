"""
Sajnát segítségre néhány gyakori import és eljárás
"""

__doc__ = """bla-bla"""

import sys
import os
import logging.config
from dotenv import load_dotenv, set_key, get_key

<<<<<<< HEAD
logging.config.fileConfig('.logging.conf')
l = logging.getLogger('root')
# l.debug(f'2+2 = {2+2}')

env_file = '.env'
load_dotenv(env_file)

logging.config.fileConfig('.logging.conf')
l = logging.getLogger('root')
# l.debug(f'2+2 = {2+2}')
# set_key(dotenv_path='.env', key_to_set="mlflow_runid", value_to_set="Johni")


env_file = '.env'
load_dotenv(env_file)
# get_key('.env','mlflow_runid')
# os.environ['mlflow_runid'] = 'sss'
# os.environ['mlflow_runid'] 
>>>>>>> b10e0e8a62685663d87ce4a13c91582a3bb9aa43

def genv(key):
    """bla"""
    _ = get_key(env_file, key)
    return os.environ[key]

def senv(key, value):
    """bla"""
    set_key(dotenv_path=env_file, key_to_set=key, value_to_set=value) #ez átírja a fájl
    os.environ[key] = value # ez meg a lokális tömböt

<<<<<<< HEAD
def logi(text):
    """bla"""
    s = sys._getframe(1).f_code.co_name # ki hívta az eljárást
    s = sys._getframe(1).f_code.co_qualname
=======
def logi(text=''):
    """bla"""
    s = sys._getframe(1).f_code.co_name # ki hívta az eljárást
    #s = sys._getframe(1).f_code.co_qualname
>>>>>>> b10e0e8a62685663d87ce4a13c91582a3bb9aa43
    l.info(s)


if __name__ == "__main__":
    l.info("ez modul, ne tuttasd direktben")