import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.join(os.path.dirname(__file__),"../Configuration/config.ini"))
 
class ReadConfig:
    
    @staticmethod
    def getBaseUrl():
        return config.get("login", "baseUrl")

    @staticmethod
    def getBrowser():
        return config.get("login", "browser")

    @staticmethod
    def getUsername():
        return config.get("login", "username")

    @staticmethod
    def getPassword():
        return config.get("login", "password")
