import pytest
from playwright.sync_api import sync_playwright
import allure

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chromium",
        help="Browser choice: chromium, firefox, or webkit"
    )

@pytest.fixture(scope="function")
def page(request):
    browser_name = request.config.getoption("--browser_name")
    
    with sync_playwright() as p:
        if browser_name == "firefox":
            browser = p.firefox.launch(headless=True)
        elif browser_name == "webkit":
            browser = p.webkit.launch(headless=True)
        else:
            browser = p.chromium.launch(headless=True, args=["--start-maximized"])
            
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()
        
        ad_patterns = [
            "**/*googlesyndication.com*",
            "**/*googleads.g.doubleclick.net*",
            "**/*adservice.google.com*",
            "**/*pagead2.googlesyndication.com*",
            "**/*google_vignette*"
        ]
        for pattern in ad_patterns:
            context.route(pattern, lambda route: route.abort())
        
        yield page
        
        if request.node.rep_call.failed:
            allure.attach(
                page.screenshot(full_page=True),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            
        context.close()
        browser.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)

@pytest.fixture(autouse=True)
def logged_in_home(page):
    page.goto("http://automationexercise.com")
    assert "automationexercise.com" in page.url
    return page