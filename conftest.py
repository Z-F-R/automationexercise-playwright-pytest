import uuid
import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from pages.account_information_page import AccountInformationPage
from pages.login_page import LoginPage
import allure
from pytest import Item
from typing import Any


@pytest.fixture
def page(page: Page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.set_default_timeout(10000)
    page.route(
        "**/*",
        lambda route: (
            route.abort()
            if any(
                domain in route.request.url
                for domain in [
                    "googlesyndication.com",
                    "doubleclick.net",
                    "googleadservices.com",
                ]
            )
            else route.continue_()
        ),
    )
    return page


@pytest.fixture
def registered_user(page: Page):
    home_page = HomePage(page)
    signup_page = SignupPage(page)
    account_information_page = AccountInformationPage(page)
    login_page = LoginPage(page)

    email = f"test_user_{uuid.uuid4().hex[:8]}@example.com"
    password = "TestPassword123!"

    home_page.open()
    home_page.click_signup_login()

    signup_page.fill_signup_form("Test User", email)
    signup_page.click_signup()

    account_information_page.fill_personal_information()
    account_information_page.select_newsletter()
    account_information_page.select_special_offers()
    account_information_page.fill_address_information()
    account_information_page.click_create_account()

    assert account_information_page.is_account_created_visible()

    account_information_page.click_continue()
    home_page.click_logout()

    yield {
        "email": email,
        "password": password,
    }

    page.goto("https://www.automationexercise.com/login")

    login_page.fill_login_form(email, password)
    login_page.click_login()

    home_page.click_delete_account()
    assert home_page.is_account_deleted_visible()


@pytest.fixture
def login_user(page: Page):
    home_page = HomePage(page)
    signup_page = SignupPage(page)
    account_information_page = AccountInformationPage(page)

    email = f"test_user_{uuid.uuid4().hex[:8]}@example.com"
    password = "TestPassword123!"

    home_page.open()
    home_page.click_signup_login()

    signup_page.fill_signup_form("Test User", email)
    signup_page.click_signup()

    account_information_page.fill_personal_information()
    account_information_page.select_newsletter()
    account_information_page.select_special_offers()
    account_information_page.fill_address_information()
    account_information_page.click_create_account()

    assert account_information_page.is_account_created_visible()

    account_information_page.click_continue()
    home_page.click_logout()

    yield {
        "email": email,
        "password": password,
    }


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Any):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            allure.attach(
                page.screenshot(),
                name="Failure screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
