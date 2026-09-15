import allure
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.account_information_page import AccountInformationPage


@allure.title("Test Case 2: Login User with correct email and password")
def test_login_user(page: Page, login_user_for_delete: dict):
    home_page = HomePage(page)
    account_information_page = AccountInformationPage(page)
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
        login_page.fill_login_form(login_user_for_delete["email"], login_user_for_delete["password"])

    with allure.step("Click login button"):
        login_page.click_login()

    with allure.step("Verify that Logged in as username is visible"):
        assert home_page.is_logged_in_as_visible()

    with allure.step("Click Delete Account button"):
        home_page.click_delete_account()

    with allure.step("Verify that ACCOUNT DELETED! is visible"):
        assert account_information_page.is_account_deleted_visible()
