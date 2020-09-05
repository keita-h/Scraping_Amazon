from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
import datetime as dt


"""
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
"""

options = Options()
options.add_argument('--disable-gpu')
options.add_argument('--disable-extensions')
options.add_argument('--proxy-server="direct://"')
options.add_argument('--proxy-bypass-list=*')
options.add_argument('--start-maximized')


class Login:
    def __init__(self, driver):
        self.driver = driver

    def input_email(self, email):
        try:

            success_massage = None

            selector = "#ap_email"
            element = self.driver.find_element_by_css_selector(selector)
            element.send_keys(email)

            selector = "#continue"
            element = self.driver.find_element_by_css_selector(selector)
            element.click()

            selector = "#ap_password"
            element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector)))

        except TimeoutException:
            import traceback
            now = dt.datetime.now()
            success_massage = (now.strftime("%H%M%S"),
                               now.strftime("%H:%M:%S") + "\r\n" + traceback.format_exc().strip() + "メールアドレス入力に失敗")

        except NoSuchElementException:
            import traceback
            now = dt.datetime.now()
            success_massage = (now.strftime("%H%M%S"),
                               now.strftime("%H:%M:%S") + "\r\n" + traceback.format_exc().strip() + "メールアドレス入力に失敗")

        except ElementNotInteractableException:
            import traceback
            now = dt.datetime.now()
            success_massage = (now.strftime("%H%M%S"),
                               now.strftime("%H:%M:%S") + "\r\n" + traceback.format_exc().strip() + "メールアドレス入力に失敗")

        except ElementClickInterceptedException:
            import traceback
            now = dt.datetime.now()
            success_massage = (now.strftime("%H%M%S"),
                               now.strftime("%H:%M:%S") + "\r\n" + traceback.format_exc().strip() + "クリックに失敗(メールアドレス)")

        finally:
            return success_massage

    def input_pass(self, password):
        try:
            success_massage = None

            selector = "#ap_password"
            element = self.driver.find_element_by_css_selector(selector)
            element.send_keys(password)

            selector = "#signInSubmit"
            element = self.driver.find_element_by_css_selector(selector)
            element.click()
            self.driver.implicitly_wait(10)
            selector = "#nav-hamburger-menu > i"

            element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector)))

        except TimeoutException:
            import traceback
            now = dt.datetime.now()
            success_massage = (now.strftime("%H%M%S"),
                               now.strftime("%H:%M:%S") + "\r\n" + traceback.format_exc().strip() + "パスワード入力に失敗")

        except NoSuchElementException:
            import traceback
            now = dt.datetime.now()
            success_massage = (now.strftime("%H%M%S"),
                               now.strftime("%H:%M:%S") + "\r\n" + traceback.format_exc().strip() + "パスワード入力に失敗")

        except ElementNotInteractableException:
            import traceback
            now = dt.datetime.now()
            success_massage = (now.strftime("%H%M%S"),
                               now.strftime("%H:%M:%S") + "\r\n" + traceback.format_exc().strip() + "パスワード入力に失敗")

        except ElementClickInterceptedException:
            import traceback
            now = dt.datetime.now()
            success_massage = (now.strftime("%H%M%S"),
                               now.strftime("%H:%M:%S") + "\r\n" + traceback.format_exc().strip() + "クリックに失敗(パスワード)")

        finally:
            return success_massage
