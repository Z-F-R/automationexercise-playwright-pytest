import allure
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.category_page import CategoryPage


@allure.title("Test Case 18: View Category Products")
def test_view_category_products(page: Page):
    home_page = HomePage(page)
    category_page = CategoryPage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Verify that categories are visible on left side bar"):
        assert category_page.is_categories_visible()

    with allure.step("Click on Women category"):
        category_page.click_women()

    with allure.step("Click on Tops category under Women"):
        category_page.click_women_tops()

    with allure.step("Verify category page and Women - Tops Products text"):
        assert category_page.is_women_tops_products_visible()

    with allure.step("Click on Men category"):
        category_page.click_men()

    with allure.step("Click on Tshirts category under Men"):
        category_page.click_men_tshirts()

    with allure.step("Verify navigation to Men - Tshirts category"):
        assert category_page.is_men_tshirts_products_visible()
