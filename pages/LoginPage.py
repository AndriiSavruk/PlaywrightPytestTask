class LoginPage:
    def __init__(self, page):
        self.page = page
        self.new_user_title = page.get_by_text("New User Signup!")
        self.new_user_name_field = page.locator('//*[@id="form"]/div/div/div[3]/div/form/input[2]')
        self.new_user_email_field = page.locator('//*[@id="form"]/div/div/div[3]/div/form/input[2]')
        self.signup_btn = page.locator('//*[@id="form"]/div/div/div[3]/div/form/button')


    def fill_new_user_field(self, text):
        self.new_user_name_field.fill(text)

    def fill_new_user_email_field(self, text):
        self.new_user_email_field.fill(text)

    def click_signup_btn(self):
        self.signup_btn.click()