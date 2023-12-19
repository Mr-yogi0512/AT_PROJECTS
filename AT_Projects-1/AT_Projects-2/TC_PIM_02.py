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
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        wait = WebDriverWait(self.driver, 20)
        try:
            wait.until(EC.url_matches('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'))

            admin_box = wait.until(EC.presence_of_element_located((By.XPATH, PIM_Locators().username_locators)))
            admin_box.send_keys('Admin')

            pass_box = wait.until(EC.presence_of_element_located((By.XPATH, PIM_Locators().password_xpath)))
            pass_box.send_keys('admin123')

            login_box = wait.until(EC.element_to_be_clickable((By.XPATH, PIM_Locators().login_box)))
            login_box.click()
            # correct title verify
            self.driver.get(self.driver.current_url)
            my_title = self.driver.title
            print(my_title)
            admin_click = wait.until(EC.element_to_be_clickable((By.XPATH, PIM_Locators().admin_xpath)))
            admin_click.click()
            # Mention the admin page header
            header_admin_page = wait.until(EC.presence_of_element_located(((By.XPATH, PIM_Locators().
                                                                            admin_page_header)))).text
            print(header_admin_page.title())

        except TimeoutException:
            print("loading page")


url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

login_web = OrangeHRM(url)

login_web.login()
