import allure
from playwright.sync_api import Page, expect
from pages.account_information_page import AccountInformationPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.order_placed_page import OrderPlacedPage


@allure.title("Test Case 16: Place Order - Login before Checkout")
def test_place_order_login_before_checkout(page: Page, login_user_for_delete):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    payment_page = PaymentPage(page)
    order_placed_page = OrderPlacedPage(page)
    account_information_page = AccountInformationPage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Verify that home page is visible successfully"):
        expect(page).to_have_title("Automation Exercise")

    with allure.step("Click Signup / Login button"):
        home_page.click_signup_login()

    with allure.step("Fill email, password and click Login button"):
        login_page.fill_login_form(login_user_for_delete["email"], login_user_for_delete["password"])
        login_page.click_login()

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
