import configparser

config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config:
    @staticmethod
    def get_admin_page_url():
        url=config.read('admin login info','url')
        return url
    @staticmethod
    def get_username():
        username=config.read('admin login info','username')
        return username
    @staticmethod
    def get_password():
        password=config.read('admin login info','password')
        return password
    @staticmethod
    def get_invalid_username():
        invalid_username=config.read('admin login info','invalid_username')
        return invalid_username

