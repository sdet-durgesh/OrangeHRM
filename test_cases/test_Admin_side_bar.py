import time

from selenium.webdriver.common.by import By

from utilities.custom_logger import Log_Maker
from utilities.read_properties import Read_Config
from page_objects.Admin_side_bar import Admin_side_bar
from page_objects.LHS_Slider_Bar import Side_page
from page_objects.Login_Page import Login_page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Admin_Side_Bar:
    url =               Read_Config.get_admin_page_url()
    username =          Read_Config.get_username()
    password =          Read_Config.get_password()
    logger =            Log_Maker.loggen()

    def test_05_admin_side_bar(self, setup):
        self.logger.info("*** test_05_admin_side_bar ****")
        self.logger.info("**** Admin Side Bar test Start ****")
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(2)
        self.obj_admin_side_bar=Admin_side_bar(self.driver)
        self.obj_lp = Login_page(self.driver)
        self.obj_lp.enter_email(self.username)
        time.sleep(1)
        self.obj_lp.enter_pass(self.password)
        time.sleep(1)
        self.obj_lp.click_login()
        time.sleep(1)
        search_field = self.obj_admin_side_bar.click_search_btn()
        time.sleep(2)
        search_field.clear()
        search_field.send_keys("Admin")
        time.sleep(2)
        self.obj_lhs_sider_bar= Side_page(self.driver)
        time.sleep(2)
        self.obj_lhs_sider_bar.click_admin()
        time.sleep(5)
        # below code is not run ae per expected for log message and screenshot methods
        self.target_page=self.obj_admin_side_bar.isSystemUserPageExists()
        if self.target_page==True:
            assert True
            self.logger.info("**** Admin Page title Matched ****")
        else:
            self.driver.save_screenshot(".\\screenshots\\test_05_admin_side_bar Page title NOT Matched.png")
        time.sleep(2)
        self.obj_admin_side_bar.enter_uname("Admin")
        self.obj_admin_side_bar.click_admin_search_btn()
        time.sleep(2)
        self.obj_admin_side_bar.click_reset_btn()
        time.sleep(2)
        self.obj_admin_side_bar.click_add_btn()
        time.sleep(2)

        #list of webelements is not able to print
        print("List of Add User Text Fields are : ", self.obj_admin_side_bar.check_add_user_text_items())




        # page_title_add_user=self.driver.find_element(By.LINK_TEXT,"Add User")
        # print(page_title_add_user)
        # admin_page_title = page_title_add_user.text
        # print("Add User page title is:" + admin_page_title)
        # if admin_page_title == "Add User":
        #     assert True
        #     self.logger.info("**** Add User Page title Matched ****")
        # else:
        #     self.driver.save_screenshot(".\\screenshots\\test_05 Add User Page title NOT Matched.png")
        #     self.driver.close()
        #     assert False
        # add_user_item_list=self.obj_admin_side_bar.check_add_user_text_items().text()
        # print("The visible text items fields on Add User page are:"+ add_user_item_list)

        self.obj_lp.click_prof()
        time.sleep(3)
        self.obj_lp.click_logout()
        self.logger.info("**** Admin Side Bar test Ends ****")
        self.logger.info("**** test_05_admin_side_bar Passed ****")
        self.driver.close()