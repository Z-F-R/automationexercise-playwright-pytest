import allure
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage


@allure.title("Test Case 8: Verify All Products and product detail page")
def test_products_and_product_detail(page: Page):
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    product_detail_page = ProductDetailPage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Verify that home page is visible successfully"):
        expect(page).to_have_title("Automation Exercise")

    with allure.step("Click on Products button"):
        home_page.click_products()

    with allure.step("Verify user is navigated to ALL PRODUCTS page successfully"):
        expect(page).to_have_url("https://www.automationexercise.com/products")
        assert products_page.is_all_products_visible()

    with allure.step("Verify that products list is visible"):
        assert products_page.is_products_list_visible()

    with allure.step("Click on View Product of first product"):
        products_page.click_first_view_product()

    with allure.step("Verify user is landed to product detail page"):
        expect(page).to_have_url("https://www.automationexercise.com/product_details/1")

    with allure.step(
        "Verify product name, category, price, availability, condition and brand"
    ):
        product_detail_page.is_product_details_visible()
