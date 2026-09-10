import allure
from playwright.sync_api import Page, expect

from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage


@allure.title("Test Case 21: Add Review on Product")
def test_add_review_on_product(page: Page):
    home_page = HomePage(page)
    products_page = ProductsPage(page)
    product_detail_page = ProductDetailPage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Click Products button"):
        home_page.click_products()

    with allure.step("Verify ALL PRODUCTS page is visible"):
        assert products_page.is_all_products_visible()

    with allure.step("Click View Product button"):
        products_page.click_first_view_product()

    with allure.step("Verify Write Your Review is visible"):
        assert product_detail_page.is_write_review_visible()

    with allure.step("Enter name, email and review"):
        product_detail_page.submit_review(
            "Test User",
            "testuser@example.com",
            "This is a great product.",
        )

    with allure.step("Verify review success message"):
        assert product_detail_page.is_review_success_visible()