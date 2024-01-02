import re
from playwright.sync_api import Page, expect
from pages.MainPage import MainPage
from pages.LoginPage import LoginPage
from utils.test_data import Data
from pages.SignupPage import SignupPage
from pages.AccountCreatedPage import AccountCreatedPage
from pages.DeleteAccountPage import DeleteAccountPage
from pages.ContactUsPage import ContactUsPage
from pages.ProductsPage import ProductsPage
from pages.FirstProductDetailPage import FirstProductDetailPage


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


def test_login_user_with_correct_email_and_password(page: Page):
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

    # Verify 'Login to your account' is visible
    expect(login_page.login_to_your_account_title).to_be_visible()

    # Enter correct email address and password
    # Let's create new account and logout
    login_page.fill_new_user_field(Data.name)
    login_page.fill_new_user_email_field(Data.email)
    login_page.click_signup_btn()
    signup_page.check_mr_title()
    expect(signup_page.name_field).to_have_value(Data.name)
    expect(signup_page.email_field).to_have_value(Data.email)
    signup_page.fill_password_field(Data.password)
    signup_page.select_day_birth(Data.birthday)
    signup_page.select_month_birth(Data.birthmonth)
    signup_page.select_year_birth(Data.birthyear)
    signup_page.check_news_letter_checkbox()
    signup_page.check_special_offers_checkbox()
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
    signup_page.click_create_account_btn()
    account_created_page.click_continue_btn()
    main_page.click_logout_btn()

    login_page.fill_old_user_email_field(Data.email)
    login_page.fill_old_user_password_field(Data.password)

    # Click 'login' button
    login_page.click_login_btn()

    # Verify that 'Logged in as username' is visible
    expect(main_page.logged_in_block).to_be_visible()
    expect(main_page.username_name).to_have_text(Data.name)

    # Click 'Delete Account' button
    main_page.click_delete_account_link()

    # Verify that 'ACCOUNT DELETED!' is visible
    expect(delete_account_page.account_deleted_title).to_be_visible()

def test_login_user_with_incorrect_email_and_password(page: Page):
    main_page = MainPage(page)
    login_page = LoginPage(page)

    main_page.navigate()

    # Verify that home page is visible successfully.
    expect(page).to_have_title(re.compile("Automation Exercise"))

    # Click on 'Signup / Login' button
    main_page.click_signup_login_btn()

    # Verify 'Login to your account' is visible
    expect(login_page.login_to_your_account_title).to_be_visible()

    # Enter incorrect email address and password
    login_page.fill_old_user_email_field(Data.email)
    login_page.fill_old_user_password_field(Data.password)

    # Click 'login' button
    login_page.click_login_btn()

    # Verify error 'Your email or password is incorrect!' is visible
    expect(login_page.login_warning).to_be_visible()

def test_logout_user(page: Page):
    main_page = MainPage(page)
    login_page = LoginPage(page)

    main_page.navigate()

    # Verify that home page is visible successfully.
    expect(page).to_have_title(re.compile("Automation Exercise"))

    # Click on 'Signup / Login' button
    main_page.click_signup_login_btn()

    # Verify 'Login to your account' is visible
    expect(login_page.login_to_your_account_title).to_be_visible()

    # Enter correct email address and password
    login_page.fill_old_user_email_field(Data.correctemail)
    login_page.fill_old_user_password_field(Data.correctpassword)

    # Click 'login' button
    login_page.click_login_btn()

    # Verify that 'Logged in as username' is visible
    expect(main_page.logged_in_block).to_be_visible()
    expect(main_page.username_name).to_have_text(Data.correctname)

    # Click 'Logout' button
    main_page.click_logout_btn()

    # Verify that user is navigated to login page
    expect(page).to_have_url('https://automationexercise.com/login')

def test_register_user_with_existing_email(page: Page):
    main_page = MainPage(page)
    login_page = LoginPage(page)

    main_page.navigate()

    # Verify that home page is visible successfully.
    expect(page).to_have_title(re.compile("Automation Exercise"))

    # Click on 'Signup / Login' button
    main_page.click_signup_login_btn()

    # Verify 'New User Signup!' is visible
    expect(login_page.new_user_title).to_be_visible()

    # Enter name and already registered email address
    login_page.fill_new_user_field(Data.correctname)
    login_page.fill_new_user_email_field(Data.correctemail)

    # Click 'Signup' button
    login_page.click_signup_btn()

    # Verify error 'Email Address already exist!' is visible
    expect(login_page.new_user_warning).to_be_visible()

