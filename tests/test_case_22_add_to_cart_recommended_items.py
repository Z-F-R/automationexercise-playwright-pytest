import allure
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.cart_page import CartPage


@allure.title("Test Case 22: Add to Cart from Recommended Items")
def test_add_to_cart_from_recommended_items(page: Page):
    home_page = HomePage(page)
    cart_page = CartPage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Scroll to bottom of page"):
        home_page.scroll_to_recommended_items()

    with allure.step("Verify RECOMMENDED ITEMS are visible"):
        assert home_page.is_recommended_items_visible()

    with allure.step("Click Add To Cart on recommended product"):
        home_page.add_recommended_product_to_cart()

    with allure.step("Click View Cart button"):
        home_page.click_cart()

    with allure.step("Verify product is displayed in cart"):
        assert cart_page.is_cart_products_visible()