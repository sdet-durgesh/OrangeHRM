
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Admin_side_bar:
    btn_admin_xpath="//a[@class='oxd-main-menu-item active']"
    system_users_dropdown_xpath = "//*[@class='oxd-table-filter-header']"

    txt_username_sys_users_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']"
    txt_emp_name_sys_users_xpath = "//input[@placeholder='Type for hints...']"
    select_dropdown_user_role_xpath_1 = "//*[@class='oxd-select-text-input']"  # 2 select items located
    select_dropdown_user_role_xpath_2 = "//*[@class='oxd-select-text-input']"  # 2 select items located

    btn_reset_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--ghost']"
    btn_search_xpath="//input[@placeholder='Search']"
    btn_search_admin_page_xpath="//*[@type='submit']"
    btn_add_xpath = "//*[@class='oxd-button oxd-button--medium oxd-button--secondary']"

    msg_system_users="System Users"
    records_found_xpath = "//span[@class='oxd-text oxd-text--span']"
    text_add_user_items_xpath = "//div[@class='oxd-grid-item oxd-grid-item--gutters']"  # 5 text fields located

    #admin page headers
    user_management_dropdown = "//span[contains(text(),'User Management')]"
    user_management_dropdown_items ="//ul[@role='menu']/li"
    job_dropdown = "//span[contains(text(),'Job')]"
    job_dropdown_items="//ul[@class='oxd-dropdown-menu']//li" #//ul[@role='menu']/li"
    organization_dropdown = "//span[contains(text(),'Organization')]"
    organization_dropdown_items = "//ul[@role='menu']/li"
    qualification_dropdown = "//a[contains(text(),'Qualification')]"
    qualification_dropdown_items = "//ul[@role='menu']/li"
    nationalities_dropdown = "//a[contains(text(),'Nationalities')]"
    corporate_branding_dropdown = "//a[contains(text(),'Corporate')]"
    configuration_dropdown = "//a[contains(text(),'Configuration')]"
    configuration_dropdown_items = "//ul[@role='menu']/li"




    def __init__(self,driver):
        self.driver=driver
        # Locator for the 'Job' span/button that opens the dropdown
        self.user_button_locator = (By.XPATH, self.job_dropdown)
        self.items_user_button_locator = (By.XPATH, self.job_dropdown_items)

    def click_admin(self):
        self.driver.find_element(By.XPATH,self.btn_admin_xpath).click()

    def enter_uname(self, username):
        self.driver.find_element(By.XPATH, self.txt_username_sys_users_xpath).send_keys(username)

    def click_search_btn(self):
        wait=WebDriverWait(self.driver,10)
        element=wait.until(EC.element_to_be_clickable((By.XPATH,self.btn_search_xpath)))
        element.click()
        element.send_keys()
        return element

    def isSystemUserPageExists(self):
        try:
            self.driver.find_element(By.XPATH,self.msg_system_users).is_displayed()
        except:
            return False

    def click_admin_search_btn(self):
        self.driver.find_element(By.XPATH,self.btn_search_admin_page_xpath).click()

    def check_records_admin_after_search(self):
        self.driver.find_element(By.XPATH, self.records_found_xpath)

    def click_reset_btn(self):
        self.driver.find_element(By.XPATH, self.btn_reset_xpath).click()

    def click_add_btn(self):
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()

    def check_add_user_text_items(self):
        list_add_user_text_field=self.driver.find_elements(By.XPATH, self.text_add_user_items_xpath)
        return list_add_user_text_field

    def dropdown_items_user_management(self):
        # Click the 'Job' button to make the options appear
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.user_button_locator)).click()

        # Wait for the list items to be visible
        job_items = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.items_user_button_locator)
        )

        # Extract and return the text for each element
        return job_items