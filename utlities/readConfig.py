
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), "Configuration", "config.ini"))

class ReadConfig():
    @staticmethod  
      def getUserurl():  
          return config.get("login", "baseurl")

      @staticmethod  
      def getBrowser():
          return config.get("login", "browser")

      @staticmethod  
      def getUsername():
          return config.get("login", "username")

      @staticmethod  
      def getPassword():
          return config.get("login", "password")
