import allure
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


@allure.title("Test Case 12: Add Products in Cart")
def test_add_products_in_cart(page: Page):
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Verify that home page is visible successfully"):
        expect(page).to_have_title("Automation Exercise")

    with allure.step("Click Products button"):
        home_page.click_products()

    with allure.step("Hover over first product and click Add to cart"):
        products_page.add_first_product_to_cart()

    with allure.step("Click Continue Shopping button"):
        products_page.click_continue_shopping()

    with allure.step("Hover over second product and click Add to cart"):
        products_page.add_second_product_to_cart()

    with allure.step("Click View Cart button"):
        home_page.click_cart()

    with allure.step("Verify both products are added to Cart"):
        assert cart_page.is_products_visible()

    with allure.step("Verify their prices, quantity and total price"):
        cart_page.verify_product_details(
            [
                {"id": 1, "price": "Rs. 500", "quantity": "1", "total": "Rs. 500"},
                {"id": 2, "price": "Rs. 400", "quantity": "1", "total": "Rs. 400"},
            ]
        )