import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.join(os.path.dirname(__file__),"../Configuration/config.ini"))

class ReadConfig:

    # ── LOGIN ──────────────────────────────
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

    # ── REGISTER ───────────────────────────
    @staticmethod
    def getRegisterUrl():
        return config.get("register", "url")

    @staticmethod
    def getFirstname():
        return config.get("register", "firstname")

    @staticmethod
    def getLastname():
        return config.get("register", "lastname")

    @staticmethod
    def getAddress():
        return config.get("register", "address")

    @staticmethod
    def getCity():
        return config.get("register", "city")

    @staticmethod
    def getState():
        return config.get("register", "state")

    @staticmethod
    def getZipcode():
        return config.get("register", "zipcode")

    @staticmethod
    def getPhone():
        return config.get("register", "phone")

    @staticmethod
    def getSSN():
        return config.get("register", "ssn")

    @staticmethod
    def getRegisterUsername():
        return config.get("register", "username")

    @staticmethod
    def getRegisterPassword():
        return config.get("register", "password")
