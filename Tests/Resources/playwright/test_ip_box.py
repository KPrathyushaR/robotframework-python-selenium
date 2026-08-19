from playwright.sync_api import Page, expect

def test_verify_ip_box(page: Page):
    page.goto("https://testautomationpractice.blogspot.com")

    # Verify IP Box
    text_box = page.locator("#name")
    expect(text_box).to_be_visible()
    expect(text_box).to_be_enabled()
    expect(text_box).to_have_attribute("maxlength", "15")

    text_box.fill("prathyusha")
    page.wait_for_timeout(1000)  # Wait for 1 second to observe the filled value

    max_length = text_box.get_attribute("maxlength")
    assert max_length == "15", f"Expected maxlength to be 15, but got {max_length}"
    print(f"Max length of the text box is: {max_length}")

    get_value = text_box.input_value()
    print(f"Value entered in the text box is: {get_value}")