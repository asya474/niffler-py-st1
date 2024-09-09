import pytest
from selene.support.shared import browser
from faker import Faker
from helper.create_user import create_user

fake = Faker()


@pytest.fixture(scope='function', autouse=True)
def configure_browser():
    browser.config.driver = 'Chrome'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open('http://frontend.niffler.dc/')
    browser.driver.maximize_window()
    yield browser

    browser.quit()


@pytest.fixture(scope='function')
def login_user():
    user_credentials = create_user()
    username = user_credentials['username']
    password = user_credentials['password']
    # login
    browser.element('[name="username"]').type(username)
    browser.element('[name="password"]').type(password)
    browser.element('button.form__submit').click()


@pytest.fixture(scope='function')
def user_credentials():
    user_credentials = create_user()

    yield user_credentials  # Возвращаем данные пользователя для использования в тестах
