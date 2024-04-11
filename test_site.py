from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, when, then

scenarios('site.feature')


@given('We navigated to the site')
def visit_site(page: Page):
    page.goto('https://www.saucedemo.com/')


@given('We are logged in')
def logged_in(page):
    visit_site(page)
    page.locator('//input[@id="user-name"]').fill('standard_user')
    page.locator('//input[@id="password"]').fill('secret_sauce')
    page.locator('//input[@data-test="login-button"]').click()
    expect(page.locator('//a[@data-test="shopping-cart-link"]')).to_be_visible()


@when('We fill the login and pass fields with correct data')
def fill_login(page):
    page.locator('//input[@id="user-name"]').fill('standard_user')
    page.locator('//input[@id="password"]').fill('secret_sauce')


@when('We fill the login and pass fields with invalid data')
def fill_login_invalid(page):
    page.locator('//input[@id="user-name"]').fill('locked_out_user')
    page.locator('//input[@id="password"]').fill('secret_sauce')


@when('We press login button')
def press_login(page):
    page.locator('//input[@data-test="login-button"]').click()


@when('We add product to the cart')
def add_product(page):
    page.locator('//button[@data-test="add-to-cart-sauce-labs-backpack"]').click()


@when("We press on cart icon")
def press_cart(page):
    page.locator('//a[@data-test="shopping-cart-link"]').click()


@then("Product appears in cart")
def product_in_cart(page):
    expect(page.locator('//div[@data-test="inventory-item-name"]')).to_contain_text('Sauce Labs Backpack')


@then("We are successfully logged in")
def res_page_suc(page):
    expect(page.locator('//a[@data-test="shopping-cart-link"]')).to_be_visible()


@then("We got an error message and not logged in")
def res_page_unsuc(page):
    expect(page.locator('//h3[@data-test="error"]')).to_contain_text('Epic sadface: Sorry, this user has been locked out.')



