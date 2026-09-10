import allure
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.cart_page import CartPage


@allure.title("Test Case 11: Verify Subscription in Cart page")
def test_subscription_cart(page: Page):
    home_page = HomePage(page)
    cart_page = CartPage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Verify that home page is visible successfully"):
        expect(page).to_have_title("Automation Exercise")

    with allure.step("Click Cart button"):
        home_page.click_cart()

    with allure.step("Scroll down to footer"):
        cart_page.footer.scroll_to_footer()

    with allure.step("Verify text 'SUBSCRIPTION'"):
        assert cart_page.footer.is_subscription_visible()

    with allure.step("Enter email address in input and click arrow button"):
        cart_page.footer.subscribe("test_subscription_cart@example.com")

    with allure.step(
        "Verify success message 'You have been successfully subscribed!' is visible"
    ):
        assert cart_page.footer.is_subscription_success_visible()
