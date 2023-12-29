import re
from playwright.sync_api import Page, expect
from pages.MainPage import MainPage

def test_register_user(page: Page):
    main_page=MainPage(page)
    main_page.navigate()

    # Verify that home page is visible successfully.
    expect(page).to_have_title(re.compile("Automation Exercise"))

    # Click on 'Signup / Login' button
    main_page.click_signup_login_btn()

    # Verify 'New User Signup!' is visible
    expect(page.get_by_text("New User Signup!")).to_be_visible()
