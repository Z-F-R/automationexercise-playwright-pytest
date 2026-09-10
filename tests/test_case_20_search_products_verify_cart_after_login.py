import allure
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage


@allure.title("Test Case 20: Search Products and Verify Cart After Login")
def test_search_products_verify_cart_after_login(page: Page, login_user):
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    login_page = LoginPage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Click Products button"):
        home_page.click_products()

    with allure.step("Verify ALL PRODUCTS page is visible"):
        assert products_page.is_all_products_visible()

    with allure.step("Search for product"):
        products_page.search_product("Top")

    with allure.step("Verify SEARCHED PRODUCTS is visible"):
        assert products_page.is_searched_products_visible()

    with allure.step("Verify search results are visible"):
        assert products_page.is_search_results_visible()

    with allure.step("Add all searched products to cart"):
        products_page.add_all_search_results_to_cart()

    with allure.step("Click Cart button"):
        home_page.click_cart()

    with allure.step("Verify searched products are visible in cart"):
        assert cart_page.is_cart_products_visible()

    with allure.step("Click Signup / Login button"):
        home_page.click_signup_login()

    with allure.step("Login with registered user"):
        login_page.fill_login_form(login_user["email"], login_user["password"])
        login_page.click_login()

    with allure.step("Go to Cart page again"):
        home_page.click_cart()

    with allure.step("Verify products are visible in cart after login"):
        assert cart_page.is_cart_products_visible()