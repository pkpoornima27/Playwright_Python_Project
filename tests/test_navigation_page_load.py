import re
import time
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect


### TC-001: Homepage Load
def test_homepage_load(page: Page) -> None:
    # Ensure screenshots directory exists
    Path("screenshots").mkdir(exist_ok=True)
    page.goto("https://dotesthere.com/")

    # Asserting Page title displays (FIXED)
    expect(page).to_have_title(re.compile("dotesthere", flags=re.IGNORECASE))

    # Assert Header text
    expect(page.get_by_text(
        "DoTestHere.com by automation mentors Web Elements API Testing Manual Testing")).to_be_visible()

    # Assert Navigation menu items
    expect(page.get_by_role("banner").get_by_role("link", name="Web Elements")).to_be_visible()
    expect(page.get_by_role("banner").get_by_role("link", name="API Testing")).to_be_visible()
    expect(page.get_by_role("banner").get_by_role("link", name="Manual Testing Lab")).to_be_visible()

    # Assert Footer
    expect(page.get_by_role("contentinfo")).to_be_visible()
    page.screenshot(path="screenshots/test_homepage_load.png")


### TC-002: Navigation Menu Functionality (REMOVED DUPLICATE IMPORT)
def test_navigation_menu_functionality(page: Page) -> None:
    # Ensure screenshots directory exists
    Path("screenshots").mkdir(exist_ok=True)
    page.goto("https://dotesthere.com/", wait_until="networkidle")
    expect(
        page.get_by_role("heading", name="Automation Testing Practice")
    ).to_be_visible()

    # Web Elements
    page.get_by_role("banner").get_by_role("link", name="Web Elements").click()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("heading", name=re.compile("Automation Testing Practice", re.IGNORECASE))).to_be_visible()
    page.screenshot(path="screenshots/Web_Elements.png")

    # Back to homepage
    page.get_by_role("banner").get_by_role("link", name="DoTestHere.com").click()
    page.wait_for_load_state("networkidle")
    expect(
        page.get_by_role("heading", name="Automation Testing Practice")
    ).to_be_visible()

    #API Testing
    page.get_by_role("banner").get_by_role("link", name="API Testing").click()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("heading", name="API Testing Practice")).to_be_visible()
    page.screenshot(path="screenshots/API_Testing_Practice_Hub.png")

    # Back to homepage
    page.get_by_role("banner").get_by_role("link", name="DoTestHere.com").click()
    page.wait_for_load_state("networkidle")
    expect(
        page.get_by_role("heading", name="Automation Testing Practice")
    ).to_be_visible()

    #Manual Testing Lab
    page.get_by_role("banner").get_by_role("link", name="Manual Testing Lab").click()
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("heading", name="Scenario Exploration")).to_be_visible()
    page.screenshot(path="screenshots/Manual_Testing_Lab.png")

    #Back to homepage
    page.get_by_role("banner").get_by_role("link", name="DoTestHere.com").click()
    page.wait_for_load_state("networkidle")
    expect(
        page.get_by_role("heading", name="Automation Testing Practice")
    ).to_be_visible()


### TC-003: A/B Testing Version Switch
@pytest.mark.switch
def test_a_b_version_switch(page: Page) -> None:
    # Ensure screenshots directory exists
    Path("screenshots").mkdir(exist_ok=True)
    page.goto("https://dotesthere.com/", wait_until="networkidle")
    expect(
        page.get_by_role("heading", name="Automation Testing Practice")
    ).to_be_visible()

    ##Assert "A/B Testing" is visible
    expect(page.get_by_text("A/B Testing Version A:")).to_be_visible()

    ###Assert A/B switch is clicked
    heading1 = page.get_by_role("heading", name="Version A: Original Content")
    expect(heading1).to_be_visible()
    heading_text1 = heading1.inner_text()
    if "Version A" in heading_text1:
        page.get_by_role("button", name="Switch Version").click()
        expect(page.get_by_role("heading", name="Version B: Alternative Content"))
        page.screenshot(path="screenshots/Version_B.png")
    elif "Version B" in heading_text1:
        page.get_by_role("button", name="Switch Version").click()
        expect(page.get_by_role("heading", name="Version A: Original Content"))
        page.screenshot(path="screenshots/Version_A.png")

    heading2 = page.get_by_role("heading", name="Version B: Alternative Content")
    expect(heading2).to_be_visible()
    heading_text2 = heading2.inner_text()
    if "Version A" in heading_text2:
        page.get_by_role("button", name="Switch Version").click()
        expect(page.get_by_role("heading", name="Version B: Alternative Content"))
        page.screenshot(path="screenshots/Version_B.png")
    elif "Version B" in heading_text2:
        page.get_by_role("button", name="Switch Version").click()
        expect(page.get_by_role("heading", name="Version A: Original Content"))
        page.screenshot(path="screenshots/Version_A.png")

## TC-004: Add Element Functionality
@pytest.mark.add_remove
def test_add_remove_elements(page: Page) -> None:
    # Ensure screenshots directory exists
    Path("screenshots").mkdir(exist_ok=True)
    page.goto("https://dotesthere.com/", wait_until="networkidle")
    expect(
        page.get_by_role("heading", name="Automation Testing Practice")
    ).to_be_visible()

    ##Assert ADD/REMOVE ELEMENTS is visible
    expect(page.get_by_role("heading", name="Add/Remove Elements")).to_be_visible()

    ###Add the elements 4 times
    add_button = page.get_by_role("button", name="Add Element")
    for i in range(4):
        add_button.click()

    time.sleep(2)
    ##Assert 4 delete buttons
    page.screenshot(path="screenshots/delete_button.png")
    delete_buttons = page.get_by_role("button", name="Delete")
    button_count = delete_buttons.count()
    time.sleep(2)
    for i in range(button_count):
        delete_buttons.click()






