import allure
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.test_cases_page import CasesPage


@allure.title("Test Case 7: Verify Test Cases Page")
def test_test_cases_page(page: Page):
    home_page = HomePage(page)
    test_cases_page = CasesPage(page)

    with allure.step("Navigate to url http://automationexercise.com"):
        home_page.open()

    with allure.step("Verify that home page is visible successfully"):
        expect(page).to_have_title("Automation Exercise")

    with allure.step("Click on Test Cases button"):
        home_page.click_test_cases()

    with allure.step("Verify user is navigated to test cases page successfully"):
        expect(page).to_have_url("https://www.automationexercise.com/test_cases")
        assert test_cases_page.is_test_cases_page_visible()
