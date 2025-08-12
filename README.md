# 🧪 Test Automation Framework Summary

This is a Python-based automation framework using Selenium WebDriver for browser testing and Pytest for running test cases. It follows the Page Object Model (POM) design and supports data-driven testing using CSV files. I’ve added Allure for better reporting and connected the project to GitHub Actions for automatic test runs. The framework also covers API testing using requests and responses, handles real-time UI bugs, takes screenshots on failure, and retries flaky tests when needed.Actively seeking QA opportunities. ** Reach out if you’re hiring or know someone who is. ** 

---

## 📅 Day-by-Day Progress

### 📘 Day 1: Introduction to Testing + First Selenium Script

**Manual Testing Theory Covered:**
- Test Cases vs Test Scenarios
- Types of Testing: Functional, Regression, Sanity, Smoke, UAT, Exploratory
- SDLC and STLC lifecycle understanding
- Bug Life Cycle and Defect Reporting

**Selenium Practice:**
- 🔗 Launched `python.org` using `driver.get()`
- 🔍 Performed a search using `By.NAME` and `send_keys()`
- ✅ Asserted page title with `assert`
- 🔁 Clicked buttons using `click()`
- 🦹 Closed browser using `driver.quit()`

---

### 🔐 Day 2: Login Flow Automation on SauceDemo

- Used `By.ID` to locate login fields
- Tested valid and invalid login scenarios
- Captured error messages for failures
- Handled exceptions using `try-except-finally`
- Implemented assertions for validating login success/failure

---

### 🧭 Day 3: XPath, Waits, and Reusable Functions

- ⏱ Replaced `time.sleep()` with `WebDriverWait` & `ExpectedConditions`
- Mastered XPath functions: `contains()`, `*`, and text-based search
- Created reusable functions like `perform_login()` and `check_error()`
- Introduced exception handling with `TimeoutException`
- Modularized test logic for clarity and reusability

---

### 📦 Day 4: Page Object Model (POM) & Test Structuring

- Implemented **Page Object Model (POM)** for scalable code
- Split code into:
  - `login_pom.py`: with methods like `load()`, `login()`, `get_error()`
  - `test_login.py`: for test cases using the POM class
- Used assertions to validate test outcomes
- Managed errors with `WebDriverException`, `TimeoutException`, and `AssertionError`
- Wrapped logic in `try-except-finally` for robust execution and browser cleanup

---

### 📂 Day 5: CSV-Driven Testing + Pytest Integration

- Read login test data from external `login_details.csv`
- Used `csv.DictReader()` for structured data handling
- Sanitized input with `.strip()` to avoid parsing issues
- Introduced **Pytest** framework for test automation
- Used `@pytest.mark.parametrize()` to feed test data dynamically from CSV
- Ran test cases directly using `pytest`

---
### 📂 Day 6 - Progress Summary

- Integrated `pytest.fixture` for WebDriver setup and teardown.
- Implemented **Product POM** with:
  - Single product add to cart 
  - Cart icon click
  - Basic error handling
- Combined Login + Product POM test (end-to-end)
- Added clean assertions for product add/cart
---
### 📅 Day 7 - Summary
- Read multiple product IDs from CSV and added them dynamically.
- Introduced time.sleep() delays for better step visibility.
- Added product title check (details page navigation + back button).
- Implemented single product removal from cart.
- No changes in login flow.
---
### 📅 Day 8 - Automation Progress
- Today, I extended my test automation framework by adding support for the checkout flow using a dedicated Page Object Model (POM) class. This class handles entering user details (First Name, Last Name, Zip Code) and continues the checkout process. I also refactored the product removal functionality to support multiple removals via CSV input, mirroring how products are added/removed.

- Additionally, I implemented robust error handling for all major test flows — including per-item screenshot capture in case of failure. This adds traceability and debugging ease to the test suite.
---
### 📅 Day 9 - Automation Progress
- Completed end-to-end checkout flow on SauceDemo using POM structure.
- Included cart cancel, checkout cancel, final order confirmation, and go-to-cart revisit.
- Added robust error handling, screenshots on failure, and assertions to verify dynamic user input.
- Used pytest to execute and validate flows with clear test separation.

- ___Backend (API Testing using requests + pytest):
- Introduced API automation with reqres.in, focusing on:
- POST login with various payloads and status expectations.
- GET single user and all users, with param checks.
- Used API key authentication via headers.
- Validated response structures, like token, data, and error.
- Wrote parameterized tests with meaningful assertions.

