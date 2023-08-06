import time
from PageObject import SignUp
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

serv = Service("C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver")
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


class test_signup:

    def test_signup_driver(self):

        SignUp.open_signup.open_signup_url()
        SignUp.open_signup.selectplatform_driver()
        SignUp.open_signup.drp_regtype_click(self)
        SignUp.open_signup.drp_select_type(self)
        SignUp.open_signup.signup_names(self, 0, "Mark Trucks")
        SignUp.open_signup.signup_names(self, 1, "234534532")
        SignUp.open_signup.signup_names(self, 2, "marktrucks@yomail.com")
        SignUp.open_signup.phonenumber(self, "+1 234 454 3423")
        SignUp.open_signup.scroll_windows(self)
        SignUp.open_signup.select_address(self)
        SignUp.open_signup.btn_continue(self, 0)
        SignUp.open_signup.signup_names(self, 0, "mark")
        SignUp.open_signup.signup_names(self, 1, "mark@yopmail.com")
        SignUp.open_signup.phonenumber(self, "+1 234 454 3426")

        owner_address = driver.find_element(By.CSS_SELECTOR,
                                            ".form-control.bg-transparent.myclass-event.pac-target-input")
        owner_address.send_keys("nj clark")
        SignUp.open_signup.signup_names(self, 2, "New York")
        SignUp.open_signup.signup_names(self, 3, "America")
        SignUp.open_signup.signup_names(self, 4, "New York")
        SignUp.open_signup.signup_names(self, 5, "10001")
        SignUp.open_signup.btn_continue(self, 1)
        SignUp.open_signup.signup_names(self, 0, "12345")
        SignUp.open_signup.signup_names(self, 1, "12345")
        time.sleep(5)
        print("Success")
        print("Test case started successfully")
        driver.close()

    def test_signup_advertiser(self):

        SignUp.open_signup.open_signup_url()
        SignUp.open_signup.selectplatform_advertiser()
        SignUp.open_signup.signup_names(self, 0, "Elon")
        SignUp.open_signup.signup_names(self, 1, "Mash")
        SignUp.open_signup.signup_names(self, 2, "Elon@yopmail.com")
        SignUp.open_signup.signup_names(self, 3, "X")
        SignUp.open_signup.signup_names(self, 4, "CEO")
        driver.implicitly_wait(3)
        SignUp.open_signup.adv_dropdown_platform(self)
        SignUp.open_signup.scroll_windows(self)
        SignUp.open_signup.select_address(self)
        SignUp.open_signup.btn_continue(self, 0)
        driver.implicitly_wait(3)
        SignUp.open_signup.signup_names(self, 0, "12345")
        SignUp.open_signup.signup_names(self, 1, "12345")
        time.sleep(3)

        print("success")


openurl = test_signup()

openurl.test_signup_driver()
# openurl.test_signup_advertiser()
