from playwright.sync_api import Page, expect

def test_google_page(page: Page):
    # Navigate to website
    page.goto("https://google.com/")
    
    # Expect title
    expect(page).to_have_title("Google")

    # Expect image to be visible
    expect(page.locator(".lnXdpd")).to_be_visible()
