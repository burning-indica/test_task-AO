from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    # Класс для работы с главной страницей сайта ОхотАктив

    def attention_see(self):
        # Закрывает баннер подтверждения возраста, если он появился
        try:
            # Ожидание появления баннера подтверждения возраста
            WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(MainPageLocators.ATTENTION_OA_BANNER)
            )
            butt = self.browser.find_element(*MainPageLocators.ATTENTION_OA_BANNER)  # Находим баннер
            butt.click()  # Клик по баннеру для его закрытия
        except NoSuchElementException:
            # Если баннер не найден, продолжаем тест без ошибок
            print("Баннер подтверждения возраста не найден, продолжаем тест.")

    def open_button_registration(self):
        # Открывает форму регистрации
        # Ожидание, пока кнопка регистрации станет кликабельной
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(MainPageLocators.OPEN_BUTTON)
        )
        butt = self.browser.find_element(*MainPageLocators.OPEN_BUTTON)  # Находим кнопку регистрации
        butt.click()  # Клик по кнопке регистрации

    def open_button_email(self):
        # Открывает форму входа по email
        # Ожидание, пока кнопка для открытия email станет кликабельной
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(MainPageLocators.OPEN_EMAIL_BUTTON)
        )
        butt = self.browser.find_element(*MainPageLocators.OPEN_EMAIL_BUTTON)  # Находим кнопку для открытия email
        butt.click()  # Клик по кнопке для открытия email

    def email_label_input(self, email):
        # Активирует поле ввода email и отправляет email
        # Ожидание появления метки email
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.LOCATOR_INPUT_LABEL)
        )
        label = self.browser.find_element(*MainPageLocators.LOCATOR_INPUT_LABEL)  # Находим метку email
        label.click()  # Клик по метке email для активации поля ввода

        # Ожидание появления поля ввода email
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.LOCATOR_INPUT_MAIL)
        )
        input_txt = self.browser.find_element(*MainPageLocators.LOCATOR_INPUT_MAIL)  # Находим поле ввода email
        input_txt.send_keys(email)  # Вводим email, переданный в метод

        # Ожидание, пока кнопка для отправки email станет кликабельной
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOCATOR_INPUT_BUTTON)
        )
        input_button = self.browser.find_element(*MainPageLocators.LOCATOR_INPUT_BUTTON)  # Находим кнопку отправки
        input_button.click()  # Клик по кнопке отправки email

    def input_confirmation_code(self, confirmation_code):
        # Вводит код подтверждения по цифрам в соответствующие поля
        code_digits = list(confirmation_code)  # Преобразуем код в список цифр

        # Ожидание появления полей ввода кода подтверждения
        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(MainPageLocators.CODE_INPUT_FIELD)
        )
        input_fields = self.browser.find_elements(*MainPageLocators.CODE_INPUT_FIELD)  # Находим поля ввода кода

        # Проверяем, совпадает ли количество полей с количеством цифр в коде
        if len(input_fields) != len(code_digits):
            print("Количество полей ввода не совпадает с количеством цифр в коде.")
            return

        # Вводим каждую цифру кода в соответствующее поле
        for i, digit in enumerate(code_digits):
            input_fields[i].send_keys(digit)  # Ввод каждой цифры кода

        print("Код подтверждения успешно введен.")

    def check_successful_authorization(self):
        # Проверяет появление уведомления об успешной авторизации
        try:
            # Ожидание появления уведомления об успешной авторизации
            WebDriverWait(self.browser, 20).until(
                EC.visibility_of_element_located(MainPageLocators.SUCCESS_AUTH_TOAST)
            )
            return True  # Успешная авторизация
        except TimeoutException:
            print("Уведомление об успешной авторизации не найдено.")
            return False  # Неуспешная авторизация