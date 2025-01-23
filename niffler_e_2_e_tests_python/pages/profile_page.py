from .base_page import BasePage
from selene import have


class ProfilePage(BasePage):

    def assert_category_title(self, expected_text):
        self.find_element('.main-content__section-add-category h2')


    def add_category(self, category):
        self.find_element('input[name=category]').set_value(category)
        self.find_element('.add-category__input-container button').click()


    def assert_added_category(self, category):
        last_category_item = self.find_element('.categories__list .categories__item:last-child')
        last_category_item.should(have.text(category))


    def update_profile(self, name, surname):
        self.find_element('input[name=firstname]').set_value(name)
        self.find_element('input[name=surname]').set_value(surname)
        self.find_element('[type=submit]').click()


    def assert_changes(self, name, surname):
        self.find_element('input[name=firstname]').should(have.value(name))
        self.find_element('input[name=surname]').should(have.value(surname))


profile_page=ProfilePage()