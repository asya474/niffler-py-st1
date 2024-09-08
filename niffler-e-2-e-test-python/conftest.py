import os
from faker import Faker
import pytest
from dotenv import load_dotenv
from selene import browser, be
from clients.spends_client import SpendsHttpClient


@pytest.fixture(scope="session")
def envs():
    load_dotenv()


@pytest.fixture(scope="session")
def frontend_url(envs):
    return os.getenv("FRONTEND_URL")


@pytest.fixture(scope="session")
def gateway_url(envs):
    return os.getenv("GATEWAY_URL")


@pytest.fixture(scope="session")
def app_user(envs):
    return os.getenv("TEST_USERNAME"), os.getenv("TEST_PASSWORD")


@pytest.fixture(scope="function", autouse=True)
def auth(frontend_url):
    fake = Faker()
    name = fake.first_name()
    username, password = name, '12345'
    browser.open(frontend_url)
    # register
    browser.element("a[href='http://auth.niffler.dc:9000/register']").click()
    # create user
    browser.element('#username').type(username)
    browser.element('#password').type(password)
    browser.element('#passwordSubmit').type(password)
    # button sugn up
    browser.element('button.form__submit').click()
    # sign in
    browser.element("a[href='http://frontend.niffler.dc/redirect']").click()
    # auth
    browser.element('[name="username"]').type(username)
    browser.element('[name="password"]').type(password)
    browser.element('button.form__submit').click()
    #return {'username': username, 'password': password}
    #return browser.driver.execute_script('return window.sessionStorage.getItem("id_token")')


@pytest.fixture(scope="session")
def spends_client(gateway_url, auth) -> SpendsHttpClient:
    return SpendsHttpClient(gateway_url, auth)


@pytest.fixture(params=[])
def category(request, spends_client):
    category_name = request.param
    current_categories = spends_client.get_categories()
    category_names = [category["category"] for category in current_categories]
    if category_name not in category_names:
        spends_client.add_category(category_name)
    return category_name


@pytest.fixture(params=[])
def spends(request, spends_client):
    spend = spends_client.add_spends(request.param)
    yield spend
    try:
        # TODO вместо исключения проверить список текущих spends
        spends_client.remove_spends([spend["id"]])
    except Exception:
        pass


@pytest.fixture()
def main_page(auth, frontend_url):
    browser.open(frontend_url)