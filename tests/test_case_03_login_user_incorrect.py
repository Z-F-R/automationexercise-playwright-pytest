import allure
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.title("Test Case 3: Login User with incorrect email and password")
def test_login_user_incorrect(page: Page):
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

    with allure.step("Enter incorrect email address and password"):
        login_page.fill_login_form("incorrect@example.com", "IncorrectPassword123!")

    with allure.step("Click login button"):
        login_page.click_login()

    with allure.step("Verify error 'Your email or password is incorrect!' is visible"):
        assert login_page.is_login_error_visible()