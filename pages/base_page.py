import allure
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://automationexercise.com"

    @allure.step("Dismiss ad overlay if present")
    def dismiss_ad_if_present(self):
        close_selectors = [
            "#dismiss-button",
            "iframe[name*='aswift']", 
            ".ns-m-2-dismiss-button",
            "div[aria-label='Close ad']",
            "button:has-text('Close')"
        ]
        
        for selector in close_selectors:
            locator = self.page.locator(selector).first
            if locator.is_visible():
                try:
                    locator.click()
                    break
                except Exception:
                    pass
                
        if "#google_vignette" in self.page.url:
            try:
                self.page.go_back()
            except Exception:
                pass

    @allure.step("Navigate to application URL: {url_path}")
    def navigate(self, url_path=""):
        self.page.goto(f"{self.base_url}/{url_path}")

    @allure.step("Click element: {selector}")
    def click(self, selector: str):
        self.page.click(selector)
        self.dismiss_ad_if_present()
        if "#google_vignette" in self.page.url:
            self.page.click(selector)

    @allure.step("Fill input {selector} with value")
    def fill(self, selector: str, value: str):
        self.page.fill(selector, value)

    @allure.step("Get text from element: {selector}")
    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).text_content()

    @allure.step("Verify element is visible: {selector}")
    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()