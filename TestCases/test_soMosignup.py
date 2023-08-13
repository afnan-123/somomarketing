import time
import pytest as pytest
from PageObject.SignUp import Signup
from Config.Config import SignUp_data
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class TestSignup:
    config = SignUp_data()
    adv_firstname = config.adv_firstname
    @pytest.fixture(scope="function")
    def setup(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()



    def test_signup_driver(self, setup):

        print("Test case started successfully")
        self.sp= Signup(self.driver)
        self.sp.open_signup_url()
        self.sp.click_on_driver_button()
        self.sp.drp_regtype_click()
        self.sp.drp_select_type()
        self.sp.signup_names(0, "Mark Trucks")
        self.sp.signup_names(1, "234534532")
        self.sp.signup_names(2, "marktrucks@yomail.com")
        self.sp.enter_phone_number("+1 234 454 3423")
        self.sp.scroll_windows()
        self.sp.select_address()
        self.sp.click_btn_continue(0)
        self.sp.signup_names(0, "mark")
        self.sp.signup_names(1, "mark@yopmail.com")
        self.sp.enter_phone_number("+1 234 454 3426")
        self.sp.enter_owner_address("nj clark")

        self.sp.signup_names(2, "New York")
        self.sp.signup_names(3, "America")
        self.sp.signup_names(4, "New York")
        self.sp.signup_names(5, "10001")
        self.sp.click_btn_continue(1)
        self.sp.signup_names(0, "12345")
        self.sp.signup_names(1, "12345")
        self.sp.click_btn_continue(1)
        self.sp.verify_success_message()
        time.sleep(5)
        print("Test case completed successfully")

    def test_signup_advertiser(self, setup):

        print("Test case started successfully")
        self.sp= Signup(self.driver)
        self.sp.open_signup_url()
        self.sp.selectplatform_advertiser()
        self.sp.signup_names(0, self.adv_firstname)
        self.sp.signup_names(1, "Mash")
        self.sp.signup_names(2, "Elon1@yopmail.com")
        self.sp.signup_names(3, "XX")
        self.sp.signup_names(4, "CEO")
        self.sp.adv_dropdown_platform()
        self.sp.scroll_windows()
        self.sp.select_address()
        self.sp.click_btn_continue(0)
        self.sp.enter_password("12345")
        self.sp.enter_confirm_password("12345")
        self.sp.click_btn_continue(1)
        self.sp.click_btn_continue(0)
        self.sp.verify_success_message()
        time.sleep(5)
        print("Test case completed successfully")

if __name__ == "__main__":
    pytest.main()
# openurl.test_signup_advertiser()
