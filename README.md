# 🧪 My Selenium + Python Automation Learning Journey

Welcome to my hands-on automation journey! This repository showcases my daily learning progress with **Selenium WebDriver using Python**, including writing automated test scripts, managing test data, and using testing frameworks like **Pytest**.

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
## 📂 Day 6 - Progress Summary

- Integrated `pytest.fixture` for WebDriver setup and teardown.
- Implemented **Product POM** with:
  - Single product add to cart
  - Cart icon click
  - Basic error handling
- Combined Login + Product POM test (end-to-end)
- Added clean assertions for product add/cart
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
- ✅ CSV Data-Driven Testing
- ✅ Pytest basics: test discovery, assertions, parameterization(`@pytest.mark.parametrize`)
- ✅`pytest.fixture` usage for reusable WebDriver setup
- ✅Basic Page Object Model (POM) structure for product interaction
- ✅Error handling with `try-except` in POM
- ✅Writing assertions for UI interactions (add to cart, cart view)
---

## 🚀 How to Run

```bash
# Install dependencies
pip install selenium pytest

# Run tests with output
pytest -s -v test_login_pom.py
