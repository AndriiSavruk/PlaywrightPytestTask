import re
from playwright.sync_api import Page, expect
from pages.MainPage import MainPage
from pages.LoginPage import LoginPage
from utils.test_data import Data

def test_register_user(page: Page):
    main_page=MainPage(page)
    login_page = LoginPage(page)

    main_page.navigate()

    # Verify that home page is visible successfully.
    expect(page).to_have_title(re.compile("Automation Exercise"))

    # Click on 'Signup / Login' button
    main_page.click_signup_login_btn()

    # Verify 'New User Signup!' is visible
    expect(login_page.new_user_title).to_be_visible()

    # Enter name and email address
    login_page.fill_new_user_field(Data.name)
    login_page.fill_new_user_email_field(Data.email)
