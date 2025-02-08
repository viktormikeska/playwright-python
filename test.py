from playwright.sync_api import Page, expect

def test_page_title(page: Page):
    # Navigate to website
    page.goto("https://playwright.dev/")
    
    # Expect title
    expect(page).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")
