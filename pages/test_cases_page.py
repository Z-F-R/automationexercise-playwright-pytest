from playwright.sync_api import Page, expect


class CasesPage:
    def __init__(self, page: Page):
        self.page = page
        self.test_cases_heading = page.locator("h2.title", has_text="Test Cases")

    def is_test_cases_page_visible(self):
        expect(self.test_cases_heading).to_be_visible()
        return True
