import allure
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.products_page import ProductsPage


@allure.title("Test Case 9: Search Product")
def test_search_product(page: Page):
    home_page = HomePage(page)
    products_page = ProductsPage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Verify that home page is visible successfully"):
        expect(page).to_have_title("Automation Exercise")

    with allure.step("Click on Products button"):
        home_page.click_products()

    with allure.step("Verify user is navigated to ALL PRODUCTS page successfully"):
        expect(page).to_have_url("https://www.automationexercise.com/products")
        assert products_page.is_all_products_visible()

    with allure.step("Enter product name in search input and click search button"):
        products_page.search_product("Blue Top")

    with allure.step("Verify SEARCHED PRODUCTS is visible"):
        assert products_page.is_searched_products_visible()

    with allure.step("Verify all the products related to search are visible"):
        assert products_page.is_search_results_visible()
