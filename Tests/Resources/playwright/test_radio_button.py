from playwright.sync_api import Page, expect
def test_radio_button(page: Page):
    page.goto("https://testautomationpractice.blogspot.com")

    # Verify radio buttons
    radio_button1 = page.locator("#male")
    radio_button2 = page.locator("#female")

    expect(radio_button1).to_be_visible()
    expect(radio_button2).to_be_visible()

    # Select the first radio button
    radio_button1.check()
    expect(radio_button1).to_be_checked()
    expect(radio_button2).not_to_be_checked()

    # Select the second radio button
    radio_button2.check()
    expect(radio_button2).to_be_checked()
    expect(radio_button1).not_to_be_checked()

    print("Radio button test completed successfully.")