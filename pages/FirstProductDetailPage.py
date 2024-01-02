class FirstProductDetailPage:

    def __init__(self, page):
        self.page = page
        self.product_name = page.get_by_text('Blue Top')
        self.product_category = page.get_by_text('Category: Women')
        self.product_price = page.get_by_text('Rs. 500')
        self.product_availability = page.get_by_text('Availability:')
        self.product_condition = page.get_by_text('Condition:')
        self.product_brand = page.get_by_text('Brand:')
