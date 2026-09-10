# AutomationExercise Playwright Tests

End-to-end test automation framework for the [AutomationExercise](https://www.automationexercise.com/) web application using **Python, Playwright and pytest**.

## Tech Stack

* Python 3.14
* Playwright
* pytest
* pytest-playwright
* pytest-xdist
* Allure Report
* GitHub Actions
* GitHub Pages
* Slack notifications

## Project Structure

```text
automationexercise-playwright-pytest/
├── components/          # Reusable UI components
├── pages/               # Page Object Model classes
├── tests/               # Test cases
├── test_data/           # Test data
├── conftest.py          # Fixtures and test configuration
├── pytest.ini           # pytest configuration
├── requirements.txt     # Python dependencies
└── README.md
```

## Test Coverage

The project automates the test cases provided by AutomationExercise, covering functionality such as:

* User registration and account management
* Login and logout
* Contact Us
* Test Cases page
* Products and product details
* Search
* Product categories and brands
* Shopping cart
* Checkout
* Payment
* Order placement
* Reviews
* Subscription
* Other core e-commerce functionality

## Page Object Model

The framework uses the **Page Object Model (POM)** to separate test logic from UI interaction logic.

Page Objects contain:

* Locators
* Page actions
* Reusable verification methods

Tests contain the business flow and assertions.

## Running Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

Run all tests:

```bash
pytest
```

Run tests in parallel:

```bash
pytest -n auto
```

Run tests with a specific browser:

```bash
pytest --browser chromium
```

```bash
pytest --browser firefox
```

Run a specific test:

```bash
pytest tests/test_case_19_view_cart_brand_products.py
```

## Allure Report

Allure results are generated automatically in the `allure-results` directory.

Generate and open the report locally:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

Failed tests automatically include a screenshot in the Allure report.

## Test Configuration

Common pytest configuration is stored in `pytest.ini`.

The project uses:

* automatic Allure result collection
* automatic cleanup of previous Allure results
* verbose pytest output

## CI/CD

GitHub Actions is used to execute the automated test suite.

The CI pipeline will:

1. Install Python dependencies
2. Install Playwright
3. Run tests in parallel
4. Generate Allure results
5. Publish the Allure report to GitHub Pages

Slack notifications will provide the test execution result and a link to the published report.

## Browsers

The test suite supports:

* Chromium
* Firefox

Browser selection can be controlled from the pytest command line.

## Test Isolation

Tests use pytest fixtures to create and manage test data where required.

User-related tests generate unique email addresses to avoid conflicts between parallel test workers.

## Code Quality

The framework follows:

* Page Object Model
* DRY
* KISS
* YAGNI
* reusable pytest fixtures
* reliable Playwright locators
* parallel-safe test execution where applicable