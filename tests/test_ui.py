

import pytest
import re

from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.acme_bank
def test_acme_bank_login(page: Page):

    # Arrange
    # call page.goto with the target URL. This will load the page.
    page.goto('https://demo.applitools.com/')  


    # Act 
    # interacting with elements on the page
    # In Playwright, we call page.locator with a selector to locate the target element, and then we call interaction methods like fill and click
    page.locator('id=username').fill('will')
    page.locator('id=password').fill('123')
    page.locator('id=log-in').click()

    # Assert 
    # we need to check that the main page loaded correctly
    # picking a few of the most important elements on the page to make sure they are visible
    # Playwright uses the 'expect' function to perform 'assertions' instead of Python’s standard assert command.  
    # Using 'expect' will make the assertions wait for elements to be ready before checking them. These are called “web-first assertions". 
    # Playwright also provides several assertion methods for both elements and the page itself, such as the 'to_be_visible' method.
    expect(page.locator('div.logo-w')).to_be_visible()
    expect(page.locator('ul.main-menu')).to_be_visible()
    expect(page.get_by_text('Add Account')).to_be_visible()
    expect(page.get_by_text('Make Payment')).to_be_visible()
    expect(page.get_by_text('View Statement')).to_be_visible()
    expect(page.get_by_text('Request Increase')).to_be_visible()
    expect(page.get_by_text('Pay Now')).to_be_visible()
