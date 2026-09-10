import allure
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage


@allure.title("Test Case 13: Verify Product quantity in Cart")
def test_product_quantity_in_cart(page: Page):
    home_page = HomePage(page)
    product_detail_page = ProductDetailPage(page)
    cart_page = CartPage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Verify that home page is visible successfully"):
        expect(page).to_have_title("Automation Exercise")

    with allure.step("Click View Product for any product"):
        home_page.click_first_view_product()

    with allure.step("Verify product detail is opened"):
        assert product_detail_page.is_product_details_visible()

    with allure.step("Increase quantity to 4"):
        product_detail_page.set_quantity(4)

    with allure.step("Click Add to cart button"):
        product_detail_page.add_to_cart()

    with allure.step("Click View Cart button"):
        home_page.click_cart()

    with allure.step("Verify that product is displayed in cart with exact quantity"):
        cart_page.verify_product_quantity(product_id=1, quantity=4)
