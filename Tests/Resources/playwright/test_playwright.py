from playwright.sync_api import Page, Expect

def test_has_title(page: Page, expect: Expect):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title("Playwright")
