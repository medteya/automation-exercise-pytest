import allure
from pages.signup_login_page import SignupLoginPage
from utils.data_generator import DataGenerator

@allure.feature("Authentication")
@allure.story("Negative Login Flow")
class TestLoginNegative:

    @allure.title("Test Case 2: Login User with incorrect email and password")
    def test_login_with_invalid_credentials(self, page):
        login_page = SignupLoginPage(page)
        invalid_data = DataGenerator.get_invalid_credentials()

        with allure.step("Navigate to Login/Signup view"):
            login_page.open_login_page()

        with allure.step("Verify 'Login to your account' is visible"):
            assert page.get_by_text("Login to your account").is_visible()

        with allure.step("Enter incorrect credentials and click login"):
            login_page.login_user(invalid_data["email"], invalid_data["password"])

        with allure.step("Verify error 'Your email or password is incorrect!' is displayed"):
            page.get_by_text("Your email or password is incorrect!").wait_for(state="visible")