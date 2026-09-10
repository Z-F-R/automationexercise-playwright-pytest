import allure
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


@allure.title("Test Case 25: Verify Scroll Up using Arrow Button")
def test_verify_scroll_up(page: Page):
    home_page = HomePage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Verify that home page is visible successfully"):
        expect(page).to_have_title("Automation Exercise")

    with allure.step("Scroll down to the bottom of the page"):
        home_page.scroll_to_bottom()

    with allure.step("Verify SUBSCRIPTION is visible"):
        assert home_page.footer.is_subscription_visible()

    with allure.step("Click scroll up arrow"):
        home_page.click_scroll_up()

    with allure.step("Verify page is scrolled up and hero text is visible"):
        assert home_page.is_hero_text_visible()