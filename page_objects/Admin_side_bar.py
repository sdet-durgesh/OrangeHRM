
from selenium.webdriver.common.by import By


class admin_side_bar:
    btn_admin_xpath="//a[@class='oxd-main-menu-item active']"
    system_users_dropdown_xpath = "//*[@class='oxd-table-filter-header']"

    txt_uname_sys_users_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    txt_emp_name_sys_users_xpath = "//input[@placeholder='Type for hints...']"
    select_dropdown_user_role_xpath_1 = "//*[@class='oxd-select-text-input']"  # 2 select items located
    select_dropdown_user_role_xpath_2 = "//*[@class='oxd-select-text-input']"  # 2 select items located

    btn_reset_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--ghost']"
    btn_search_xpath = "//button[@type='submit']"
    btn_add_xpath = "//*[@class='oxd-button oxd-button--medium oxd-button--secondary']"

    records_found_xpath = "//span[@class='oxd-text oxd-text--span']"
    txt_Add_user_xpath = "//*[@class='oxd-text oxd-text--h6 orangehrm-main-title']"
    text_add_user_items_xpath = "//div[@class='oxd-grid-item oxd-grid-item--gutters']"  # 5 text fields located

    def __init__(self,driver):
        self.driver=driver

    def click_admin(self):
        self.driver.find_element(By.XPATH,self.btn_admin_xpath).click()

    def enter_uname(self, username):
        self.driver.find_element(By.XPATH, self.txt_uname_sys_users_xpath).send_keys(username)

    def click_search_btn(self):
        self.driver.find_element(By.XPATH,self.btn_search_xpath).click()

    def click_reset_btn(self):
        self.driver.find_element(By.XPATH, self.btn_reset_xpath).click()

    def click_add_btn(self):
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()