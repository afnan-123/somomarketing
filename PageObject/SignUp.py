import time

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
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)


class SignUp:

    def open_signup_url(self):
        driver.get("https://develop.somomarketingtech.com/select-platform")
        driver.maximize_window()

    def scroll_windows(self):
        driver.execute_script("window.scrollTo(0, 400)")

    def selectplatform_driver(self):
        btn_driver = driver.find_element(By.CSS_SELECTOR, ".btn.color-secondary-bg.px-4")
        driver.execute_script("arguments[0].click();", btn_driver)

    def selectplatform_advertiser(self):
        SignUp.scroll_windows(self)
        btn_advertiser = driver.find_elements(By.CSS_SELECTOR, ".btn.color-secondary-bg.px-4")
        btn_advertiser[1].click()

    def select_address(self):
        business_address = driver.find_element(By.ID, "map")
        business_address.send_keys("nj clark")
        suggestion_list = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "pac-container")))

        if len(suggestion_list) > 0:
            suggestion_list[0].click()  # Click on the first suggestion to select the address
        else:
            # If no suggestions are found, you may need to handle this scenario differently
            print("No suggestions found.")

    def phonenumber(self, value):
        phone_number = value
        business_contact_no = driver.find_element(By.CSS_SELECTOR, ".vti__input")
        business_contact_no.send_keys(phone_number)

    def btn_continue(self, argument):
        argu = argument
        btn_continue = driver.find_elements(By.CSS_SELECTOR, ".btn.button-primary")
        btn_continue[argu].click()

    def signup_names(self, argument, value):
        field_text = value
        argu = argument
        name_field = driver.find_elements(By.CSS_SELECTOR, ".form-control.bg-transparent")
        name_field[argu].send_keys(field_text)

    def drp_regtype_click(self):
        drp_type = driver.find_element(By.CSS_SELECTOR, ".form-select.bg-transparent")
        drp_type.click()

    def drp_select_type(self):
        sel_regtype = Select(driver.find_element(By.CSS_SELECTOR, ".form-select.bg-transparent"))
        sel_regtype.select_by_index(1)

    def adv_dropdown(self, value):
        val = value
        drp_advertising = driver.find_elements(By.CSS_SELECTOR, ".form-select.bg-transparent")
        drp_advertising[val].click()
        selt_advertising = Select(driver.find_element(By.CSS_SELECTOR, ".form-select.bg-transparent"))
        selt_advertising.select_by_index(1)

    def adv_dropdown_platform(self):
        drp_platform = driver.find_element(By.XPATH,
                                           "//div[@class='col-md-3']//select[@aria-label='Default select example']")
        drp_platform.click()

        time.sleep(1)
        selt_platform = Select(
            driver.find_element(By.XPATH, "//div[@class='col-md-3']//select[@aria-label='Default select example']"))
        selt_platform.select_by_index(1)

    def signup_driver(self):

        SignUp.drp_regtype_click(self)
        SignUp.drp_select_type(self)
        SignUp.signup_names(self, 0, "Mark Trucks")
        SignUp.signup_names(self, 1, "234534532")
        SignUp.signup_names(self, 2, "marktrucks@yomail.com")
        SignUp.phonenumber(self, "+1 234 454 3423")
        SignUp.scroll_windows(self)
        SignUp.select_address(self)
        SignUp.btn_continue(self, 0)
        SignUp.signup_names(self, 0, "mark")
        SignUp.signup_names(self, 1, "mark@yopmail.com")
        SignUp.phonenumber(self, "+1 234 454 3426")

        owner_address = driver.find_element(By.CSS_SELECTOR,
                                            ".form-control.bg-transparent.myclass-event.pac-target-input")
        owner_address.send_keys("nj clark")
        SignUp.signup_names(self, 2, "New York")
        SignUp.signup_names(self, 3, "America")
        SignUp.signup_names(self, 4, "New York")
        SignUp.signup_names(self, 5, "10001")
        SignUp.btn_continue(self, 1)
        SignUp.signup_names(self, 0, "12345")
        SignUp.signup_names(self, 1, "12345")
        time.sleep(5)
    def SignUp_advertiser(self):
        SignUp.open_signup_url(self)
        driver.implicitly_wait(4)
        SignUp.selectplatform_advertiser(self)
        SignUp.signup_names(self, 0, "Elon")
        SignUp.signup_names(self, 1, "Mash")
        SignUp.signup_names(self, 2, "Elon@yopmail.com")
        SignUp.signup_names(self, 3, "X")
        SignUp.signup_names(self, 4, "CEO")
        SignUp.adv_dropdown(self, 0)
        driver.implicitly_wait(3)
        SignUp.adv_dropdown_platform(self)
        SignUp.scroll_windows(self)
        SignUp.select_address(self)
        SignUp.btn_continue(self, 0)
        time.sleep(3)
        SignUp.signup_names(self, 0, "12345")
        SignUp.signup_names(self, 1, "12345")
        time.sleep(3)


open_signup = SignUp()
open_signup.SignUp_advertiser()

