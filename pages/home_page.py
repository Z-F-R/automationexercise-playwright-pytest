from playwright.sync_api import Page, expect
from pages.components.footer import Footer


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.footer = Footer(page)
        self.signup_login_button = page.get_by_text("Signup / Login")
        self.logged_in_as = page.get_by_text("Logged in as", exact=False)
        self.delete_account_button = page.locator('a[href="/delete_account"]')
        self.account_deleted = page.get_by_role("heading", name="Account Deleted!")
        self.logout_button = page.locator('a[href="/logout"]')
        self.contact_us_button = page.locator('a[href="/contact_us"]')
        self.shop_menu = page.locator(".shop-menu")
        self.test_cases_button = self.shop_menu.locator("a[href='/test_cases']")
        self.products_button = page.locator(".shop-menu a[href='/products']")
        self.cart_button = page.locator(".shop-menu a[href='/view_cart']")
        self.first_view_product = page.locator("a[href^='/product_details/']").first
        self.recommended_items = page.locator(".recommended_items")
        self.recommended_items_heading = self.recommended_items.locator("h2").first
        self.recommended_add_to_cart = page.locator(
            '.recommended_items a[data-product-id="4"]'
        )
        self.continue_shopping_button = page.get_by_role(
            "button", name="Continue Shopping"
        )
        self.scroll_up_button = page.locator("#scrollUp")
        self.hero_text = page.get_by_role(
            "heading",
            name="Full-Fledged practice website for Automation Engineers",
        ).first

    def open(self):
        self.page.goto("https://www.automationexercise.com/")

    def click_signup_login(self):
        self.signup_login_button.click()

    def is_logged_in_as_visible(self):
        expect(self.logged_in_as).to_be_visible()
        return True

    def click_delete_account(self):
        self.delete_account_button.click()

    def is_account_deleted_visible(self):
        expect(self.account_deleted).to_be_visible()
        return True

    def click_logout(self):
        self.logout_button.click()

    def click_contact_us(self):
        self.contact_us_button.click()

    def click_test_cases(self):
        self.test_cases_button.click()

    def click_products(self):
        self.products_button.click()

    def click_cart(self):
        self.cart_button.click()

    def click_first_view_product(self):
        self.first_view_product.click()

    def scroll_to_recommended_items(self):
        self.recommended_items.scroll_into_view_if_needed()

    def is_recommended_items_visible(self):
        expect(self.recommended_items_heading).to_be_visible()
        return True

    def add_recommended_product_to_cart(self):
        self.recommended_add_to_cart.click()
        self.continue_shopping_button.click()

    def scroll_to_bottom(self):
        self.page.locator("footer").scroll_into_view_if_needed()

    def click_scroll_up(self):
        self.scroll_up_button.click()

    def is_hero_text_visible(self):
        expect(self.hero_text).to_be_visible()
        return True

    def scroll_to_top(self):
        self.page.evaluate("window.scrollTo(0, 0)")