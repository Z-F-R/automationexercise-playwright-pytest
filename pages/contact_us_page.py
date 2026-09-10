from playwright.sync_api import Page, expect


class ContactUsPage:
    def __init__(self, page: Page):
        self.page = page

        self.get_in_touch = page.get_by_role("heading", name="Get In Touch", exact=True)
        self.name_input = page.locator('[data-qa="name"]')
        self.email_input = page.locator('[data-qa="email"]')
        self.subject_input = page.locator('[data-qa="subject"]')
        self.message_input = page.locator('[data-qa="message"]')
        self.upload_file = page.locator('input[type="file"][name="upload_file"]')
        self.submit_button = page.locator('[data-qa="submit-button"]')
        self.success_message = page.locator(
            "#contact-page .contact-form .status.alert-success"
        )
        self.home_button = page.locator('#form-section a[href="/"]')

    def is_get_in_touch_visible(self):
        expect(self.get_in_touch).to_be_visible()
        return True

    def fill_contact_form(self, name: str, email: str, subject: str, message: str):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.subject_input.fill(subject)
        self.message_input.fill(message)

    def upload_file_from_path(self, file_path: str):
        self.upload_file.set_input_files(file_path)

    def click_submit(self):
        self.submit_button.click()

    def is_success_message_visible(self):
        expect(self.success_message).to_be_visible()
        return True

    def click_home(self):
        self.home_button.click(force=True)
