import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Locators import PIM_Locators


class OrangeHRM:
    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome()

    def login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            self.driver.implicitly_wait(10)
            wait = WebDriverWait(self.driver, 20)

            forget_password = wait.until(EC.presence_of_element_located((By.XPATH, PIM_Locators().reset_xpath)))
            forget_password.click()

            username_send = wait.until(EC.presence_of_element_located((By.XPATH, PIM_Locators().username_xpath)))
            username_send.send_keys('YOGESH R')

            username_reset = wait.until(EC.element_to_be_clickable((By.XPATH, PIM_Locators().reset_username)))
            username_reset.click()
            time.sleep(5)

            if 'Reset Password link sent successfully' in self.driver.page_source:
                print('SUCCESS : Reset with in username completed')
            else:
                print('FAILED : Reset with in username not completed')

        except TimeoutException:
            print('waiting for page load')


url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

login_web = OrangeHRM(url)

login_web.login()
