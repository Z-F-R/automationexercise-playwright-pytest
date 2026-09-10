from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_to_account = page.get_by_text("Login to your account", exact=True)
        self.email_input = self.page.locator('[data-qa="login-email"]')
        self.password_input = self.page.locator('[data-qa="login-password"]')
        self.login_button = self.page.locator('[data-qa="login-button"]')
        self.login_error = page.get_by_text(
            "Your email or password is incorrect!", exact=True
        )

    def is_login_to_account_visible(self):
        expect(self.login_to_account).to_be_visible()
        return True

    def fill_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)

    def click_login(self):
        self.login_button.click()

    def is_login_error_visible(self):
        expect(self.login_error).to_be_visible()
        return True
