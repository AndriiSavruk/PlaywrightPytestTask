class ProductsPage:

    def __init__(self, page):
        self.page = page
        self.products_list = page.get_by_text('ALL PRODUCTS')
        self.first_product_view_product_btn = page.locator('[href="/product_details/1"]')

    def click_first_product_view_product_btn(self):
        self.first_product_view_product_btn.click()