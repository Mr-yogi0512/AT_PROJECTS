import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Tc_login_locators import first_login
from Tc_login_locators import pim_page


# ADMIN EDIT EMPLOYEE ID DELETED

class orangeHRM:

    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome()

    def login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            self.driver.implicitly_wait(10)
            wait = WebDriverWait(self.driver, 20)

            wait.until(EC.url_matches('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'))

            admin_box = wait.until(EC.presence_of_element_located((By.NAME, first_login().admin)))
            admin_box.send_keys('Admin')

            pass_box = wait.until(EC.presence_of_element_located((By.NAME, first_login().password_fail)))
            pass_box.send_keys('admin123')

            login_box = wait.until(EC.element_to_be_clickable((By.XPATH, first_login().login_button)))
            login_box.click()
            # time.sleep(3)
            pim = wait.until(EC.visibility_of_element_located((By.XPATH, pim_page().pim_step)))
            pim.click()
            emp_name_search = wait.until(EC.visibility_of_element_located((By.XPATH, pim_page().emp_name)))
            emp_name_search.send_keys('Yogesh r')
            search_emp = wait.until(EC.presence_of_element_located((By.XPATH, pim_page().search_name)))
            search_emp.click()
            delete_emp = wait.until(EC.presence_of_element_located((By.XPATH, pim_page().delete_id)))
            delete_emp.click()

            self.driver.switch_to.window(self.driver.window_handles[0])

            alert_switch = wait.until(EC.element_to_be_clickable((By.XPATH, pim_page().switch_alert)))
            alert_switch.click()
            time.sleep(5)

            if 'No Records Found' in self.driver.page_source:
                print('SUCCESS FULL TEXT : Found it deleted!')
            else:
                print('FAILED TEXT : Did not find it not deleted.')

        except TimeoutException as selenium_error:
            print(selenium_error)

    def shutdown(self):
        self.driver.quit()


url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

login_web = orangeHRM(url)

login_web.login()

login_web.shutdown()
