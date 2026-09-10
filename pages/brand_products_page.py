from playwright.sync_api import Page, expect


class BrandProductsPage:
    def __init__(self, page: Page):
        self.page = page

        self.brands_heading = page.get_by_text("Brands", exact=True)

    def is_brands_visible(self):
        expect(self.brands_heading).to_be_visible()
        return True

    def click_brand(self, brand: str):
        self.page.locator(f".brands-name a[href='/brand_products/{brand}']").click(force=True)

    def is_brand_products_visible(self, brand: str):
        expect(
            self.page.get_by_text(f"Brand - {brand} Products", exact=True)
        ).to_be_visible()
        return True