import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.custom_logger import Log_Maker
from utilities.read_properties import Read_Config
from page_objects.LHS_Slider_Bar import Side_page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_LHS_Slider_Bar:
    url =               Read_Config.get_admin_page_url()
    username =          Read_Config.get_username()
    invalid_username =  Read_Config.get_invalid_username()
    password =          Read_Config.get_password()
    logger =            Log_Maker.loggen()

    def test_03_side_bar(self, setup):
        self.logger.info("*** test_03_side_bar ****")
        self.logger.info("**** Side Bar test Start ****")
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.obj_side_page=Side_page(self.driver)
        self.obj_side_page.enter_email(self.username)
        time.sleep(3)
        self.obj_side_page.enter_pass(self.password)
        time.sleep(3)
        self.obj_side_page.click_login()
        time.sleep(3)
        result_list=self.driver.find_elements(By.XPATH,"//li[@class='oxd-main-menu-item-wrapper']")
        count=len(result_list)
        print("Total Count of side bar items are  :", count)
        for list_items in result_list:
            print("List of all side items are  :", list_items.text)
        self.obj_side_page.click_prof()
        self.obj_side_page.click_logout()
        self.logger.info("**** Side Bar test Ends ****")
        self.logger.info("**** test_03_side_bar Passed ****")
        self.driver.close()

    def test_04_side_bar_admin(self, setup):
        self.logger.info("*** test_04_side_bar_admin ***")
        self.logger.info("**** Side Bar Admin test Start ****")
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.obj_side_page=Side_page(self.driver)
        self.obj_side_page.enter_email(self.username)
        time.sleep(2)
        self.obj_side_page.enter_pass(self.password)
        time.sleep(2)
        self.obj_side_page.click_login()
        time.sleep(2)
        self.obj_side_page.click_search()
        search_element = self.driver.find_element(By.XPATH,"//input[@placeholder='Search']")
        assert search_element.is_enabled()
        print("Search field is Enabled")
        self.obj_side_page.click_search()
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("ADMIN")
        self.driver.find_element(By.XPATH,"//span[text()='Admin']").click()
        wait=WebDriverWait(self.driver,10)
        page_title=wait.until(EC.visibility_of_element_located((By.XPATH,"//h6[normalize-space()='Admin']")))
        admin_page_title = page_title.text
        print("Admin Page title is:" + admin_page_title)
        if admin_page_title == "Admin":
            assert True
            self.logger.info("**** Admin Page title Matched ****")
        else:
            self.driver.save_screenshot(".\\screenshots\\test_04_side_bar_Admin Page title NOT Matched.png")
            self.driver.close()
            assert False
        time.sleep(3)
        self.obj_side_page.click_prof()
        self.obj_side_page.click_logout()
        self.logger.info("**** Side Bar Admin test Ends ****")
        self.logger.info("**** test_04_side_bar_admin Passed ****")
        self.driver.close()
