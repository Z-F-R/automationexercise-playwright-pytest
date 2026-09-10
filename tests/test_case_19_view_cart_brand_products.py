import allure
import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.brand_products_page import BrandProductsPage


@pytest.mark.parametrize("brand", ["Polo", "Madame"])
@allure.title("Test Case 19: View & Cart Brand Products - {brand}")
def test_view_cart_brand_products(page: Page, brand: str):
    home_page = HomePage(page)
    brand_products_page = BrandProductsPage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Click Products button"):
        home_page.click_products()

    with allure.step("Verify that Brands are visible on left side bar"):
        assert brand_products_page.is_brands_visible()

    with allure.step(f"Click on {brand} brand"):
        brand_products_page.click_brand(brand)

    with allure.step(f"Verify {brand} brand page and products"):
        assert brand_products_page.is_brand_products_visible(brand)