'''Локатары для всех pages'''

from selenium.webdriver.common.by import By

class MainPageLocators():
    MAIN_LINK = 'https://ohotaktiv.ru/'

    ATTENTION_OA_BANNER = (By.CSS_SELECTOR,
                           '.CookiePopup_accept__2FCsg')
    OPEN_BUTTON = (By.CSS_SELECTOR,
                           'button.ActionsProfile_button__uPVZC')
    OPEN_EMAIL_BUTTON = (By.CSS_SELECTOR,
                         'button.enter_anotherButton__6BUyb')
    LOCATOR_INPUT_LABEL = (By.CSS_SELECTOR,
                          '.Input_label__NBBzX ')
    LOCATOR_INPUT_MAIL = (By.ID,
                          "auth-email")
    LOCATOR_INPUT_BUTTON = (By.CSS_SELECTOR,
                            'button.Button_button__L2jY8.enter_button__2VbvX')
    # Локатор поля ввода кода подтверждения
    CODE_INPUT_FIELD = (By.CSS_SELECTOR, '.code-input_input__VG_m0')
    # Локатор тоста успешной авторизации
    SUCCESS_AUTH_TOAST = (By.XPATH, "//div[contains(@class, 'Toastify__toast-body')]//p[text()='Вы успешно авторизованы.']")

class EmailPageLocators():
    EMAIL_LINK = 'https://mail.google.com/mail'
    #LOCATOR_INPUT_EMAIL_LOGIN = (By.CSS_SELECTOR, '.#identifierId')
    LOCATOR_INPUT_EMAIL_LOGIN = (By.CSS_SELECTOR,
                                 "input[type='email']")
    LOCATOR_OPEN_BUTTON_EMAIL = (By.CSS_SELECTOR,
                                 "div#identifierNext")
    LOCATOR_INPUT_EMAIL_PASS = (By.CSS_SELECTOR,
                                "input[type='password']")
    LOCATOR_OPEN_BUTTON_PASS = (By.CSS_SELECTOR,
                                "div#passwordNext")

class GmailLocators():
    # Локатор строки письма в списке
    EMAIL_ROW = (By.CSS_SELECTOR, 'tr.zA')
    # Локатор сообщений в треде (ветке)
    THREAD_MSG = (By.CSS_SELECTOR, 'div.ajA, div[role="listitem"]')
    # Локатор абзацев в письме
    MSG_PARAGRAPH = (By.TAG_NAME, 'p')

class ChromeWelcomeLocators():
    # Локатор ссылки для закрытия окна приветствия Chrome (по частичному тексту)
    @staticmethod
    def link_by_text(text):
        return (By.XPATH, f"//a[contains(text(), '{text}')]")






