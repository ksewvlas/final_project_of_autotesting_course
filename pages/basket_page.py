from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_dir()

    def should_be_basket_url(self):
        basket_url = self.browser.current_url
        print(basket_url)
        assert 'basket' in basket_url, 'This is not basket page'

    def should_be_basket_dir(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_DIR), 'Basket directory is not presented'

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), 'Basket is not empty'
