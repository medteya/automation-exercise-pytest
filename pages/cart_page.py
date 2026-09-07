import allure
from pages.home_page import HomePage

class CartPage(HomePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_nav_button = "a[href='/view_cart']"

    @allure.step("Click on 'Cart' button in header navigation")
    def click_cart_nav(self):
        self.page.locator(self.cart_nav_button).first.click()
        self.page.wait_for_url("**/view_cart", wait_until="domcontentloaded")