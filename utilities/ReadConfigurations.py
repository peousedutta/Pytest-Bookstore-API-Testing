import os
import httpx
from configparser import ConfigParser


config = ConfigParser()

# Get the absolute path of the config file
config_path = os.path.join(os.path.dirname(__file__), "../configurations/config.ini")
config.read(config_path)

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        try:
            print("[DEBUG] -- URL --", config.get('info','baseurl'))
            return config.get('info','baseurl')
        except Exception as err:
            raise Exception(f"[ERROR] Exception occured while fetch base url got --> {err}")
    @staticmethod
    def getSlackWebHook():
        try:
            return config.get('info','slackwebhook')
        except Exception as err:
            raise Exception(f"[ERROR] Exception occured while fetch slack web hook --> {err}")