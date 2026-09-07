import allure
from pages.products_page import ProductsPage

@allure.feature("Products")
@allure.story("Product Catalog and Detail View")
class TestProducts:

    @allure.title("Test Case 8: Verify All Products and product detail page")
    def test_verify_all_products_and_details(self, page):
        products_page = ProductsPage(page)

        with allure.step("Navigate to Products page and verify catalog view"):
            products_page.click_products_nav()
            products_page.verify_all_products_page()
            assert "/products" in page.url

        with allure.step("Select first product and verify all detail attributes"):
            products_page.click_first_product_view()
            products_page.verify_product_details()