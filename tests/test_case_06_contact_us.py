import allure
from playwright.sync_api import Page, expect
from pages.contact_us_page import ContactUsPage
from pages.home_page import HomePage


@allure.title("Test Case 6: Contact Us Form")
def test_contact_us_form(page: Page):
    home_page = HomePage(page)
    contact_us_page = ContactUsPage(page)

    with allure.step("Launch browser"):
        pass

    with allure.step("Navigate to url http://automationexercise.com"):
        home_page.open()

    with allure.step("Verify that home page is visible successfully"):
        assert page.title() == "Automation Exercise"

    with allure.step("Click on Contact Us button"):
        home_page.click_contact_us()

    with allure.step("Verify GET IN TOUCH is visible"):
        assert contact_us_page.is_get_in_touch_visible()

    with allure.step("Enter name, email, subject and message"):
        contact_us_page.fill_contact_form(
            "Test User",
            "test@example.com",
            "Test Subject",
            "This is a test message.",
        )

    with allure.step("Upload file"):
        file_path = "test_file.txt"

        with open(file_path, "w", encoding="utf-8") as file:
            file.write("Automation Exercise test file")

        contact_us_page.upload_file_from_path(file_path)
        page.wait_for_timeout(500)

    with allure.step("Click Submit button"):
        page.once("dialog", lambda dialog: dialog.accept())
        contact_us_page.click_submit()

    with allure.step("Verify success message is visible"):
        expect(contact_us_page.success_message).to_be_visible()

    with allure.step("Click Home button and verify that landed to home page successfully"):
        contact_us_page.click_home()
        expect(page).to_have_url("https://www.automationexercise.com/")