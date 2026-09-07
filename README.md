# Playwright Pytest Automation Framework - AutomationExercise.com

A robust, enterprise-grade test automation framework built using **Python**, **Playwright**, **Pytest**, and **Allure Reports**, implementing the **Page Object Model (POM)** design pattern.

---

## Summary

This framework automates 10 core end-to-end test scenarios on [Automation Exercise](https://automationexercise.com/), validating critical e-commerce workflows including user navigation, product search, cart operations, dynamic reviews, subscription management, and page scrolling.

---

## Requirements

- Python 3.10 or higher
- Allure Commandline (for generating local Allure reports)
- Git

---

## Steps to Install

1. Clone the repository:
   ```bash
   git clone <url>
   ```
2. Create and activate a virtual environment:
   On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install project dependencies:

```bash
pip install -r requirements.txt
```

4. Install Playwright browser binaries:

```bash
playwright install
```

---

## Steps to Launch

- Run all tests (headless Chromium by default):

```bash
python -m pytest
```

- Run tests in parallel using multiple CPU cores:

```bash
python -m pytest -n auto
```

- Run tests on a specific browser:

```bash
python -m pytest --browser_name=firefox
python -m pytest --browser_name=webkit
```

- Run tests with Allure result generation:

```bash
python -m pytest --alluredir=allure-results
```

## Steps to Generate Reports

Generate the Allure HTML report from results:

```bash
allure generate allure-results --clean -o allure-report
```

Open the Allure report in your browser:

```bash
allure open allure-report
```
