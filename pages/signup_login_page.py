import allure
from pages.base_page import BasePage

class SignupLoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.signup_login_nav_button = "a[href='/login']"
        self.signup_name_input = "input[data-qa='signup-name']"
        self.signup_email_input = "input[data-qa='signup-email']"
        self.signup_button = "button[data-qa='signup-button']"

        self.login_email_input = "input[data-qa='login-email']"
        self.login_password_input = "input[data-qa='login-password']"
        self.login_button = "button[data-qa='login-button']"
        self.login_error_message = "form[action*='login'] p"

    @allure.step("Navigate to Signup/Login page")
    def open_login_page(self):
        self.navigate("login")

    @allure.step("Signup with name: {name} and email: {email}")
    def initiate_signup(self, name: str, email: str):
        self.fill(self.signup_name_input, name)
        self.fill(self.signup_email_input, email)
        self.click(self.signup_button)

    @allure.step("Login with wrong email: {email} and password: {password}")
    def login_user(self, email: str, password: str):
        self.fill(self.login_email_input, email)
        self.fill(self.login_password_input, password)
        self.click(self.login_button)