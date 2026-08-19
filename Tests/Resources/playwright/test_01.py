import re

from playwright.sync_api import Page, expect
def test_verify(page: Page):
    page.goto(
        "https://testautomationpractice.blogspot.com/p/playwrightpractice.html"
    )

    # Verify logo
    logo = page.get_by_alt_text("logo")
    expect(logo).to_be_visible()

    # Verify text
    expect(
        page.get_by_text("Locate elements by their text content.")
    ).to_be_visible()

    # Verify buttons
    expect(
        page.get_by_role("button", name="Primary Action")
    ).to_be_visible()

    expect(
        page.get_by_role("button", name="Toggle Button")
    ).to_be_visible()

    # Enter text
    # textbox = page.get_by_role("textbox")
    # textbox.fill("Hello World")

    # expect(textbox).to_be_visible()

    # # Verify link
    # expect(page.get_by_role("link")).to_be_visible()

    # Verify text using regex
    expect(
        page.get_by_text(re.compile("some important text that"))
    ).to_be_visible()

    # Fill login fields
    page.get_by_label("Email Address:").fill("prathyusha")
    page.get_by_label("Password:").fill("12345")

    page.get_by_test_id("profile-name").click()



    