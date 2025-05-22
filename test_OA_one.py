import time
import logging
import pytest
import allure

from pages.email_page import EmailPage
from pages.locators import MainPageLocators
from pages.locators import EmailPageLocators
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCase1:

    @allure.title("Проверка регистрации/авторизации пользователя с валидной почтой")
    @allure.description("Тест автоматизирует сценарий регистрации/авторизации пользователя через email и подтверждение кода из Gmail.")
    def test_open_link(self, browser, login_data):
        email, password = login_data
        logging.basicConfig(level=logging.INFO)
        try:
            with allure.step("Открываем главную страницу сайта"):
                page = MainPage(
                    browser,
                    MainPageLocators.MAIN_LINK
                )
                page.open_site()
            with allure.step("Открываем новую вкладку для Gmail"):
                browser.execute_script("window.open('about:blank', '_blank');")
                browser.switch_to.window(browser.window_handles[1])
            with allure.step("Авторизация в Gmail и получение кода подтверждения"):
                emailpage = EmailPage(
                    browser,
                    EmailPageLocators.EMAIL_LINK
                )
                emailpage.open_site()
                emailpage.input_email_login(email)
                emailpage.submit_login()
                emailpage.input_password(password)
                emailpage.submit_pass()
            with allure.step("Регистрация/авторизация на сайте ОхотАктив"):
                browser.switch_to.window(browser.window_handles[0])
                page.attention_see()
                page.open_button_registration()
                page.open_button_email()
                page.email_label_input(email)
            with allure.step("Получение и ввод кода подтверждения"):
                browser.switch_to.window(browser.window_handles[1])
                confirmation_code = emailpage.read_first_email()
                browser.close()
                browser.switch_to.window(browser.window_handles[0])
                page.input_confirmation_code(confirmation_code)
            with allure.step("Проверка успешной авторизации"):
                assert page.check_successful_authorization(), "Авторизация не удалась!"
                logging.info("Авторизация прошла успешно!")
        except Exception as e:
            logging.error(f"Ошибка в тесте: {e}")
            # Вложение скриншота в Allure
            screenshot_path = page.save_screenshot("fail")
            if screenshot_path:
                allure.attach.file(screenshot_path, name="fail_screenshot", attachment_type=allure.attachment_type.PNG)
            raise

        #time.sleep(10)  # Ожидание для наблюдения результата