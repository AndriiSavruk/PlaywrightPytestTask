class SignupPage:

    def __init__(self, page):
        self.page = page
        self.enter_account_information_title = page.get_by_text('Enter Account Information')
        self.mr_title = page.get_by_label('Mr.')
        self.name_field = page.locator('#name')
        self.email_field = page.locator('#email')
        self.password_field = page.locator('#password')
        self.day_birth = page.locator('#days')
        self.month_birth = page.locator('#months')
        self.year_birth = page.locator('#years')
        self.news_letter_checkbox = page.locator('#newsletter')
        self.special_offers_checkbox = page.locator('#optin')
        self.first_name_field = page.locator('#first_name')
        self.last_name_field = page.locator('#last_name')
        self.company_field = page.locator('#company')
        self.first_address_field = page.locator('#address1')
        self.second_address_field = page.locator('#address2')
        self.country_field = page.locator('#country')
        self.state_field = page.locator('#state')
        self.city_field = page.locator('#city')
        self.zipcode_field = page.locator('#zipcode')
        self.mobile_number_field = page.locator('#mobile_number')

    def check_mr_title(self):
        self.mr_title.check()

    def fill_name_field(self, text):
        self.name_field.fill(text)

    def fill_email_field(self, text):
        self.email_field.fill(text)

    def fill_password_field(self, text):
        self.password_field.fill(text)

    def select_day_birth(self, text):
        self.day_birth.select(text)

    def select_month_birth(self, text):
        self.month_birth.select(text)

    def select_year_birth(self, text):
        self.year_birth.select(text)

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
        self.country_field.select(text)

    def fill_state_field(self, text):
        self.state_field.fill(text)

    def fill_city_field(self, text):
        self.city_field.fill(text)

    def fill_zipcode_field(self, text):
        self.zipcode_field.fill(text)

    def fill_mobile_number_field(self, text):
        self.mobile_number_field.fill(text)


