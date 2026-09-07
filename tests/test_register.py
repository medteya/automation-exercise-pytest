import allure
from pages.signup_login_page import SignupLoginPage
from pages.signup_details_page import SignupDetailsPage
from utils.data_generator import DataGenerator

@allure.feature("Authentication")
@allure.story("User Registration Flow")
class TestRegister:

    @allure.title("Test Case 1: Register User")
    def test_register_user_end_to_end(self, page):
        login_page = SignupLoginPage(page)
        details_page = SignupDetailsPage(page)

        user_data = DataGenerator.get_user_registration_data()
        name = user_data["name"]
        email = user_data["email"]

        with allure.step("Click 'Signup / Login' button and verify 'New User Signup!' is visible"):
            login_page.open_login_page()
            assert page.get_by_text("New User Signup!").is_visible()

        with allure.step("Enter credentials and initiate signup"):
            login_page.initiate_signup(name, email)
            page.get_by_text("Enter Account Information").wait_for(state="visible")

        with allure.step("Fill out full account details and submit"):
            details_page.fill_account_details(user_data)

        with allure.step("Verify account creation and continue"):
            assert page.get_by_text("Account Created!").is_visible()
            details_page.click_continue()

        with allure.step("Verify user is successfully logged in"):
            assert page.get_by_text(f"Logged in as {name}").is_visible()

        with allure.step("Delete account and verify deletion"):
            details_page.delete_account()
            page.get_by_text("Account Deleted!").wait_for(state="visible")
            details_page.click_continue()