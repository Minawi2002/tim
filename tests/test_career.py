"""
Test suite – ti&m Career Page
SUT: https://www.ti8m.com/de/career

P1  Karriere-Seite lädt und zeigt zentrale Inhalte
P1  User findet offene Jobs / Jobübersicht
P1  User kann Jobdetails oder Bewerbung öffnen
"""

import re
import pytest
from playwright.sync_api import Page, expect

from pages import CareerLandingPage


@pytest.mark.smoke
def test_career_page_loads(landing_page: Page) -> None:
    """P1 – Karriere-Seite lädt und zeigt zentrale Inhalte"""
    lp = CareerLandingPage(landing_page)
    expect(lp.heading).to_be_visible()
    expect(lp.jobs_cta).to_be_visible()


@pytest.mark.smoke
def test_job_overview_accessible(landing_page: Page) -> None:
    """P1 – User findet offene Jobs / Jobübersicht"""
    lp = CareerLandingPage(landing_page)
    lp.jobs_cta.click()
    expect(lp.jobs_iframe).to_be_visible()


@pytest.mark.smoke
def test_job_detail_opens(landing_page: Page) -> None:
    """P1 – User kann Jobdetails oder Bewerbung öffnen"""
    lp = CareerLandingPage(landing_page)
    lp.jobs_cta.click()

    expect(lp.first_job_in_iframe).to_be_visible(timeout=10000), "Keine Stelleninserate im iframe gefunden"
    with landing_page.expect_popup() as popup_info:
        lp.first_job_in_iframe.click()

    detail = popup_info.value
    detail.wait_for_load_state("networkidle", timeout=15000)
    expect(detail.get_by_role("link", name=re.compile(r"Bewerben|Apply", re.I)).first).to_be_visible()
