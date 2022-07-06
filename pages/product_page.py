from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), 'Add to cart button is not presented'

    def click_to_add_to_cart_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def should_be_message_about_item_added_to_cart(self):
        message_item_title = self.browser.find_elements(*ProductPageLocators.MESSAGE_ITEM_TITLE)[0].text
        item_title = self.browser.find_element(*ProductPageLocators.ITEM_TITLE).text
        assert message_item_title == item_title, 'Product name does not match'

    def should_be_message_with_cart_price(self):
        message_item_price = self.browser.find_element(*ProductPageLocators.MESSAGE_ITEM_PRICE).text
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert message_item_price == item_price, 'Product price does not match'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
