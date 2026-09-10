import allure
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.title("Test Case 4: Logout User")
def test_logout_user(page: Page, registered_user: dict):
    home_page = HomePage(page)
    login_page = LoginPage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Verify that home page is visible successfully"):
        assert page.title() == "Automation Exercise"

    with allure.step("Click on Signup / Login button"):
        home_page.click_signup_login()

    with allure.step("Verify Login to your account is visible"):
        assert login_page.is_login_to_account_visible()

    with allure.step("Enter correct email address and password"):
        login_page.fill_login_form(
            registered_user["email"],
            registered_user["password"],
        )

    with allure.step("Click login button"):
        login_page.click_login()

    with allure.step("Verify that Logged in as username is visible"):
        assert home_page.is_logged_in_as_visible()

    with allure.step("Click Logout button"):
        home_page.click_logout()

    with allure.step("Verify that user is navigated to login page"):
        expect(page).to_have_url("https://www.automationexercise.com/login")
