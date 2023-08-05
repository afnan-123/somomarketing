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

serv = Service("C:\\Drivers\\chromedriver_win32")
driver = webdriver.Chrome()


class Test_Admincruds:

    def test_inventory_crud(self):
        # serv = Service("C:\\Users\\PC\\Downloads\\chromedriver_win32")
        # driver = webdriver.Chrome()
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # Open the website and maximize the window
        driver.get("https://develop.somomarketingtech.com/login")
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        enter_username = driver.find_element(By.ID, "user-name")
        enter_username.send_keys("admin@somomarketing.com")

        enter_password = driver.find_element(By.ID, "user-password")
        enter_password.send_keys("password123")

        submit_button = driver.find_element(By.CSS_SELECTOR, ".color-secondary-bg.px-4.border-0.btn")
        submit_button.click()

        close_popup = wait.until(EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, ".btn.p-1.button-primary.rounded-circle.close-loggedIn")))
        close_popup[0].click()

        menu_inventory = driver.find_elements(By.CSS_SELECTOR, ".accordion-button.f-14.py-2")
        menu_inventory[5].click()
        time.sleep(5)

        add_inventory = driver.find_element(By.XPATH, "//a[normalize-space()='Add Screen']")
        add_inventory.click()
        time.sleep(3)
        add_image = driver.find_element(By.CSS_SELECTOR, ".inputFile.img-h")
        add_image.send_keys("C:\\Users\\PC\\Downloads\\2-way-Audio-Voice-Monitor.jpg")
        time.sleep(2)
        vehicle_category = driver.find_element(By.CSS_SELECTOR, ".form-select.f-14")
        vehicle_category.click()
        select_category = Select(driver.find_element(By.CSS_SELECTOR, ".form-select.f-14"))
        select_category.select_by_index(3)
        inventory_name = driver.find_elements(By.CSS_SELECTOR, ".form-control")
        inventory_name[0].send_keys("Kit 0022")
        inventory_brand = driver.find_elements(By.CSS_SELECTOR, ".form-control")
        inventory_brand[1].send_keys("samsara")
        inventory_price = driver.find_elements(By.CSS_SELECTOR, ".form-control")
        inventory_price[2].send_keys("1000")
        btn_save = driver.find_element(By.CSS_SELECTOR, ".btn.color-secondary-bg.mt-1")
        btn_save.click()
        time.sleep(3)
        delete_inventory = driver.find_element(By.CSS_SELECTOR, ".btn.btn-icon-style.btn-outline-danger")
        delete_inventory.click()
        time.sleep(3)
        btn_yes = driver.find_element(By.CSS_SELECTOR, ".btn.button-primary")
        btn_yes.click()
        time.sleep(5)

    def teammember_crud(self):
        menu_teammember = driver.find_elements(By.CSS_SELECTOR, ".accordion-button.f-14.py-2")
        menu_teammember[1].click()
        time.sleep(5)
        add_member = driver.find_element(By.XPATH, "//a[normalize-space()='Add']")
        add_member.click()
        time.sleep(5)
        pic_upload = driver.find_element(By.CSS_SELECTOR, ".inputFile")
        pic_upload.send_keys("C:\\Users\\PC\\Downloads\\unnamed (6).jpg")
        driver.implicitly_wait(5)
        member_name = driver.find_elements(By.CSS_SELECTOR, ".form-control")
        member_name[0].send_keys("John")
        member_email = driver.find_elements(By.CSS_SELECTOR, ".form-control")
        member_email[1].send_keys("John001@gmail.com")
        member_password = driver.find_elements(By.CSS_SELECTOR, ".form-control")
        member_password[2].send_keys("12345")
        member_cpassword = driver.find_elements(By.CSS_SELECTOR, ".form-control")
        member_cpassword[3].send_keys("12345")
        member_phonenumber = driver.find_element(By.CSS_SELECTOR, ".vti__input")
        member_phonenumber.send_keys("+1 234 567 3534")
        driver.execute_script("window.scrollTo(0, 400)")
        driver.implicitly_wait(5)
        permission_dashboard = driver.find_element(By.XPATH, "//input[@id='31']")
        permission_dashboard.click()
        permission_tech = driver.find_element(By.XPATH, "//input[@id='32']")
        permission_tech.click()
        driver.execute_script("window.scrollTo(0, 450)")
        time.sleep(5)
        wait = WebDriverWait(driver, 10)
        btn_savemember = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".menu-grid.py-2")))
        driver.execute_script("arguments[0].click();", btn_savemember)
        time.sleep(3)


opensomo = Test_Admincruds()
opensomo.test_inventory_crud()
opensomo.teammember_crud()
