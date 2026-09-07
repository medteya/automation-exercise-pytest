import allure
from pages.home_page import HomePage

@allure.feature("Scroll Functionality")
class TestScroll:

    @allure.title("Test Case 25: Verify Scroll Up using 'Arrow' button and Scroll Down functionality")
    def test_scroll_up_using_arrow(self, page):
        home_page = HomePage(page)

        with allure.step("Scroll down page to bottom"):
            home_page.scroll_to_bottom()

        with allure.step("Verify 'SUBSCRIPTION' is visible"):
            home_page.verify_subscription_heading()
            assert page.locator(".single-widget h2").is_visible()

        with allure.step("Click on arrow at bottom right side to move upward"):
            home_page.click_scroll_up_arrow()

        with allure.step("Verify that page is scrolled up and header text is visible"):
            home_page.verify_main_banner_text_visible("Full-Fledged practice website for Automation Engineers")

    @allure.title("Test Case 26: Verify Scroll Up without 'Arrow' button and Scroll Down functionality")
    def test_scroll_up_without_arrow(self, page):
        home_page = HomePage(page)

        with allure.step("Scroll down page to bottom"):
            home_page.scroll_to_bottom()

        with allure.step("Verify 'SUBSCRIPTION' is visible"):
            home_page.verify_subscription_heading()
            assert page.locator(".single-widget h2").is_visible()

        with allure.step("Scroll up page to top programmatically"):
            home_page.scroll_up_to_top()

        with allure.step("Verify that page is scrolled up and header text is visible"):
            home_page.verify_main_banner_text_visible("Full-Fledged practice website for Automation Engineers")