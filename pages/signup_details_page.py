import allure
from pages.base_page import BasePage

class SignupDetailsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title = "#id_gender1"
        self.password_input = "#password"
        self.days_dropdown = "#days"
        self.months_dropdown = "#months"
        self.years_dropdown = "#years"
        self.newsletter_checkbox = "#newsletter"
        self.optin_checkbox = "#optin"
        
        self.first_name_input = "#first_name"
        self.last_name_input = "#last_name"
        self.company_input = "#company"
        self.address1_input = "#address1"
        self.address2_input = "#address2"
        self.country_dropdown = "#country"
        self.state_input = "#state"
        self.city_input = "#city"
        self.zipcode_input = "#zipcode"
        self.mobile_input = "#mobile_number"
        self.create_account_button = "button[data-qa='create-account']"
        
        self.account_created_header = "h2[data-qa='account-created']"
        self.continue_button = "a[data-qa='continue-button']"

        self.delete_account_button = "a[href*='delete_account']"
        self.account_deleted_header = "h2[data-qa='account-deleted']"

    @allure.step("Fill out account registration details using dictionary data mapping")
    def fill_account_details(self, data: dict):
        self.page.click(self.title)
        self.page.select_option(self.days_dropdown, "15")
        self.page.select_option(self.months_dropdown, "5")
        self.page.select_option(self.years_dropdown, "1995")
        
        self.page.click(self.newsletter_checkbox)
        self.page.click(self.optin_checkbox)
        
        field_mapping = {
            self.password_input: data["password"],
            self.first_name_input: data["first_name"],
            self.last_name_input: data["last_name"],
            self.company_input: data["company"],
            self.address1_input: data["address1"],
            self.address2_input: data["address2"],
            self.state_input: data["state"],
            self.city_input: data["city"],
            self.zipcode_input: data["zipcode"],
            self.mobile_input: data["mobile"]
        }

        for selector, value in field_mapping.items():
            self.fill(selector, str(value))

        self.page.select_option(self.country_dropdown, data["country"])
        self.click(self.create_account_button)

    @allure.step("Click Continue button")
    def click_continue(self):
        self.click(self.continue_button)

    @allure.step("Delete account")
    def delete_account(self):
        self.click(self.delete_account_button)