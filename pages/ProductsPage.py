class ProductsPage:

    def __init__(self, page):
        self.page = page
        self.products_list = page.get_by_text('ALL PRODUCTS')
        self.first_product_view_product_btn = page.locator('[href="/product_details/1"]')
        self.search_product_field = page.locator('//*[@id="search_product"]')
        self.search_product_btn = page.locator('//*[@id="submit_search"]')
        self.searched_products_title = page.get_by_text("Searched Products")
        self.stylish_dress_image = page.locator('[src="/get_product_picture/4" ]')

    def click_first_product_view_product_btn(self):
        self.first_product_view_product_btn.click()

    def fill_search_product_field(self, text):
        self.search_product_field.fill(text)

    def click_search_product_btn(self):
        self.search_product_btn.click()