from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_FORM)
        basket.click()

    def should_name_egual(self):
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        book_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET).text
        assert book_name == book_name_basket, "Names of product isn't equal"
