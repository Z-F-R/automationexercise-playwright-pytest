import uuid
import allure
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.signup_page import SignupPage
from pages.account_information_page import AccountInformationPage
from pages.checkout_page import CheckoutPage


@allure.title("Test Case 23: Verify Address Details in Checkout")
def test_verify_address_details_checkout(page: Page):
    home_page = HomePage(page)
    signup_page = SignupPage(page)
    account_information_page = AccountInformationPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Verify that home page is visible successfully"):
        expect(page).to_have_title("Automation Exercise")

    with allure.step("Click Signup / Login button"):
        home_page.click_signup_login()

    with allure.step("Fill all details in Signup and create account"):
        signup_page.fill_signup_form(
            "Test User",
            f"test_user_{uuid.uuid4().hex[:8]}@example.com",
        )
        signup_page.click_signup()

        account_information_page.fill_personal_information()
        account_information_page.select_newsletter()
        account_information_page.select_special_offers()
        account_information_page.fill_address_information()
        account_information_page.click_create_account()

    with allure.step("Verify ACCOUNT CREATED and click Continue"):
        assert account_information_page.is_account_created_visible()
        account_information_page.click_continue()

    with allure.step("Verify Logged in as username"):
        assert home_page.is_logged_in_as_visible()

    with allure.step("Add products to cart"):
        home_page.click_products()
        products_page.add_first_product_to_cart()
        products_page.click_continue_shopping()

    with allure.step("Click Cart button"):
        home_page.click_cart()

    with allure.step("Verify that cart page is displayed"):
        expect(page).to_have_url("https://www.automationexercise.com/view_cart")

    with allure.step("Click Proceed To Checkout"):
        cart_page.click_proceed_to_checkout()

    with allure.step("Verify delivery and billing addresses"):
        checkout_page.verify_addresses()

    with allure.step("Click Delete Account"):
        home_page.click_delete_account()

    with allure.step("Verify ACCOUNT DELETED and click Continue"):
        assert account_information_page.is_account_deleted_visible()
        account_information_page.click_continue()