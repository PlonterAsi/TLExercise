from playwright.sync_api import sync_playwright, Page

class WebProduct():
  def __init__(self, url) -> None:
    self.url = url
    self.page = self.getPage()
    self.total_items = self.getTotalItems()

  def getPage(self):
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()
    page.goto(self.url)
    return page

  def addItem(self, product: str):
    self.page.locator(f"//h4[contains(text(), '{product}')]/following-sibling::div/descendant::button").click()

  def addItems(self, products: list):
    for product in products:
      self.addItem(product)

  def getTotalItems(self):
    total_items_elem = self.page.locator("//td[contains(text(), 'Items')]/following-sibling::td/strong")
    self.total_items = total_items_elem.inner_text()
    return self.total_items

  def clickOnCart(self):
    # self.page.locator("a.cart-icon").click()
    self.page.get_by_role("link", name="Cart").click()

  def findCartPreviewWindow(self):
    return self.page.locator("div.cart-preview.active")

  def proceedToCheckOut(self):
    self.page.get_by_role("button", name="PROCEED TO CHECKOUT").click()

  def getCheckedOutItems(self):
    _table = self.page.locator("table.cartTable")
    _table.wait_for()
    return _table.locator("tbody tr")

  def applyDiscountCode(self):
    self.page.get_by_role("button", name="Apply").click()

  def enterDiscountCode(self, dis_code: str):
    code_input = self.page.locator("input.promoCode")
    code_input.fill(dis_code)
    self.applyDiscountCode()

  def getCodeAppliedText(self):
    code_applied = self.page.get_by_text("Code applied ..!")
    code_applied.wait_for()
    return code_applied

  def getTotalAmount(self):
    return self.page.locator("span.TotAmt").text_content()

  def getDiscountPercent(self):
    return self.page.locator("span.discountPerc").text_content()

  def getDiscountAmount(self):
    return self.page.locator("span.discountAmt").text_content()