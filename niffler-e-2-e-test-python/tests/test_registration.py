import pytest
from selene.support.conditions import have
from selene.support.shared import browser
from faker import Faker

fake = Faker()
username = fake.first_name()


def test_success_registration():
    # open registration page
    browser.element("a[href='http://auth.niffler.dc:9000/register']").click()
    # fill form inputs
    browser.element('#username').type(username)
    browser.element('#password').type('12345')
    browser.element('#passwordSubmit').type('12345')
    # create user
    browser.element('button.form__submit').click()
    # check success registration
    assert browser.element('p.form__paragraph').should(have.text("Congratulations! You've registered!"))


def test_registration_password_validation():
    # pen registration page
    browser.element("a[href='http://auth.niffler.dc:9000/register']").click()
    # fill form inputs
    browser.element('#username').type(username)
    browser.element('#password').type('12345')
    browser.element('#passwordSubmit').type('12347')
    # create user
    browser.element('button.form__submit').click()
    # check validation password
    assert browser.element('#register-form > label:nth-child(6) > span').should(have.text("Passwords should be equal"))
