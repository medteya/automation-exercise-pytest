import allure
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.footer_heading = ".single-widget h2"
        self.subscribe_input = "#susbscribe_email"
        self.subscribe_button = "#subscribe"
        self.success_alert = "#success-subscribe"

        self.scroll_up_arrow = "#scrollUp"
    
    @allure.step("Scroll down page to bottom")
    def scroll_to_bottom(self):
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    @allure.step("Verify subscription heading text in footer")
    def verify_subscription_heading(self):
        self.page.locator(self.footer_heading).wait_for(state="visible")
        assert "subscription" in self.get_text(self.footer_heading).lower()

    @allure.step("Enter email {email} and submit subscription")
    def subscribe_email(self, email: str):
        self.fill(self.subscribe_input, email)
        self.click(self.subscribe_button)

    @allure.step("Verify success subscription message is visible")
    def verify_success_message(self):
        self.page.locator(self.success_alert).wait_for(state="visible")
        assert "You have been successfully subscribed!" in self.get_text(self.success_alert)

    @allure.step("Scroll up page to top")
    def scroll_up_to_top(self):
        self.page.evaluate("window.scrollTo(0, 0)")

    @allure.step("Click on the scroll-up arrow button at the bottom right")
    def click_scroll_up_arrow(self):
        arrow = self.page.locator(self.scroll_up_arrow)
        arrow.scroll_into_view_if_needed()
        arrow.click()

    @allure.step("Verify main banner text is visible: {expected_text}")
    def verify_main_banner_text_visible(self, expected_text: str):
        banner_locator = self.page.locator(f"h2:has-text('{expected_text}')").first
        banner_locator.wait_for(state="visible")
        assert banner_locator.is_visible(), f"Expected banner text '{expected_text}' to be visible on screen"