def test_contact_us_form(page: Page):
    main_page = MainPage(page)
    contact_us_page = ContactUsPage(page)

    main_page.navigate()

    # Verify that home page is visible successfully.
    expect(page).to_have_title(re.compile("Automation Exercise"))

    # Click on 'Contact Us' button
    main_page.click_contact_us_btn()

    # Verify 'GET IN TOUCH' is visible
    expect(contact_us_page.get_in_touch_title).to_be_visible()

    # Enter name, email, subject and message
    contact_us_page.fill_name_field(Data.correctname)
    contact_us_page.fill_email_field(Data.correctemail)
    contact_us_page.fill_subject_field('Test')
    contact_us_page.fill_message_field('Hello world!')

    # Upload file
    contact_us_page.upload_file('message.rtf')

    # Click 'Submit' button
    # Click OK button
    page.on("dialog", lambda dialog: dialog.accept())
    contact_us_page.click_submit_btn()

    # Verify success message 'Success! Your details have been submitted successfully.' is visible
    expect(contact_us_page.success_message).to_be_visible()

    #  Click 'Home' button and verify that landed to home page successfully
    contact_us_page.click_home_link()
    expect(page).to_have_url('https://automationexercise.com/')

def test_verify_test_cases_page(page: Page):
    main_page = MainPage(page)

    main_page.navigate()

    # Verify that home page is visible successfully.
    expect(page).to_have_title(re.compile("Automation Exercise"))

    # Click on 'Test Cases' button
    main_page.click_test_cases_btn()

    # Verify user is navigated to test cases page successfully
    expect(page).to_have_url('https://automationexercise.com/test_cases')

def test_verify_all_products_and_product_detail_page(page: Page):
    main_page = MainPage(page)
    products_page = ProductsPage(page)
    first_product_detail_page = FirstProductDetailPage(page)

    main_page.navigate()

    # Verify that home page is visible successfully.
    expect(page).to_have_title(re.compile("Automation Exercise"))

    # Click on 'Products' button
    main_page.click_products_btn()

    # Verify user is navigated to ALL PRODUCTS page successfully
    expect(page).to_have_url('https://automationexercise.com/products')

    # The products list is visible
    expect(products_page.products_list).to_be_visible()

    # Click on 'View Product' of first product
    products_page.click_first_product_view_product_btn()

    # User is landed to product detail page
    expect(page).to_have_url('https://automationexercise.com/product_details/1')

    # Verify that detail is visible: product name, category, price, availability, condition, brand
    expect(first_product_detail_page.product_name).to_be_visible()
    expect(first_product_detail_page.product_category).to_be_visible()
    expect(first_product_detail_page.product_price).to_be_visible()
    expect(first_product_detail_page.product_availability).to_be_visible()
    expect(first_product_detail_page.product_condition).to_be_visible()
    expect(first_product_detail_page.product_brand).to_be_visible()

def test_search_product(page: Page):
    main_page = MainPage(page)
    products_page = ProductsPage(page)

    main_page.navigate()

    # Verify that home page is visible successfully.
    expect(page).to_have_title(re.compile("Automation Exercise"))

    # Click on 'Products' button
    main_page.click_products_btn()

    # Verify user is navigated to ALL PRODUCTS page successfully
    expect(page).to_have_url('https://automationexercise.com/products')

    # Enter product name in search input and click search button
    products_page.fill_search_product_field(Data.product)
    products_page.click_search_product_btn()

    # Verify 'SEARCHED PRODUCTS' is visible
    expect(products_page.searched_products_title).to_be_visible()

    # Verify all the products related to search are visible
    expect(products_page.stylish_dress_image).to_be_visible()

def test_verify_subscription_in_home_page(page: Page):
    main_page = MainPage(page)

    main_page.navigate()

    # Verify that home page is visible successfully.
    expect(page).to_have_title(re.compile("Automation Exercise"))

    # Scroll down to footer
    main_page.footer.scroll_into_view_if_needed()

    # Verify text 'SUBSCRIPTION'
    expect(main_page.subscription_title).to_be_visible()

    # Enter email address in input and click arrow button
    main_page.fill_email_address_field(Data.correctemail)
    main_page.click_subscribe_btn()

    # Verify success message 'You have been successfully subscribed!' is visible
    expect(main_page.success_subscribe_message).to_be_visible()
























