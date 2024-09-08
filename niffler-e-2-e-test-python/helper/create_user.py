from selene.support.shared import browser
from faker import Faker

fake = Faker()
def create_user():
    name = fake.first_name()
    username, password = name, '12345'
    browser.open('http://frontend.niffler.dc/')
    #register
    browser.element("a[href='http://auth.niffler.dc:9000/register']").click()
    #create user
    browser.element('#username').type(username)
    browser.element('#password').type(password)
    browser.element('#passwordSubmit').type(password)
    #button sugn up
    browser.element('button.form__submit').click()
    # sign in
    browser.element("a[href='http://frontend.niffler.dc/redirect']").click()
    return {'username': username, 'password': password}