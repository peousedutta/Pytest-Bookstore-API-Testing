from configparser import ConfigParser

config = ConfigParser()

config.read("../configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        return config.get('info','baseurl')