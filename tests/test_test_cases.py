import allure
from pages.test_cases_page import CasesPage

@allure.feature("Navigation")
@allure.story("Test Cases Page Verification")
class TestTestCases:

    @allure.title("Test Case 7: Verify Test Cases Page")
    def test_verify_test_cases_page(self, page):
        test_cases_page = CasesPage(page)

        with allure.step("Click 'Test Cases' button and navigation"):
            test_cases_page.click_test_cases_nav()
            test_cases_page.verify_navigation()
            assert "/test_cases" in page.url