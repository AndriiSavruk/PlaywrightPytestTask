class MainPage:
    def __init__(self, page):
        self.page = page
        self.signup_login_btn = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')

    def navigate(self):
        self.page.goto("https://automationexercise.com/")

    def click_signup_login_btn(self):
        self.signup_login_btn.click()

