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


