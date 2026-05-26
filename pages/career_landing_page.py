import re
from playwright.sync_api import Page


class CareerLandingPage:
    URL = "https://www.ti8m.com/de/career"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.heading = page.get_by_role("heading", name=re.compile("Gestalte", re.I))
        self.jobs_cta = page.get_by_role("link", name=re.compile(r"Alle Jobs", re.I)).first
        self.jobs_iframe = page.locator("iframe.ti8m-iframe")
        self.first_job_in_iframe = page.frame_locator("iframe.ti8m-iframe").locator("div.job").first
