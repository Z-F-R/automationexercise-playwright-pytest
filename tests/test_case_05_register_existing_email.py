import allure
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.signup_page import SignupPage


@allure.title("Test Case 5: Register User with existing email")
def test_register_existing_email(page: Page, registered_user: dict):
    home_page = HomePage(page)
    signup_page = SignupPage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Verify that home page is visible successfully"):
        assert page.title() == "Automation Exercise"

    with allure.step("Click on Signup / Login button"):
        home_page.click_signup_login()

    with allure.step("Verify New User Signup! is visible"):
        assert signup_page.is_new_user_signup_visible()

    with allure.step("Enter name and already registered email address"):
        signup_page.fill_signup_form("Test User", registered_user["email"])

    with allure.step("Click Signup button"):
        signup_page.click_signup()

    with allure.step("Verify Email Address already exist! is visible"):
        assert signup_page.is_email_exists_error_visible()
