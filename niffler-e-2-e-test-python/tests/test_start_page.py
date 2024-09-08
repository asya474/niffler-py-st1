import pytest
from selene.support.conditions import have
from selene.support.shared import browser
from faker import Faker

fake = Faker()
username = fake.first_name()

def test_start_page_authorization_button():
    browser.open('http://frontend.niffler.dc/')
    browser.element("a[href='/redirect']").click()
    assert browser.element('p.form__paragraph').should(have.text("Please sign in"))

def test_start_page_registration_button():
    browser.open('http://frontend.niffler.dc/')
    browser.element("a[href='http://auth.niffler.dc:9000/register']").click()
    assert browser.element('p.form__paragraph').should(have.text("Registration form"))