---
###  📅 Day 10 - Automation Progress
- POST /login: Tested valid, missing, and empty credentials
- GET /users/{id}: Fetched user info; handled 200 & 404 cases
- GET /users: Fetched all users and validated response
- DELETE /users/{id}: Verified auth-based behavior (with/without API key)
---
### 📅 Day 11 - Summary
- Created your own MockAPI project simulating a users and products resource. (It's free of cost for maximum 2 resource creation).
- Designed and tested the following HTTP methods:
    - Single product add to cart 
    - GET /users – Retrieve all users.
    - GET /users/:id – Retrieve a single user by ID.
    - POST /users – Create a new user.
    - DELETE /users/:id – Delete a specific user.
---
### 📅 Day 12 - Summary
- Migrated API testing script for `reqres.in` to a separate module
- Designed and tested a mock product API using CSV-driven testing
- Verified all test cases manually in Postman before automating
- Created and structured CSV test data with the following methods:
  - `GET`, `POST`, `PATCH`, `DELETE`, `HEAD`.
---
### 📅 Day 13 to day 16 - Summary
- Experimented button's behaviour on `demoqa.com`.
- implemeted `@pytest.mark.smoke`, and it was unrecognisable then solved the issue by introduicng `pytest.ini`. (config file).
- Implemented **flaky test handling** using `@pytest.mark.flaky`.
- Resolved test instability caused by dynamic ads using:
  - Custom wait strategies
  - Retry logic via `pytest-rerunfailures`
- Installed and configured **Allure Reporting**:
  - Added Allure decorators:`@allure.title`, `@allure.severity`, `@allure.description`, etc,.
---
### 📅 Day 17 - Summary
- Implemeted **Allure reporting** on other test cases.
- Wrote root `pytest.ini` config.
- Generated `allure serve <filename>` reports.
- Had a look on what i wrote from the beginning.

---
### 📅 Day 18 - Summary
- Created .github/workflows/qa_tests.yml
- Setup CI to:
    - Checkout the repo
    - Install Python 3.11 and dependencies
- Run pytest for:
  - Tests/ folder
  - qa_allure_and_github/ folder
- Generate Allure result folders (--alluredir=...)
- Upload test artifacts using actions/upload-artifact@v4.

---
### 📅 11/08/2025 - Summary
- Wrote test cases.
- Wrote `conftest.py`, which had common fixture for Ui tests.

---
## 🧠 Skills Covered So Far

- ✅ Selenium WebDriver (Chrome)
- ✅ Element locating: `By.ID`, `By.NAME`, `By.XPATH`
- ✅ XPath: `contains()`, `text()`, wildcards
- ✅ Waits: `WebDriverWait` vs `time.sleep`
- ✅ Exception Handling: `TimeoutException`, `WebDriverException`, generic `Exception`
- ✅ Assertions for validation
- ✅ Reusable and modular functions
- ✅ Page Object Model (POM) (for login)
- ✅ CSV Data-Driven Testing (for login)
- ✅ Pytest basics: test discovery, assertions, parameterization(`@pytest.mark.parametrize`)
- ✅`pytest.fixture` usage for reusable WebDriver setup
- ✅Basic Page Object Model (POM) structure for product interaction
- ✅Error handling with `try-except` in POM
- ✅Writing assertions for UI interactions (add to cart, cart view)
- ✅Introducing controlled delays using time.sleep().
- ✅Page navigation checks and UI validation.
- ✅Modular function handling inside Page Object Model.
- ✅Handling WebDriverWait alongside manual wait when needed.
- ✅ Building and integrating a new POM class (Checkout functionality)
- ✅ Improved exception handling in test class with per-case screenshots
- ✅ Explored real-world bugs through manual (exploratory) testing
- __✅ Reported actual bugs in the live application:
  - ✅Checkout input fields unresponsive to manual typing
  - ✅Remove button non-functional when clicked manually__
- ✅Screenshots on failure with timestamps
- ✅Assertions for field inputs and flows
- ✅End-to-End UI flow: login ➝ cart ➝ checkout ➝ order confirm ➝ logout.
- ✅POST, GET methods
- ✅Status code assertions (200, 400, 404)
- ✅API response validation (token, error, data)
- ✅Header-based API Key usage(reqres.in)
- ✅Parametrized payloads and response checks
- ✅Testing on POST,GET,DELETE methods with few altrations. 
- ✅Integration with MockAPI for backend simulation.
- ✅Writing and managing test cases with varying: Endpoints, Methods (GET, POST, DELETE), Payloads (valid and invalid), Expected HTTP status codes (200, 400, 404).
- ✅Learnt about json.loads() and also JSON decoding errors Handling. 
- ✅Manually verified all test cases in Postman before scripting.
- ✅Handled edge cases (404s, invalid payloads)
- ✅`pytest.ini` markers, allure basics, allure report view using `alllure serve <filename>`.
- ✅ Learnt about github actions and implemeted it.
- ✅ Learnt about responses(The responses library is a mock server specifically designed for mocking out requests in Python.)
- ✅ Explored prompts,alerts,dropdwon, select options dropdown, file input handling through selenium.
- ✅ mocked ad-skipping using driver.excute_script.
- ✅ Created `conftest.py`, wrote a shared fixture for Ui tests.
---

## 🚀 How to Run

```bash
# Install dependencies
EXAMPLE: pip install selenium pytest

# Run tests with output (for ui)
pytest -s -v Tests/test_login_pom.py or pytest --html=report_frontend.html  Tests/test_login_pom.py::test_data[test0] #genrates html report

#run tests with output (API)
pytest -s -v Tests/test_backend.py

#run all tests
pytest -s -v Tests/
