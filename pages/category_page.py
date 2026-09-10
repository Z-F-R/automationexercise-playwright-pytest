from playwright.sync_api import Page, expect


class CategoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.category_heading = page.get_by_text("Category", exact=True)
        self.women_category = page.get_by_text("Women", exact=True)
        self.women_tops = page.locator("#Women a[href='/category_products/2']")
        self.men_category = page.get_by_text("Men", exact=True)
        self.men_tshirts = page.locator("#Men a[href='/category_products/3']")

        self.women_tops_products = page.get_by_text("Women - Tops Products", exact=True)
        self.men_tshirts_products = page.get_by_text(
            "Men - Tshirts Products", exact=True
        )

    def is_categories_visible(self):
        expect(self.category_heading).to_be_visible()
        expect(self.women_category).to_be_visible()
        expect(self.men_category).to_be_visible()
        return True

    def click_women(self):
        self.women_category.click()

    def click_women_tops(self):
        self.women_tops.click()

    def is_women_tops_products_visible(self):
        expect(self.women_tops_products).to_be_visible()
        return True

    def click_men(self):
        self.men_category.click()

    def click_men_tshirts(self):
        self.men_tshirts.click()

    def is_men_tshirts_products_visible(self):
        expect(self.men_tshirts_products).to_be_visible()
        return True
