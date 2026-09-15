from playwright.sync_api import Page, expect


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.all_products_heading = page.get_by_text("All Products", exact=True)
        self.products_list = page.locator(".features_items")
        self.first_view_product = page.locator("a[href^='/product_details/']").first
        self.search_input = page.locator("#search_product")
        self.search_button = page.locator("#submit_search")
        self.searched_products_heading = page.get_by_text(
            "Searched Products", exact=True
        )
        self.first_product = page.locator(".product-image-wrapper").nth(0)
        self.second_product = page.locator(".product-image-wrapper").nth(1)
        self.first_add_to_cart = self.first_product.locator("a.add-to-cart").first
        self.second_add_to_cart = self.second_product.locator("a.add-to-cart").first
        self.continue_shopping_button = page.get_by_role(
            "button", name="Continue Shopping"
        )
        self.search_results = self.page.locator(".product-image-wrapper")

    def is_all_products_visible(self):
        expect(self.all_products_heading).to_be_visible()
        return True

    def is_products_list_visible(self):
        expect(self.products_list).to_be_visible()
        return True

    def click_first_view_product(self):
        self.first_view_product.click()

    def search_product(self, product_name):
        self.search_input.fill(product_name)
        self.search_button.click()

    def is_searched_products_visible(self):
        expect(self.searched_products_heading).to_be_visible()
        return True

    def is_search_results_visible(self):
        expect(self.products_list).to_be_visible()
        return True

    def add_first_product_to_cart(self):
        expect(self.first_product).to_be_visible()
        self.first_product.scroll_into_view_if_needed()
        self.first_product.hover()
        self.first_add_to_cart.click()

    def add_second_product_to_cart(self):
        expect(self.second_product).to_be_visible()
        self.second_product.scroll_into_view_if_needed()
        self.second_product.hover()
        self.second_add_to_cart.click()

    def click_continue_shopping(self):
        self.continue_shopping_button.click()
        expect(self.page.locator("#cartModal")).to_be_hidden()

    def add_all_search_results_to_cart(self):
        for product in self.search_results.all():
            expect(product).to_be_visible()
            product.scroll_into_view_if_needed()
            product.hover()
            product.locator("a.add-to-cart").first.click()
            self.continue_shopping_button.click()