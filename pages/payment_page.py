from playwright.sync_api import Page, expect


class PaymentPage:
    def __init__(self, page: Page):
        self.page = page

        self.payment_heading = page.get_by_text("Payment", exact=True)
        self.name_on_card = page.locator('[data-qa="name-on-card"]')
        self.card_number = page.locator('[data-qa="card-number"]')
        self.cvc = page.locator('[data-qa="cvc"]')
        self.expiry_month = page.locator('[data-qa="expiry-month"]')
        self.expiry_year = page.locator('[data-qa="expiry-year"]')
        self.pay_button = page.locator('[data-qa="pay-button"]')

    def is_payment_page_visible(self):
        expect(self.payment_heading).to_be_visible()
        return True

    def fill_payment_details(self):
        self.name_on_card.fill("Test User")
        self.card_number.fill("4111111111111111")
        self.cvc.fill("311")
        self.expiry_month.fill("12")
        self.expiry_year.fill("2030")

    def pay_and_confirm_order(self):
        self.pay_button.click()