import re
from .base_page import BasePage
from .locators import EmailPageLocators, GmailLocators, ChromeWelcomeLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

# В методах класса EmailPage
class EmailPage(BasePage):
    # Класс для работы со страницей Gmail

    def close_chrome_welcome_popup(self):
        # Закрывает окно приветствия Chrome, если оно появилось
        popup_closed = False
        # Пробуем разные варианты текста ссылки
        variants = [
            "не входя в аккаунт",
            "использовать Chrome",
            "использовать chrome",
            "продолжить как",
            "не входя"
        ]
        for text in variants:
            try:
                # Используем локатор для ссылки по тексту
                link = WebDriverWait(self.browser, 2).until(
                    EC.element_to_be_clickable(ChromeWelcomeLocators.link_by_text(text))
                )
                link.click()
                print(f'Окно приветствия Chrome закрыто по ссылке: {text}')
                popup_closed = True
                break
            except TimeoutException:
                continue
        if not popup_closed:
            # Пробуем нажать ESC
            try:
                self.browser.switch_to.active_element.send_keys(Keys.ESCAPE)
                print('Окно приветствия Chrome попытались закрыть через ESC.')
            except Exception:
                print('Не удалось закрыть окно приветствия Chrome.')

    def input_email_login(self, email):
        # Вводит email в форму авторизации Gmail
        self.close_chrome_welcome_popup()
        email_address = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(EmailPageLocators.LOCATOR_INPUT_EMAIL_LOGIN)
        )
        email_address.send_keys(email)

    def submit_login(self):
        # Кликает по кнопке "Далее" после ввода email
        login_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(EmailPageLocators.LOCATOR_OPEN_BUTTON_EMAIL)
        )
        login_button.click()

    def input_password(self, password):
        # Вводит пароль в форму авторизации Gmail
        password_field = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(EmailPageLocators.LOCATOR_INPUT_EMAIL_PASS)
        )
        password_field.send_keys(password)

    def submit_pass(self):
        # Кликает по кнопке "Далее" после ввода пароля
        pass_button = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(EmailPageLocators.LOCATOR_OPEN_BUTTON_PASS)
        )
        pass_button.click()

    def read_first_email(self):
        # Открывает первый тред от ОхотАктив и извлекает код подтверждения из самого последнего сообщения в треде
        # Явное ожидание для списка сообщений
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(GmailLocators.EMAIL_ROW)
        )
        emails = self.browser.find_elements(*GmailLocators.EMAIL_ROW)
        print(f'Найдено писем: {len(emails)}')
        # Находим первое (самое верхнее) письмо от ОхотАктив
        ohotaktiv_email = None
        for email in emails:
            if "ОхотАктив" in email.text:
                ohotaktiv_email = email
                break
        if not ohotaktiv_email:
            print("Письмо от ОхотАктив не найдено.")
            return None
        ohotaktiv_email.click()  # Открываем тред
        # Ждём появления всех сообщений в треде
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_all_elements_located(GmailLocators.THREAD_MSG)
        )
        thread_msgs = self.browser.find_elements(*GmailLocators.THREAD_MSG)
        print(f'Сообщений в треде: {len(thread_msgs)}')
        if not thread_msgs:
            print("Сообщения в треде не найдены.")
            return None
        last_msg = thread_msgs[-1]
        # Получаем текст из всех <p> в этом сообщении
        paragraphs = last_msg.find_elements(*GmailLocators.MSG_PARAGRAPH)
        full_text = ' '.join([p.text for p in paragraphs])
        print(f'Текст последнего сообщения: {full_text}')
        # Ищем код подтверждения
        match = re.search(r'Ваш код подтверждения:\s*(\d{4})', full_text)
        if match:
            confirmation_code = match.group(1)
            print(f"Код подтверждения: {confirmation_code}")
            return confirmation_code
        else:
            print("Код подтверждения не найден.")
            return None