
from selenium.webdriver.common.by import By


class Side_page:
    btn_email_xpath="//input[@placeholder='Username']"
    btn_pass_xpath="//input[@placeholder='Password']"
    btn_login_xpath="//button[@type='submit']"
    btn_logout_xpath="//a[text()='Logout']"
    btn_prof_xpath="//li[@class='oxd-userdropdown']"

    side_arrow="//button[@class='oxd-icon-button oxd-main-menu-button']"
    search_bar="//input[@placeholder='Search']"
    side_menu_items="//ul[@class='oxd-main-menu']"

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

    def side_arrow_click(self):
        self.driver.find_element(By.XPATH,self.side_arrow).click()

    def search_click(self):
        self.driver.find_element(By.XPATH,self.search_bar).click()

    def side_menu(self):
        self.driver.find_element(By.XPATH,self.side_menu_items)

    def prof_click(self):
        self.driver.find_element(By.XPATH,self.btn_prof_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH,self.btn_logout_xpath).click()


