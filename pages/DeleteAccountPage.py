class DeleteAccountPage:

    def __init__(self, page):
        self.page = page
        self.account_deleted_title = page.get_by_text('ACCOUNT DELETED!')
        self.continue_btn = page.get_by_text('Continue')

    def click_continue_btn(self):
        self.continue_btn.click()