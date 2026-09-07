import allure
from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.products_nav_button = ".nav.navbar-nav a[href='/products']"
        self.all_products_heading = "h2:has-text('All Products')"
        self.products_list = ".features_items"
        self.first_view_product_button = "a[href*='/product_details/']"
        
        self.product_name = ".product-information h2"
        self.product_category = ".product-information p:has-text('Category')"
        self.product_price = ".product-information span span"
        self.product_availability = ".product-information p:has-text('Availability')"
        self.product_condition = ".product-information p:has-text('Condition')"
        self.product_brand = ".product-information p:has-text('Brand')"

        self.search_input = "#search_product"
        self.search_button = "#submit_search"
        self.searched_products_heading = "h2:has-text('Searched Products')"

        self.review_heading = "a:has-text('Write Your Review')"
        self.name_input = "#name"
        self.email_input = "#email"
        self.review_input = "#review"
        self.submit_review_button = "#button-review"
        self.success_review_alert = "#review-section .alert-success"

    @allure.step("Click on 'Products' button in header navigation")
    def click_products_nav(self):
        nav_link = self.page.locator(self.products_nav_button).first
        nav_link.wait_for(state="visible")
        nav_link.click()
        self.page.wait_for_url("**/products", wait_until="domcontentloaded")

    @allure.step("Verify user is navigated to ALL PRODUCTS page and products list is visible")
    def verify_all_products_page(self):
        assert "/products" in self.page.url
        self.page.locator(self.all_products_heading).wait_for(state="visible")
        self.page.locator(self.products_list).wait_for(state="visible")

    @allure.step("Click on 'View Product' of the first product in the list")
    def click_first_product_view(self):
        self.page.locator(self.first_view_product_button).first.click()

    @allure.step("Verify all product detail elements are visible on the detail page")
    def verify_product_details(self):
        current_url = self.page.url.split("#")[0]
        assert "/product_details/" in current_url
        self.page.locator(self.product_name).wait_for(state="visible")
        self.page.locator(self.product_category).wait_for(state="visible")
        self.page.locator(self.product_price).wait_for(state="visible")
        self.page.locator(self.product_availability).wait_for(state="visible")
        self.page.locator(self.product_condition).wait_for(state="visible")
        self.page.locator(self.product_brand).wait_for(state="visible")

    @allure.step("Search for product: {product_name}")
    def search_product(self, product_name: str):
        self.fill(self.search_input, product_name)
        self.click(self.search_button)

    @allure.step("Verify searched products results are visible")
    def verify_searched_products(self):
        self.page.locator(self.searched_products_heading).wait_for(state="visible")
        self.page.locator(self.products_list).wait_for(state="visible")

    @allure.step("Verify 'Write Your Review' section is visible")
    def verify_review_section_visible(self):
        review_element = self.page.locator(self.review_heading)
        review_element.wait_for(state="visible")
        assert review_element.is_visible(), "Expected 'Write Your Review' section to be visible"

    @allure.step("Enter name, email, and review text")
    def submit_product_review(self, name: str, email: str, review: str):
        self.fill(self.name_input, name)
        self.fill(self.email_input, email)
        self.fill(self.review_input, review)
        self.click(self.submit_review_button)

    @allure.step("Verify success message")
    def verify_review_success_message(self):
        success_message = self.page.locator(self.success_review_alert)
        success_message.wait_for(state="visible")
        assert "Thank you for your review." in success_message.inner_text()