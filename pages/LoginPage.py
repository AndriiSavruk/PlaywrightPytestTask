class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login_to_your_account_title = page.get_by_text("Login to your account")
        self.old_user_email_field = page.locator('//*[@id="form"]/div/div/div[1]/div/form/input[2]')
        self.old_user_password_field = page.locator('//*[@id="form"]/div/div/div[1]/div/form/input[3]')
        self.new_user_title = page.get_by_text("New User Signup!")
        self.new_user_name_field = page.locator('//*[@id="form"]/div/div/div[3]/div/form/input[2]')
        self.new_user_email_field = page.locator('//*[@id="form"]/div/div/div[3]/div/form/input[3]')
        self.signup_btn = page.locator('//*[@id="form"]/div/div/div[3]/div/form/button')
        self.login_btn = page.locator('//*[@id="form"]/div/div/div[1]/div/form/button')
        self.login_warning = page.get_by_text("Your email or password is incorrect!")
        self.new_user_warning = page.get_by_text("Email Address already exist!")


    def fill_new_user_field(self, text):
        self.new_user_name_field.fill(text)

    def fill_new_user_email_field(self, text):
        self.new_user_email_field.fill(text)

    def click_signup_btn(self):
        self.signup_btn.click()

    def fill_old_user_email_field(self, text):
        self.old_user_email_field.fill(text)

    def fill_old_user_password_field(self, text):
        self.old_user_password_field.fill(text)

    def click_login_btn(self):
        self.login_btn.click()

