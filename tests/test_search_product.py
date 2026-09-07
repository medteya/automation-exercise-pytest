import allure
from pages.products_page import ProductsPage

@allure.feature("Products")
@allure.story("Product Search Functionality")
class TestSearchProduct:

    @allure.title("Test Case 9: Search Product")
    def test_search_product(self, page):
        products_page = ProductsPage(page)

        with allure.step("Navigate to Products page and verify catalog view"):
            products_page.click_products_nav()
            products_page.verify_all_products_page()

        with allure.step("Enter product name in search input and search"):
            products_page.search_product("Top")
            assert "search" in page.url

        with allure.step("Verify 'SEARCHED PRODUCTS' heading and product list are visible"):
            products_page.verify_searched_products()
            assert page.locator("h2:has-text('Searched Products')").is_visible()