import allure
from pages.home_page import HomePage
from pages.cart_page import CartPage
from utils.data_generator import DataGenerator

@allure.feature("Home Page")
@allure.story("Newsletter Subscription")
class TestSubscription:

    @allure.title("Test Case 10: Verify Subscription in home page")
    def test_verify_subscription_in_home_page(self, page):
        home_page = HomePage(page)

        with allure.step("Scroll down to footer and verify SUBSCRIPTION text"):
            home_page.scroll_to_bottom()
            home_page.verify_subscription_heading()
            assert page.locator(".single-widget h2").is_visible()

        with allure.step("Enter email address and click subscribe arrow button"):
            user_data = DataGenerator.get_user_registration_data()
            home_page.subscribe_email(user_data["email"])

        with allure.step("Verify success message 'You have been successfully subscribed!' is visible"):
            home_page.verify_success_message()

    @allure.title("Test Case 11: Verify Subscription in Cart page")
    def test_verify_subscription_in_cart_page(self, page):
        cart_page = CartPage(page)

        with allure.step("Click 'Cart' button"):
            cart_page.click_cart_nav()
            assert "/view_cart" in page.url

        with allure.step("Scroll down to footer and verify 'SUBSCRIPTION' text"):
            cart_page.scroll_to_bottom()
            cart_page.verify_subscription_heading()
            assert page.locator(".single-widget h2").is_visible()

        with allure.step("Enter email address in input and click arrow button"):
            user_data = DataGenerator.get_user_registration_data()
            cart_page.subscribe_email(user_data["email"])

        with allure.step("Verify success message 'You have been successfully subscribed!' is visible"):
            cart_page.verify_success_message()