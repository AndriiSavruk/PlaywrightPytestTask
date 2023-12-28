import re
from playwright.sync_api import Page, expect

def test_register_user(page: Page):
    page.goto("https://automationexercise.com/")

    # Verify that home page is visible successfully.
    expect(page).to_have_title(re.compile("Automation Exercise"))

    # Click on 'Signup / Login' button
    page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a').click()

    # Verify 'New User Signup!' is visible
    expect(page.get_by_text("New User Signup!")).to_be_visible()