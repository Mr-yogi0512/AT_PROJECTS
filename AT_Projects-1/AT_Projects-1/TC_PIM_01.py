import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tc_login_locators import first_login
from Tc_login_locators import pim_page


# ADMIN LOGIN AND EMPLOYEE ID SAVE IT
class orangeHRM:

    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(8)
        wait = WebDriverWait(self.driver, 20)
        try:
            wait.until(EC.url_matches('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'))

            admin_box = wait.until(EC.presence_of_element_located((By.NAME, first_login().admin)))
            admin_box.send_keys('Admin')

            pass_box = wait.until(EC.presence_of_element_located((By.NAME, first_login().password_fail)))
            pass_box.send_keys('admin123')

            login_box = wait.until(EC.element_to_be_clickable((By.XPATH, first_login().login_button)))
            login_box.click()

            pim = wait.until(EC.visibility_of_element_located((By.XPATH, pim_page().pim_step)))
            pim.click()

            add_emp = wait.until(EC.visibility_of_element_located((By.XPATH, pim_page().emp_click)))
            add_emp.click()

            firstname = wait.until(EC.presence_of_element_located((By.XPATH, pim_page().first_name)))
            firstname.send_keys('Yogesh')

            lastname = wait.until(EC.presence_of_element_located((By.XPATH, pim_page().last_name)))
            lastname.send_keys('r')

            button = wait.until(EC.element_to_be_clickable((By.XPATH, pim_page().button_click)))
            button.click()

            username = wait.until(EC.presence_of_element_located((By.XPATH, pim_page().username_1)))
            username.send_keys('Mr_yogi_yogi')

            password_01 = wait.until(EC.presence_of_element_located((By.XPATH, pim_page().password_1)))
            password_01.send_keys('yogesh12')

            password_02 = wait.until(EC.visibility_of_element_located((By.XPATH, pim_page().password_2)))
            password_02.send_keys('yogesh12')

            save_click = wait.until(EC.element_to_be_clickable((By.XPATH, pim_page().save_id)))
            save_click.click()
            time.sleep(5)

        except TimeoutException:
            print("selenium_error")

    def shutdown(self):
        self.driver.quit()


url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

login_web = orangeHRM(url)

# login_web.login()

login_web.login()

login_web.shutdown()
