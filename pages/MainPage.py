class MainPage:
    def __init__(self, page):
        self.page = page
        self.signup_login_btn = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
        self.logged_in_block = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a')
        self.username_name = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a/b')
        self.delete_account_link = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')

    def navigate(self):
        self.page.goto("https://automationexercise.com/")

    def click_signup_login_btn(self):
        self.signup_login_btn.click()

    def click_delete_account_link(self):
        self.delete_account_link.click()

