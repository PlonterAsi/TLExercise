import pytest
from webProduct import WebProduct
from MyExpect import Expect as expect

items = ["Brocolli", "Cauliflower", "Cucumber"]

@pytest.fixture(scope="module")
def webProduct():
  url = "https://rahulshettyacademy.com/seleniumPractise/#/"
  return WebProduct(url)

def test_add_item(webProduct):
  current_items = webProduct.total_items
  webProduct.addItem(items[0])
  expect.num(webProduct.getTotalItems()).toEqual(int(current_items) + 1)

def test_add_items(webProduct):
  current_items = webProduct.total_items
  webProduct.addItems(items[1:])
  expect.num(webProduct.getTotalItems()).toEqual(int(current_items) + 2)

def test_go_to_cart(webProduct):
  webProduct.clickOnCart()
  expect.ui(webProduct.findCartPreviewWindow()).to_be_visible()
  webProduct.proceedToCheckOut()
  expect.num(webProduct.getCheckedOutItems().count()).toEqual(len(items))

def test_discount(webProduct):
  webProduct.enterDiscountCode("rahulshettyacademy")
  expect.ui(webProduct.getCodeAppliedText()).to_be_visible()
  total_amount = float(webProduct.getTotalAmount())
  discount_percent = float(webProduct.getDiscountPercent().replace("%", ""))
  discount_amount = float(webProduct.getDiscountAmount())
  expect.num(discount_amount).toEqual(total_amount - ((total_amount * discount_percent) / 100))
