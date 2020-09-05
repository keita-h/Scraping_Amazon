from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
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


class Logout:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        try:
            success_massage = None

            selector = "#nav-hamburger-menu > i"
            element = self.driver.find_element_by_css_selector(selector)
            element.click()

            element = self.driver.find_element_by_link_text("ログアウト")
            element.click()

            selector = "#authportal-main-section > div:nth-child(2) > div > div.a-section > form > div > div > div > h1"
            element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector)))

        except TimeoutException:
            import traceback
            now = dt.datetime.now()
            success_massage = (now.strftime("%H%M%S"),
                               now.strftime("%H:%M:%S") + "\r\n" + traceback.format_exc().strip() + "ログアウトに失敗")

        except NoSuchElementException:
            import traceback
            now = dt.datetime.now()
            success_massage = (now.strftime("%H%M%S"),
                               now.strftime("%H:%M:%S") + "\r\n" + traceback.format_exc().strip() + "ログアウトに失敗")

        except ElementClickInterceptedException:
            import traceback
            now = dt.datetime.now()
            success_massage = (now.strftime("%H%M%S"),
                               now.strftime("%H:%M:%S") + "\r\n" + traceback.format_exc().strip() + "クリックに失敗")

        finally:
            return success_massage
