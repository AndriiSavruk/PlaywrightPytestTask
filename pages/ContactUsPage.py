class ContactUsPage:

    def __init__(self, page):
        self.page = page
        self.get_in_touch_title = page.locator('//*[@id="contact-page"]/div[2]/div[1]/div/h2')
        self.name_field = page.locator('//*[@id="contact-us-form"]/div[1]/input')
        self.email_field = page.locator('//*[@id="contact-us-form"]/div[2]/input')
        self.subject_field = page.locator('//*[@id="contact-us-form"]/div[3]/input')
        self.message_field = page.locator('//*[@id="message"]')
        self.choose_file = page.locator('//*[@id="contact-us-form"]/div[5]/input')
        self.submit_btn = page.locator('//*[@id="contact-us-form"]/div[6]/input')
        self.success_message = page.locator('//*[@id="contact-page"]/div[2]/div[1]/div/div[2]')
        self.home_link = page.locator('//*[@id="header"]/div/div/div/div[2]/div/ul/li[1]/a')

    def fill_name_field(self, text):
        self.name_field.fill(text)

    def fill_email_field(self, text):
        self.email_field.fill(text)

    def fill_subject_field(self, text):
        self.subject_field.fill(text)

    def fill_message_field(self, text):
        self.message_field.fill(text)

    def upload_file(self, text):
        self.choose_file.set_input_files(text)

    def click_submit_btn(self):
        self.submit_btn.click()

    def click_home_link(self):
        self.home_link.click()