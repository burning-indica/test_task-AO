'''Модуль фикстур'''

import pytest
from selenium import webdriver
import tempfile

def pytest_addoption(parser):
    parser.addoption("--email", action="store", default=None, help="Email for login")
    parser.addoption("--password", action="store", default=None, help="Password for login")

@pytest.fixture
def login_data(request):
    email = request.config.getoption("--email")
    password = request.config.getoption("--password")
    return email, password

@pytest.fixture
def browser():
    '''Фикстура доступа к вебдрайверу'''
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-infobars")  # Отключение информационных панелей
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--disable-features=ChromeWhatsNewUI")
    options.add_argument("--disable-features=EnableChromeBrowserCloudManagement")
    options.add_argument("--disable-sync")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    user_data_dir = tempfile.mkdtemp()
    options.add_argument(f'--user-data-dir={user_data_dir}')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()