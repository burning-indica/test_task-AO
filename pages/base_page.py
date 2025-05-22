'''Класс с методами для работы с WebDriver'''

from conftest import browser
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime

class BasePage():
    # Базовый класс для всех страниц

    def __init__(self, browser, url, timeout=10):
        '''Инициализация'''
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open_site(self):
        self.browser.get(self.url)

    def wait_and_click(self, locator, timeout=10):
        # Ожидает, пока элемент станет кликабельным, и кликает по нему
        element = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        return element

    def wait_visible(self, locator, timeout=10):
        # Ожидает, пока элемент станет видимым
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def save_screenshot(self, name_prefix="fail"):
        # Сохраняет скриншот текущей страницы в папку screenshots с уникальным именем
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{name_prefix}_{timestamp}.png"
        self.browser.save_screenshot(filename)
        logging.info(f"Скриншот сохранён: {filename}")
        return filename


