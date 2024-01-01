class SignupPage:

    def __init__(self, page):
        self.page = page
        self.enter_account_information_title = page.get_by_text('Enter Account Information')
        self.mr_title = page.get_by_label('Mr.')
        self.name_field = page.locator('//*[@id="name"]')
        self.email_field = page.locator('//*[@id="email"]')
        self.password_field = page.locator('//*[@id="password"]')
        self.day_birth = page.locator('//*[@id="days"]')
        self.month_birth = page.locator('//*[@id="months"]')
        self.year_birth = page.locator('//*[@id="years"]')
        self.news_letter_checkbox = page.locator('//*[@id="newsletter"]')
        self.special_offers_checkbox = page.locator('//*[@id="optin"]')
        self.first_name_field = page.locator('//*[@id="first_name"]')
        self.last_name_field = page.locator('//*[@id="last_name"]')
        self.company_field = page.locator('//*[@id="company"]')
        self.first_address_field = page.locator('//*[@id="address1"]')
        self.second_address_field = page.locator('//*[@id="address2"]')
        self.country_field = page.locator('//*[@id="country"]')
        self.state_field = page.locator('//*[@id="state"]')
        self.city_field = page.locator('//*[@id="city"]')
        self.zipcode_field = page.locator('//*[@id="zipcode"]')
        self.mobile_number_field = page.locator('//*[@id="mobile_number"]')
        self.create_account_btn = page.get_by_text('Create Account')

    def check_mr_title(self):
        self.mr_title.check()

    def fill_name_field(self, text):
        self.name_field.fill(text)

    def fill_email_field(self, text):
        self.email_field.fill(text)

    def fill_password_field(self, text):
        self.password_field.fill(text)

    def select_day_birth(self, text):
        self.day_birth.select_option(text)

    def select_month_birth(self, text):
        self.month_birth.select_option(text)

    def select_year_birth(self, text):
        self.year_birth.select_option(text)

    def check_news_letter_checkbox(self):
        self.news_letter_checkbox.check()

    def check_special_offers_checkbox(self):
        self.special_offers_checkbox.check()

    def fill_first_name_field(self, text):
        self.first_name_field.fill(text)

    def fill_last_name_field(self, text):
        self.last_name_field.fill(text)

    def fill_company_field(self, text):
        self.company_field.fill(text)

    def fill_first_address_field(self, text):
        self.first_address_field.fill(text)

    def fill_second_address_field(self, text):
        self.second_address_field.fill(text)

    def select_country(self, text):
        self.country_field.select_option(text)

    def fill_state_field(self, text):
        self.state_field.fill(text)

    def fill_city_field(self, text):
        self.city_field.fill(text)

    def fill_zipcode_field(self, text):
        self.zipcode_field.fill(text)

    def fill_mobile_number_field(self, text):
        self.mobile_number_field.fill(text)

    def click_create_account_btn(self):
        self.create_account_btn.click()

