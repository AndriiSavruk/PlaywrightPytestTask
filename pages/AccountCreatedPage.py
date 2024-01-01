class AccountCreatedPage:

    def __init__(self, page):
        self.page = page
        self.account_created_title = page.locator('//*[@id="form"]/div/div/div/h2')
        self.continue_btn = page.get_by_text('Continue')

    def click_continue_btn(self):
        self.continue_btn.click()