from playwright.sync_api import Page, expect


class OrderPlacedPage:
    def __init__(self, page: Page):
        self.page = page
        self.order_placed_heading = page.get_by_text("Order Placed!", exact=True)
        self.order_confirmed_message = page.get_by_text(
            "Congratulations! Your order has been confirmed!", exact=True
        )
        self.download_invoice_button = page.get_by_text("Download Invoice", exact=True)
        self.continue_button = page.get_by_text("Continue", exact=True)

    def is_order_placed_visible(self):
        expect(self.order_placed_heading).to_be_visible()
        expect(self.order_confirmed_message).to_be_visible()
        return True

    def download_invoice(self):
        with self.page.expect_download() as download_info:
            self.download_invoice_button.click()

        download = download_info.value
        assert download.suggested_filename.endswith(".txt")

    def click_continue(self):
        self.continue_button.click()