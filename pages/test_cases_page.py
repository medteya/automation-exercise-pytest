import allure
from pages.base_page import BasePage

class CasesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.test_cases_nav_button = ".nav.navbar-nav a[href='/test_cases']"
        self.test_cases_heading = "h2:has-text('Test Cases')"

    @allure.step("Click on 'Test Cases' header button")
    def click_test_cases_nav(self):
        nav_link = self.page.locator(self.test_cases_nav_button).first
        nav_link.wait_for(state="visible")
        nav_link.click()
        self.page.wait_for_url("**/test_cases", wait_until="domcontentloaded")

    @allure.step("Verify user is successfully navigated to the Test Cases page")
    def verify_navigation(self):
        assert "/test_cases" in self.page.url
        self.page.locator(self.test_cases_heading).wait_for(state="visible")