import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Signup:

    # assertion elements
    sign_up_assertion = (By.XPATH,
     "//nav[@class='navbar navbar-expand-lg top-bar__header navbar-light bg-transparent position-sticky top-0 scrolledDown']")

    # Locators for driver signup
    btn_driver = (By.CSS_SELECTOR, ".btn.color-secondary-bg.px-4")
    btn_advertiser = (By.CSS_SELECTOR, ".btn.color-secondary-bg.px-4")
    business_contact_no = (By.CSS_SELECTOR, ".vti__input")
    btn_continue = (By.CSS_SELECTOR, ".btn.button-primary")
    name_field = (By.CSS_SELECTOR, ".form-control.bg-transparent")

    def __init__(self, driver):
        self.driver = driver

    def open_signup_url(self):
        self.driver.get("https://develop.somomarketingtech.com/select-platform")
        self.driver.maximize_window()

        # Assert that the title contains "Select Platform"
        assert "Select Platform" in self.driver.title, "Signup URL did not open successfully"

    def scroll_windows(self):
        self.driver.execute_script("window.scrollTo(0, 400)")

    def click_on_driver_button(self):
        # btn_driver = self.driver.find_element(By.CSS_SELECTOR, ".btn.color-secondary-bg.px-4")
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(self.btn_driver))

    def selectplatform_advertiser(self):
        self.scroll_windows()
        # btn_advertiser = self.driver.find_elements(By.CSS_SELECTOR, ".btn.color-secondary-bg.px-4")
        self.driver.find_elements(self.btn_advertiser[1]).click()
        assert "Sign up" in self.driver.find_element(self.sign_up_assertion), "Successfully found"

    def select_address(self):
        business_address = self.driver.find_element(By.ID, "map")
        business_address.send_keys("nj clark")
        suggestion_list = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "pac-container")))

        if len(suggestion_list) > 0:
            suggestion_list[0].click()  # Click on the first suggestion to select the address
        else:
            # If no suggestions are found, you may need to handle this scenario differently
            print("No suggestions found.")

    def enter_phone_number(self, value):
        phone_number = value
        # business_contact_no = self.driver.find_element(By.CSS_SELECTOR, ".vti__input")
        self.driver.find_element(self.business_contact_no).send_keys(phone_number)

    def enter_owner_address(self, value):
        address = value
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-control.bg-transparent.myclass-event.pac-target-input")))
        owner_address = self.driver.find_element(By.CSS_SELECTOR, ".form-control.bg-transparent.myclass-event.pac-target-input")
        owner_address.send_keys(address)

    def click_btn_continue(self, argument):
        argu = argument
        # btn_continue = self.driver.find_elements(By.CSS_SELECTOR, ".btn.button-primary")
        self.driver.find_elements(self.btn_continue[argu]).click()
        # check weather the continue button pressent or not

    def verify_success_message(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body.x-layout.swal2-toast-shown.swal2-shown:nth-child(2) > div.swal2-container.swal2-top-end.swal2-backdrop-show:nth-child(8)")))
        message= self.driver.find_element(By.CSS_SELECTOR, "body.x-layout.swal2-toast-shown.swal2-shown:nth-child(2) > div.swal2-container.swal2-top-end.swal2-backdrop-show:nth-child(8)").text
        print(message)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//wizard-button[contains(text(),'Next')]")))
        password_input = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Password"]').send_keys(password)

    def enter_confirm_password(self, password):
        confirm_password_input = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Confirm Password"]').send_keys(password)

    def signup_names(self, argument, value):
        field_text = value
        argu = argument
        # name_field = self.driver.find_elements(By.CSS_SELECTOR, ".form-control.bg-transparent")
        self.driver.find_elements(self.name_field[argu]).click()
        self.driver.find_elements(self.name_field[argu]).send_keys(field_text)

    def drp_regtype_click(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".form-select.bg-transparent"))).click()

    def drp_select_type(self):
        sel_regtype = Select(self.driver.find_element(By.CSS_SELECTOR, ".form-select.bg-transparent"))
        sel_regtype.select_by_index(1)

    def adv_dropdown(self, value):
        val = value
        drp_advertising = self.driver.find_elements(By.CSS_SELECTOR, ".form-select.bg-transparent")
        drp_advertising[val].click()
        selt_advertising = Select(self.driver.find_element(By.CSS_SELECTOR, ".form-select.bg-transparent"))
        selt_advertising.select_by_index(1)

    def adv_dropdown_platform(self):

        self.driver.find_element(By.XPATH, "//body/div[@id='main']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[6]/div[1]/select[1]").click()
        self.driver.find_element(By.XPATH, "//option[contains(text(),'Self')]").click()