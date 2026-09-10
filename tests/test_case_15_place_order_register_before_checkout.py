import uuid
import allure
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.signup_page import SignupPage
from pages.account_information_page import AccountInformationPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.order_placed_page import OrderPlacedPage


@allure.title("Test Case 15: Place Order - Register before Checkout")
def test_place_order_register_before_checkout(page: Page):
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    signup_page = SignupPage(page)
    account_information_page = AccountInformationPage(page)
    checkout_page = CheckoutPage(page)
    payment_page = PaymentPage(page)
    order_placed_page = OrderPlacedPage(page)

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

    with allure.step("Verify ACCOUNT CREATED and Continue"):
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

    with allure.step("Verify Address Details and Review Your Order"):
        assert checkout_page.is_address_details_visible()
        assert checkout_page.is_review_order_visible()

    with allure.step("Enter description in comment and Place Order"):
        checkout_page.place_order("Please deliver the order as soon as possible.")

    with allure.step("Enter payment details"):
        payment_page.fill_payment_details()

    with allure.step("Pay and Confirm Order"):
        payment_page.pay_and_confirm_order()

    with allure.step("Verify success message"):
        assert order_placed_page.is_order_placed_visible()

    with allure.step("Delete Account"):
        home_page.click_delete_account()

    with allure.step("Verify Account Deleted and Continue"):
        assert account_information_page.is_account_deleted_visible()
        account_information_page.click_continue()
