import allure
import uuid
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.account_information_page import AccountInformationPage


@allure.title("Test Case 1: Register User")
def test_register_user(page: Page):
    home_page = HomePage(page)
    signup_page = SignupPage(page)
    account_information_page = AccountInformationPage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Verify that home page is visible"):
        assert page.title() == "Automation Exercise"

    with allure.step("Click Signup / Login button"):
        home_page.click_signup_login()

    with allure.step("Verify New User Signup! is visible"):
        assert signup_page.is_new_user_signup_visible()

    with allure.step("Enter name and email address"):
        email = f"test_user_{uuid.uuid4().hex[:8]}@example.com"
        signup_page.fill_signup_form("Test User", email)

    with allure.step("Click Signup button"):
        signup_page.click_signup()

    with allure.step("Verify ENTER ACCOUNT INFORMATION is visible"):
        assert account_information_page.is_account_information_visible()

    with allure.step("Fill Title, Name, Email, Password, Date of birth"):
        account_information_page.fill_personal_information()

    with allure.step("Select newsletter checkbox"):
        account_information_page.select_newsletter()

    with allure.step("Select special offers checkbox"):
        account_information_page.select_special_offers()

    with allure.step(
        "Fill First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number"
    ):
        account_information_page.fill_address_information()

    with allure.step("Click Create Account button"):
        account_information_page.click_create_account()

    with allure.step("Verify ACCOUNT CREATED! is visible"):
        assert account_information_page.is_account_created_visible()

    with allure.step("Click Continue button"):
        account_information_page.click_continue()

    with allure.step("Verify that Logged in as username is visible"):
        assert home_page.is_logged_in_as_visible()

    with allure.step("Click Delete Account button"):
        home_page.click_delete_account()

    with allure.step("Verify ACCOUNT DELETED! is visible and click Continue button"):
        assert home_page.is_account_deleted_visible()
        account_information_page.click_continue()
