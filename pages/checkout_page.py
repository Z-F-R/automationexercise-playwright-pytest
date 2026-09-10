from playwright.sync_api import Page, expect


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

        self.address_details_heading = page.get_by_text("Address Details", exact=True)
        self.delivery_address = page.locator("#address_delivery")
        self.billing_address = page.locator("#address_invoice")

        self.review_order_heading = page.get_by_text("Review Your Order", exact=True)
        self.order_product = page.locator("#cart_info #product-1")
        self.order_comment = page.locator('textarea[name="message"]')
        self.place_order_button = page.locator("a.check_out[href='/payment']")

    def is_address_details_visible(self):
        expect(self.address_details_heading).to_be_visible()
        expect(self.delivery_address).to_be_visible()
        expect(self.billing_address).to_be_visible()
        return True

    def is_review_order_visible(self):
        expect(self.review_order_heading).to_be_visible()
        expect(self.order_product).to_be_visible()
        return True

    def place_order(self, comment):
        self.order_comment.fill(comment)
        self.place_order_button.click()

    def verify_addresses(self):
        for address in [self.delivery_address, self.billing_address]:
            expect(address).to_contain_text("Test User")
            expect(address).to_contain_text("Test Company")
            expect(address).to_contain_text("Test Address 123")
            expect(address).to_contain_text("Apartment 4")
            expect(address).to_contain_text("Ontario")
            expect(address).to_contain_text("Toronto")
            expect(address).to_contain_text("12345")
            expect(address).to_contain_text("1234567890")