'''from selenium.webdriver.common.by import By


class Login_page:
    btn_login_xpath="//a[@title='Login' and @class='_1TOQfO']"
    text_login_page_title_xpath="//*[@class='mRoCtI col col-2-5 Wf_oWq MjqgSq']/span[@class='iq0fCx']"
    textbox_enter_email_xpath="//input[@class='c3Bd2c yXUQVt']"
    btn_request_otp_xpath="//button[text()='Request OTP']"  #//button[contains(text(),'Request OTP')]

    def __init__(self,driver):
        self.driver=driver

    def click_login_button(self,driver):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def enter_email_or_mobile(self,email_or_mobile):
        self.driver.find_element(By.XPATH,self.textbox_enter_email_xpath)
        self.driver.find_element(By.XPATH,self.textbox_enter_email_xpath).send_keys(email_or_mobile)

    def click_request_otp_button(self):
        self.driver.find_element(By.XPATH,self.btn_request_otp_xpath)'''
from selenium.webdriver.common.by import By


class Login_page:
    btn_email_xpath="//input[@placeholder='Username']"
    btn_pass_xpath="//input[@placeholder='Password']"
    btn_login_xpath="//button[@type='submit']"
    btn_logout_xpath="//a[text()='Logout']"
    btn_prof_xpath="//li[@class='oxd-userdropdown']"

    def __init__(self,driver):
        self.driver=driver

    def enter_email(self,username):
        #self.driver.find_element(By.XPATH, self.btn_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.btn_email_xpath).send_keys(username)

    def enter_pass(self, password):
        #self.driver.find_element(By.XPATH, self.btn_pass_xpath).clear()
        self.driver.find_element(By.XPATH, self.btn_pass_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def prof_click(self):
        self.driver.find_element(By.XPATH,self.btn_prof_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.btn_logout_xpath).click()


