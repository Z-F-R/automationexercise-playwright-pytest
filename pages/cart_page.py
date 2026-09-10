from playwright.sync_api import Page, expect
from pages.components.footer import Footer


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.footer = Footer(page)
        self.first_product = page.locator("#product-1")
        self.second_product = page.locator("#product-2")
        self.proceed_to_checkout_button = page.locator("a.check_out")
        self.checkout_modal = page.locator("#checkoutModal")
        self.register_login_link = self.checkout_modal.locator("a[href='/login']")
        self.first_product_remove_button = self.first_product.locator(".cart_quantity_delete")
        self.cart_table = page.locator("#cart_info table")

    def is_products_visible(self):
        expect(self.first_product).to_be_visible()
        expect(self.second_product).to_be_visible()
        return True

    def verify_product_details(self, products):
        for product in products:
            product_row = self.page.locator(f"#product-{product['id']}")

            expect(product_row.locator(".cart_price p")).to_have_text(product["price"])
            expect(product_row.locator(".cart_quantity button")).to_have_text(
                product["quantity"]
            )
            expect(product_row.locator(".cart_total_price")).to_have_text(product["total"])

    def verify_product_quantity(self, product_id, quantity):
        product_row = self.page.locator(f"#product-{product_id}")
        expect(product_row.locator(".cart_quantity button")).to_have_text(str(quantity))

    def click_proceed_to_checkout(self):
        expect(self.proceed_to_checkout_button).to_be_visible()
        self.proceed_to_checkout_button.click()

    def click_register_login(self):
        expect(self.checkout_modal).to_be_visible()
        self.register_login_link.click()

    def remove_first_product(self):
        self.first_product_remove_button.click()

    def is_cart_products_visible(self):
        expect(self.cart_table).to_be_visible()
        return True