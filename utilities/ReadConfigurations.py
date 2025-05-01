from configparser import ConfigParser

config = ConfigParser()

config.read("../configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        try:
            print("[DEBUG] -- URL --", config.get('info','baseurl'))
            return config.get('info','baseurl')
        except Exception as err:
            raise Exception(f"[ERROR] Exception occured while fetch base url got --> {err}")