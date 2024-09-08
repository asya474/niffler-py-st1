from selene.support.conditions import have, be
from selene.support.shared import browser



def test_success_login(user_credentials):
    username = user_credentials['username']
    password = user_credentials['password']
    # type credentials
    browser.element('[name="username"]').type(username)
    browser.element('[name="password"]').type(password)
    browser.element('button.form__submit').click()
    # assert success login
    assert browser.element('[class="main-content__section main-content__section-add-spending"]').should(be.visible)



def test_wrong_password(user_credentials):
    username = user_credentials['username']
    wrong_password = '123'
    # type credentials
    browser.element('[name="username"]').type(username)
    browser.element('[name="password"]').type(wrong_password)
    browser.element('button.form__submit').click()
    # assert validation error
    assert browser.element('p.form__error').should(have.text('Неверные учетные данные пользователя'))