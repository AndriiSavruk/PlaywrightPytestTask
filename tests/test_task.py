import re
from playwright.sync_api import Page, expect
from pages.MainPage import MainPage
from pages.LoginPage import LoginPage
from utils.test_data import Data
from pages.SignupPage import SignupPage
from pages.AccountCreatedPage import AccountCreatedPage
from pages.DeleteAccountPage import DeleteAccountPage

def test_register_user(page: Page):
    main_page = MainPage(page)
    login_page = LoginPage(page)
    signup_page = SignupPage(page)
    account_created_page = AccountCreatedPage(page)
    delete_account_page = DeleteAccountPage(page)

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

    # Click 'Signup' button
    login_page.click_signup_btn()

    # Verify that 'ENTER ACCOUNT INFORMATION' is visible
    expect(signup_page.enter_account_information_title).to_be_visible()

    # Fill details: Title, Name, Email, Password, Date of birth
    signup_page.check_mr_title()
    expect(signup_page.name_field).to_have_value(Data.name)
    expect(signup_page.email_field).to_have_value(Data.email)
    signup_page.fill_password_field(Data.password)
    signup_page.select_day_birth(Data.birthday)
    signup_page.select_month_birth(Data.birthmonth)
    signup_page.select_year_birth(Data.birthyear)

    # Select checkbox 'Sign up for our newsletter!'
    signup_page.check_news_letter_checkbox()

    # Select checkbox 'Receive special offers from our partners!'
    signup_page.check_special_offers_checkbox()

    # Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    signup_page.fill_first_name_field(Data.firstname)
    signup_page.fill_last_name_field(Data.lastname)
    signup_page.fill_company_field(Data.company)
    signup_page.fill_first_address_field(Data.address)
    signup_page.fill_second_address_field(Data.secondaddress)
    signup_page.select_country(Data.country)
    signup_page.fill_state_field(Data.state)
    signup_page.fill_city_field(Data.city)
    signup_page.fill_zipcode_field(Data.zipcode)
    signup_page.fill_mobile_number_field(Data.mobile)

    # Click 'Create Account button'
    signup_page.click_create_account_btn()

    # Verify that 'ACCOUNT CREATED!' is visible
    expect(account_created_page.account_created_title).to_be_visible()

    # Click 'Continue' button
    account_created_page.click_continue_btn()

    # Verify that 'Logged in as username' is visible
    expect(main_page.logged_in_block).to_be_visible()
    expect(main_page.username_name).to_have_text(Data.name)

    # Click 'Delete Account' button
    main_page.click_delete_account_link()

    # Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    expect(delete_account_page.account_deleted_title).to_be_visible()
    delete_account_page.click_continue_btn()






