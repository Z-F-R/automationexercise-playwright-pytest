import allure
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@allure.title("Test Case 17: Remove Products From Cart")
def test_remove_products_from_cart(page: Page):
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Verify that home page is visible successfully"):
        expect(page).to_have_title("Automation Exercise")

    with allure.step("Add products to cart"):
        home_page.click_products()
        products_page.add_first_product_to_cart()
        products_page.click_continue_shopping()

    with allure.step("Click Cart button"):
        home_page.click_cart()

    with allure.step("Verify that cart page is displayed"):
        expect(page).to_have_url("https://www.automationexercise.com/view_cart")

    with allure.step("Click X button corresponding to particular product"):
        cart_page.remove_first_product()

    with allure.step("Verify that product is removed from the cart"):
        expect(cart_page.first_product).not_to_be_visible()
