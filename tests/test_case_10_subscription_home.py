import allure
from playwright.sync_api import Page, expect
from pages.home_page import HomePage


@allure.title("Test Case 10: Verify Subscription in home page")
def test_subscription_home(page: Page):
    home_page = HomePage(page)

    with allure.step("Open AutomationExercise home page"):
        home_page.open()

    with allure.step("Verify that home page is visible successfully"):
        expect(page).to_have_title("Automation Exercise")

    with allure.step("Scroll down to footer"):
        home_page.footer.scroll_to_footer()

    with allure.step("Verify text 'SUBSCRIPTION'"):
        assert home_page.footer.is_subscription_visible()

    with allure.step("Enter email address in input and click arrow button"):
        home_page.footer.subscribe("test_subscription@example.com")

    with allure.step(
        "Verify success message 'You have been successfully subscribed!' is visible"
    ):
        assert home_page.footer.is_subscription_success_visible()
