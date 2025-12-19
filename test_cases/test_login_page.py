import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.read_properties import Read_Config
from page_objects.Login_Page import Login_page
from test_cases import conftest
from utilities.custom_logger import Log_Maker

class Test_Login_Page:
    url=                Read_Config.get_admin_page_url()
    username=           Read_Config.get_username()
    invalid_username=   Read_Config.get_invalid_username()
    password=           Read_Config.get_password()
    logger =            Log_Maker.loggen()

    def test_01_Home_page_title(self,setup):
        self.logger.info("*************** test_01_Home_page_title *****************")
        self.logger.info("**** Home page title test Start ****")
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        self.obj_lp=Login_page(self.driver)
        self.obj_lp.enter_email(self.username)
        time.sleep(3)
        self.obj_lp.enter_pass(self.password)
        time.sleep(3)
        self.obj_lp.click_login()
        time.sleep(3)
        act_title=self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").text
        print("Actual title of the home page is:" + act_title)
        if act_title=="Dashboard":
            assert True
            self.logger.info("**** Home page title Matched ****")
        else:
            self.driver.save_screenshot(".\\screenshots\\test_01_login_page_title.png")
            self.driver.close()
            assert False
        self.obj_lp.prof_click()
        self.obj_lp.click_logout()
        self.logger.info("**** Home page title test Ends ****")
        self.logger.info("**** test_01_Home_page_title Passed ****")
        self.driver.close()

    def test_02_invalid_login(self,setup):
        self.logger.info("*************** test_02_invalid_login *****************")
        self.logger.info("**** Invalid Login test Start ****")
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        obj_lp=Login_page(self.driver)
        obj_lp.enter_email(self.invalid_username)
        time.sleep(3)
        obj_lp.enter_pass(self.password)
        time.sleep(3)
        obj_lp.click_login()
        time.sleep(3)
        login_error=self.driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text
        print("Error on the page is:  " + login_error)
        if login_error=="Invalid credentials":
            assert True
            self.logger.info("**** Invalid Login ERROR matched****")
            self.logger.info("**** Invalid Login test Ends ****")
            self.logger.info("**** test_02_invalid_login Passed ****")
        else:
            self.driver.save_screenshot(".\\screenshots\\test_02_invalid_login.png")
            self.driver.close()
            assert False
        self.logger.info("**** test_02_invalid_login Failed ****")
        self.driver.close()

