import allure
from pages.products_page import ProductsPage
from utils.data_generator import DataGenerator

@allure.feature("Product Reviews")
class TestProductReview:

    @allure.title("Test Case 21: Add review on product")
    def test_add_product_review(self, page):
        products_page = ProductsPage(page)
        user_data = DataGenerator.get_user_registration_data()

        with allure.step("Click on 'Products' button in header"):
            products_page.click_products_nav()

        with allure.step("Verify user is navigated to ALL PRODUCTS page successfully"):
            products_page.verify_all_products_page()
            assert "/products" in page.url

        with allure.step("Click on 'View Product' button"):
            products_page.click_first_product_view()

        with allure.step("Verify 'Write Your Review' is visible"):
            products_page.verify_review_section_visible()

        with allure.step("Enter randomly generated name, email and review"):
            products_page.submit_product_review(
                name=user_data["name"], 
                email=user_data["email"], 
                review="Extremely helpful practice suite for automation testing!"
            )

        with allure.step("Verify success message 'Thank you for your review.'"):
            products_page.verify_review_success_message()
            success_alert = page.locator("#review-section .alert-success")
            assert "Thank you for your review." in success_alert.inner_text()