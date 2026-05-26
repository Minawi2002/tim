import pytest
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

BASE_URL_LANDING = "https://www.ti8m.com/de/career"
BASE_URL_CAREER_CENTER = "https://career.ti8m.com"


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1440, "height": 900},
        "locale": "de-CH",
    }


@pytest.fixture()
def landing_page(page: Page) -> Page:
    page.goto(BASE_URL_LANDING)
    page.wait_for_load_state("networkidle")
    try:
        page.locator("#onetrust-accept-btn-handler").wait_for(state="visible", timeout=5000)
        page.locator("#onetrust-accept-btn-handler").click()
        page.wait_for_load_state("networkidle")
    except PlaywrightTimeoutError:
        pass  # no cookie banner
    return page


@pytest.fixture()
def career_center_page(page: Page) -> Page:
    page.goto(BASE_URL_CAREER_CENTER)
    page.wait_for_load_state("networkidle")
    return page
