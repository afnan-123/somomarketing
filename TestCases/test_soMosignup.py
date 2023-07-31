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


class test_signup:

    def __init__(self, driver):
        self.driver = driver

    def test_signup_driver(self):

        serv = Service("C:\\Drivers\\chromedriver_win32")
        driver = webdriver.Chrome()
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # Open the website and maximize the window
        driver.get("https://develop.somomarketingtech.com/select-platform")
        driver.maximize_window()
        btn_driver = driver.find_element(By.CSS_SELECTOR, ".btn.color-secondary-bg.px-4")
        driver.execute_script("arguments[0].click();", btn_driver)
        drp_type = driver.find_element(By.CSS_SELECTOR, ".form-select.bg-transparent")
        drp_type.click()
        sel_regtype = Select(driver.find_element(By.CSS_SELECTOR, ".form-select.bg-transparent"))
        sel_regtype.select_by_index(1)
        business_name = driver.find_element(By.XPATH, "//div[@class='row']//div[5]//input[1]")
        business_name.send_keys("Jonas Trucking")
        EIN = driver.find_element(By.XPATH, "//input[@placeholder='XX-XXXXXXX']")
        EIN.send_keys("123213456")
        business_email = driver.find_element(By.XPATH, "//input[@type='email']")
        business_email.send_keys("Jonastruckingg@gmail.com")
        business_contact_no = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter a phone number']")
        business_contact_no.send_keys("+1 2342 2343 3242")
        business_address = driver.find_element(By.CSS_SELECTOR, ".form-control.bg-transparent.myclass-event.pac-target-input")
        business_address.send_keys("nj clark")
        time.sleep(4)
        wait = WebDriverWait(driver, 10)
        suggestion_list = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "pac-container")))

        if len(suggestion_list) > 0:
            suggestion_list[0].click()  # Click on the first suggestion to select the address
        else:
            # If no suggestions are found, you may need to handle this scenario differently
            print("No suggestions found.")
        time.sleep(2)
        bwait = WebDriverWait(driver, 10)
        btn_continue = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.color-secondary-bg")))
        driver.execute_script("arguments[0].click();", btn_continue)
        time.sleep(5)
        owner_name = driver.find_elements(By.CSS_SELECTOR, ".form-control.bg-transparent")
        owner_name[0].send_keys("Jonas")
        owner_email = driver.find_elements(By.CSS_SELECTOR, ".form-control.bg-transparent")
        owner_email[1].send_keys("jonastruckingg@yopmail.com")
        owner_contact = driver.find_element(By.CSS_SELECTOR, ".vti__input")
        owner_contact.send_keys("+1 2334 3242 2345")
        owner_address = driver.find_element(By.CSS_SELECTOR, ".form-control.bg-transparent.myclass-event.pac-target-input")
        owner_address.send_keys("nj clark")
        time.sleep(2)
        owner_city = driver.find_element(By.XPATH, "//input[@id='city_id']")
        owner_city.send_keys("New York")
        owner_country = driver.find_element(By.XPATH, "//input[@id='country_id']")
        owner_country.send_keys("America")
        owner_state = driver.find_element(By.XPATH, "//input[@id='state_id']")
        owner_state.send_keys("NY")
        owner_zipcode = driver.find_element(By.XPATH, "//div[@class='row gy-3 mt-0']//div[2]//div[1]//input[1]")
        owner_zipcode.send_keys("10001")
        adwait = WebDriverWait(driver, 10)
        btn2_continue = adwait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue']")))
        driver.execute_script("arguments[0].click();", btn2_continue)
        password = driver.find_elements(By.CSS_SELECTOR, ".form-control.bg-transparent")
        password[0].send_keys("12345")
        confirm_password = driver.find_elements(By.CSS_SELECTOR, ".form-control.bg-transparent")
        confirm_password[1].send_keys("12345")
        btn_finish = driver.find_element(By.XPATH, "//button[@type='submit']")
        btn_finish.click()
        print("Success")
        print("Test case started successfully")

    def test_signup_advertiser(self):

        serv = Service("C:\\Drivers\\chromedriver_win32")
        driver = webdriver.Chrome()
        driver.get("https://develop.somomarketingtech.com/select-platform")
        driver.maximize_window()

        btn_advertiser = driver.find_elements(By.CSS_SELECTOR, ".btn.color-secondary-bg.px-4")
        btn_advertiser[1].click()
        # driver.execute_script("arguments[1].click();", btn_advertiser)
        adv_firstname = driver.find_elements(By.CSS_SELECTOR, ".form-control.bg-transparent")
        adv_firstname[0].send_keys("John")

        adv_lastname = driver.find_elements(By.CSS_SELECTOR, ".form-control.bg-transparent")
        adv_lastname[1].send_keys("mily")

        adv_email = driver.find_elements(By.CSS_SELECTOR, ".form-control.bg-transparent")
        adv_email[2].send_keys("polly@yopmail.com")

        adv_business = driver.find_elements(By.CSS_SELECTOR, ".form-control.bg-transparent")
        adv_business[3].send_keys("hello")

        adv_position = driver.find_elements(By.CSS_SELECTOR, ".form-control.bg-transparent")
        adv_position[4].send_keys("CEO")

        drp_advertising = driver.find_element(By.CSS_SELECTOR, ".form-select.bg-transparent")
        drp_advertising.click()

        time.sleep(1)

        selt_advertising = Select(driver.find_element(By.CSS_SELECTOR, ".form-select.bg-transparent"))
        selt_advertising.select_by_index(1)

        drp_platform = driver.find_element(By.XPATH, "//div[@class='col-md-3']//select[@aria-label='Default select example']")
        drp_platform.click()

        time.sleep(1)
        selt_platform = Select(driver.find_element(By.XPATH, "//div[@class='col-md-3']//select[@aria-label='Default select example']"))
        selt_platform.select_by_index(1)

        adv_address = driver.find_element(By.CSS_SELECTOR, ".form-control.bg-transparent.myclass-event.pac-target-input")
        adv_address.send_keys("nj clark")
        time.sleep(4)

        wait = WebDriverWait(driver, 10)
        suggestion_list = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "pac-container")))

        if len(suggestion_list) > 0:
            suggestion_list[0].click()  # Click on the first suggestion to select the address
        else:
            # If no suggestions are found, you may need to handle this scenario differently
            print("No suggestions found.")

        btn_next = driver.find_element(By.XPATH,
                                       "//wizard-button[@class='wizard-footer-right btn button-primary me-1']")
        driver.execute_script("arguments[0].click();", btn_next)
        time.sleep(2)

        adv_password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']")
        adv_password.send_keys("12345")

        adv_confirm_password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Confirm Password']")
        adv_confirm_password.send_keys("12345")

        btn_next2 = driver.find_element(By.XPATH, "//wizard-button[@class='wizard-footer-right btn button-primary me-1']")
        driver.execute_script("arguments[0].click();", btn_next2)

        btn_finish = driver.find_element(By.XPATH, "//wizard-button[@class='wizard-footer-right']")
        driver.execute_script("arguments[0].click();", btn_finish)

        print("success")


openurl = test_signup(webdriver)

openurl.test_signup_driver()
openurl.test_signup_advertiser()
