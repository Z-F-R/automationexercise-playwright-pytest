from playwright.sync_api import Page, expect


class AccountInformationPage:
    def __init__(self, page: Page):
        self.page = page
        self.account_information = page.get_by_role(
            "heading", name="Enter Account Information"
        )
        self.title_mr = page.locator("#id_gender1")
        self.password_input = page.locator('[data-qa="password"]')
        self.days_select = page.locator('[data-qa="days"]')
        self.months_select = page.locator('[data-qa="months"]')
        self.years_select = page.locator('[data-qa="years"]')
        self.newsletter_checkbox = page.locator("#newsletter")
        self.offers_checkbox = page.locator("#optin")
        self.first_name_input = page.locator('[data-qa="first_name"]')
        self.last_name_input = page.locator('[data-qa="last_name"]')
        self.company_input = page.locator('[data-qa="company"]')
        self.address_input = page.locator('[data-qa="address"]')
        self.address2_input = page.locator('[data-qa="address2"]')
        self.country_select = page.locator('[data-qa="country"]')
        self.state_input = page.locator('[data-qa="state"]')
        self.city_input = page.locator('[data-qa="city"]')
        self.zipcode_input = page.locator('[data-qa="zipcode"]')
        self.mobile_number_input = page.locator('[data-qa="mobile_number"]')
        self.create_account_button = page.locator('[data-qa="create-account"]')
        self.account_created = page.get_by_role("heading", name="Account Created!")
        self.continue_button = page.locator('[data-qa="continue-button"]')
        self.account_deleted = page.get_by_role("heading", name="Account Deleted!")

    def is_account_information_visible(self):
        expect(self.account_information).to_be_visible()
        return True

    def fill_personal_information(self):
        self.title_mr.check()
        self.password_input.fill("TestPassword123!")
        self.days_select.select_option("10")
        self.months_select.select_option("5")
        self.years_select.select_option("1995")

    def select_newsletter(self):
        self.newsletter_checkbox.check()

    def select_special_offers(self):
        self.offers_checkbox.check()

    def fill_address_information(self):
        self.first_name_input.fill("Test")
        self.last_name_input.fill("User")
        self.company_input.fill("Test Company")
        self.address_input.fill("Test Address 123")
        self.address2_input.fill("Apartment 4")
        self.country_select.select_option("Canada")
        self.state_input.fill("Ontario")
        self.city_input.fill("Toronto")
        self.zipcode_input.fill("12345")
        self.mobile_number_input.fill("1234567890")

    def click_create_account(self):
        self.create_account_button.click()

    def is_account_created_visible(self):
        expect(self.account_created).to_be_visible()
        return True

    def click_continue(self):
        self.continue_button.click()

    def is_account_deleted_visible(self):
        expect(self.account_deleted).to_be_visible()
        return True