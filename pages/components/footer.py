from playwright.sync_api import Page, expect


class Footer:
    def __init__(self, page: Page):
        self.page = page

        self.subscription_heading = page.get_by_text("Subscription", exact=True)
        self.subscription_email = page.locator("#susbscribe_email")
        self.subscription_button = page.locator("#subscribe")
        self.subscription_success = page.get_by_text(
            "You have been successfully subscribed!", exact=True
        )

    def scroll_to_footer(self):
        self.subscription_heading.scroll_into_view_if_needed()

    def is_subscription_visible(self):
        expect(self.subscription_heading).to_be_visible()
        return True

    def subscribe(self, email):
        self.subscription_email.fill(email)
        self.subscription_button.click()

    def is_subscription_success_visible(self):
        expect(self.subscription_success).to_be_visible()
        return True
