'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.Login_Page import Login_page

class Test_Login_Page:
    url="https://www.flipkart.com/"
    email_or_mobile="durgesh@gmail.com"

    def test_login_page_title(self):
        self.driver=webdriver.Chrome()
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='Login' and @class='_1TOQfO']"))
        )
        self.obj_lp=Login_page(self.driver)
        self.obj_lp.click_login_button(self.email_or_mobile)
        #self.obj_lp.click_request_otp_button()'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.read_properties import Read_Config
from page_objects.Login_Page import Login_page

class Test_Login_Page:
    url=Read_Config.get_admin_page_url()
    username=Read_Config.get_username()
    invalid_username=Read_Config.get_invalid_username()
    password=Read_Config.get_password()

    def test_01_login_page_title(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        obj_lp=Login_page(self.driver)
        obj_lp.enter_email(self.username)
        time.sleep(3)
        obj_lp.enter_pass(self.password)
        time.sleep(3)
        obj_lp.click_login()
        time.sleep(3)
        act_title=self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").text
        print("Actual title of the page is:" + act_title)
        if act_title=="Dashboard":
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\test_01_login_page_title.png")
            self.driver.close()
            assert False
        obj_lp.prof_click()
        obj_lp.click_logout()

    def test_02_invalid_login(self,setup):
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
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_02_invalid_login.png")
            self.driver.close()
            assert False

