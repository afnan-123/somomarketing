import time
import pytest as pytest
from PageObject.SignUp import Signup
from Config.Config import SignUp_data
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class TestSignup:

    config = SignUp_data()
    # advertiser vaiables
    adv_firstname = config.adv_firstname
    adv_lastname = config.adv_lastname
    adv_emailaddress = config.adv_emailaddress
    adv_business = config.adv_business
    adv_phonenumber = config.adv_phonenumber
    adv_title = config.adv_title
    adv_address = config.adv_address
    adv_password = config.adv_password
    adv_confirmpassword = config.adv_confirmpassword
    # driver variables
    driver_regtype = config.driver_regtype
    driver_Name = config.driver_Name
    driver_ein = config.driver_ein
    driver_emailaddress = config.driver_emailaddress
    driver_contact = config.driver_contact
    driver_firstaddress = config.driver_firstaddress
    driver_ownername = config.driver_ownername
    driver_owneremail = config.driver_owneremail
    driver_ownercontact = config.driver_ownercontact
    driver_owneraddress = config.driver_owneraddress
    driver_ownercity = config.driver_ownercity
    driver_onwercountry = config.driver_onwercountry
    driver_ownerstate = config.driver_ownerstate
    driver_ownerzipcode = config.driver_ownerzipcode

    @pytest.fixture(scope="function")
    def setup(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
        yield
        self.driver.quit()



    def test_signup_driver(self, setup):

        print("Test case started successfully")
        self.sp = Signup(self.driver)
        self.sp.open_signup_url()
        self.sp.click_on_driver_button()
        self.sp.drp_regtype_click()
        self.sp.drp_select_type()
        self.sp.signup_names(0, self.driver_Name)
        self.sp.signup_names(1, self.driver_ein)
        self.sp.signup_names(2, self.driver_emailaddress)
        self.sp.enter_phone_number(self.driver_contact)
        self.sp.scroll_windows()
        self.sp.select_address()
        self.sp.click_btn_continue(0)
        self.sp.signup_names(0, self.driver_ownername)
        self.sp.signup_names(1, self.driver_owneremail)
        self.sp.enter_phone_number(self.driver_ownercontact)
        self.sp.enter_owner_address(self.driver_owneraddress)

        self.sp.signup_names(2, self.driver_ownercity)
        self.sp.signup_names(3, self.driver_onwercountry)
        self.sp.signup_names(4, self.driver_ownerstate)
        self.sp.signup_names(5, self.driver_ownerzipcode)
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
        self.sp.signup_names(1, self.adv_lastname)
        self.sp.signup_names(2, self.adv_emailaddress)
        self.sp.signup_names(3, self.adv_business)
        self.sp.signup_names(4, self.adv_title)
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
