from playwright.sync_api import Page, expect


class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.new_user_signup = page.get_by_text("New User Signup!")
        self.name_input = page.locator('[data-qa="signup-name"]')
        self.email_input = page.locator('[data-qa="signup-email"]')
        self.signup_button = page.locator('[data-qa="signup-button"]')
        self.email_exists_error = page.get_by_text(
            "Email Address already exist!", exact=True
        )

    def is_new_user_signup_visible(self):
        expect(self.new_user_signup).to_be_visible()
        return True

    def fill_signup_form(self, name: str, email: str):
        self.name_input.fill(name)
        self.email_input.fill(email)

    def click_signup(self):
        self.signup_button.click()

    def is_email_exists_error_visible(self):
        expect(self.email_exists_error).to_be_visible()
        return True
