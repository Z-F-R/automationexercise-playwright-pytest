from playwright.sync_api import Page, expect


class ProductDetailPage:
    def __init__(self, page: Page):
        self.page = page

        self.product_information = page.locator(".product-information")
        self.product_name = self.product_information.locator("h2")
        self.category = self.product_information.get_by_text("Category:")
        self.price = self.product_information.locator("span > span").filter(
            has_text="Rs."
        )
        self.availability = self.product_information.get_by_text("Availability:")
        self.condition = self.product_information.get_by_text("Condition:")
        self.brand = self.product_information.get_by_text("Brand:")
        self.quantity_input = self.product_information.locator("#quantity")
        self.add_to_cart_button = self.product_information.locator("button.cart")
        self.added_to_cart_message = page.get_by_text(
            "Your product has been added to cart.", exact=True
        )
        self.continue_shopping_button = page.get_by_role(
            "button", name="Continue Shopping"
        )
        self.write_review = page.get_by_text("Write Your Review", exact=True)
        self.review_name = page.locator("#name")
        self.review_email = page.locator("#email")
        self.review_text = page.locator("#review")
        self.submit_review_button = page.locator("#button-review")
        self.review_success = page.get_by_text("Thank you for your review.", exact=True)

    def is_product_details_visible(self):
        expect(self.product_name).to_be_visible()
        expect(self.category).to_be_visible()
        expect(self.price).to_be_visible()
        expect(self.availability).to_be_visible()
        expect(self.condition).to_be_visible()
        expect(self.brand).to_be_visible()
        return True

    def set_quantity(self, quantity):
        self.quantity_input.fill(str(quantity))

    def add_to_cart(self):
        self.add_to_cart_button.click()
        expect(self.added_to_cart_message).to_be_visible()
        self.continue_shopping_button.click()

    def is_write_review_visible(self):
        expect(self.write_review).to_be_visible()
        return True

    def submit_review(self, name, email, review):
        self.review_name.fill(name)
        self.review_email.fill(email)
        self.review_text.fill(review)
        self.submit_review_button.click()

    def is_review_success_visible(self):
        expect(self.review_success).to_be_visible()
        return True