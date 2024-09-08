from selene import have, by
from selene.support.shared import browser
from faker import Faker

fake = Faker()


def test_add_information_to_profile(login_user):
    name = fake.first_name()
    surname = fake.last_name()
    # open profile
    browser.element('[class="header__avatar"]').click()
    # name
    browser.element('[name="firstname"]').type(name)
    # surname
    browser.element('[name="surname"]').type(surname)
    # currency
    browser.element('#react-select-7-input').type('KZT').press_enter()
    # submit
    browser.element(by.text('Submit')).click()
    # assert
    assert (browser.element('[class="Toastify__toast-body"]').should(have.text("Profile successfully updated")))


def test_add_category_to_profile(login_user):
    # open profile
    browser.element('[class="header__avatar"]').click()
    # category_name
    browser.element('[name="category"]').type("test category")
    # create category
    browser.element(by.text('Create')).click()
    # assert creation of category
    assert browser.element('[class="categories__item"]').should(have.text("test category"))


def test_add_spending_without_category(login_user):
    # amount
    browser.element('[name="amount"]').type(100)
    # description
    browser.element('[name="description"]').type("test description")
    # add new spending
    browser.element('button.button').should(have.text('Add new spending')).click()
    # assert
    assert browser.element('[class="form__error"]').should(have.text("Category is required"))
