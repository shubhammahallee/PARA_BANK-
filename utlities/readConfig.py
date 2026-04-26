
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), "Configuration", "config.ini"))

class ReadConfig():
    @staticmethod  # ERROR: Wrong indentation
      def getUserurl():  # ERROR: Should be getBaseurl
          return config.get("login", "baseurl")

      @staticmethod  # ERROR: Wrong indentation
      def getBrowser():
          return config.get("login", "browser")

      @staticmethod  # ERROR: Wrong indentation
      def getUsername():
          return config.get("login", "username")

      @staticmethod  # ERROR: Wrong indentation
      def getPassword():
          return config.get("login", "password")
