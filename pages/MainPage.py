class MainPage:
    def __init__(self, page):
        self.page = page
        self.signup_login_btn = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
        self.logout_btn = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
        self.logged_in_block = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a')
        self.username_name = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a/b')
        self.delete_account_link = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')
        self.contact_us_btn = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[8]/a')
        self.test_cases_btn = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')
        self.products_btn = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a')

    def navigate(self):
        self.page.goto("https://automationexercise.com/")

    def click_signup_login_btn(self):
        self.signup_login_btn.click()

    def click_delete_account_link(self):
        self.delete_account_link.click()

    def click_logout_btn(self):
        self.logout_btn.click()

    def click_contact_us_btn(self):
        self.contact_us_btn.click()

    def click_test_cases_btn(self):
        self.test_cases_btn.click()

    def click_products_btn(self):
        self.products_btn.click()

