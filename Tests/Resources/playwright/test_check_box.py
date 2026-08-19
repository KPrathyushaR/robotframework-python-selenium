from playwright.sync_api import Page, expect

def test_check_box(page: Page):
        page.goto("https://testautomationpractice.blogspot.com")

        # single specific checkbox
        checkbox1 = page.get_by_label("Sunday")
        page.wait_for_timeout(1000)  # Wait for 1 second to observe the checkbox state
        expect(checkbox1).to_be_visible()
        checkbox1.check()
        expect(checkbox1).to_be_checked()

        days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        checkboxes=[]
        for day in days:
            checkbox=page.get_by_label(day)
            checkboxes.append(checkbox)
            expect(checkbox).to_be_visible()
            checkbox.check()
            expect(checkbox).to_be_checked()
        print("All checkboxes are checked successfully.")

        # Uncheck the last three checkboxes
        for checkbox in checkboxes[-3:]:  # Uncheck the last three checkboxes
            checkbox.uncheck()
            expect(checkbox).not_to_be_checked()
            page.wait_for_timeout(1000)  # Wait for 1 second to observe the checkbox state

        #toggle checkbox
        for checkbox in checkboxes:
            page.wait_for_timeout(1000)  # Wait for 1 second to observe the checkbox state
            if checkbox.is_checked():
                expect(checkbox).to_be_checked()
            else:
                expect(checkbox).not_to_be_checked()

        #randomly check and uncheck checkboxes
        index=[1,3,5]
        for i in index:
            checkbox=checkboxes[i]
            page.wait_for_timeout(1000)  # Wait for 1 second to observe the checkbox state
            if checkbox.is_checked():
                checkbox.uncheck()
                expect(checkbox).not_to_be_checked()
            else:
                checkbox.check()
                expect(checkbox).to_be_checked()

        #select checkbox based  on the label
        weekday = "Wednesday"
        checkbox = page.get_by_label(weekday)
        page.wait_for_timeout(1000)  # Wait for 1 second to observe the checkbox state
        checkbox.check()
        expect(checkbox).to_be_checked()
        page.wait_for_timeout(1000)  # Wait for 1 second to observe the checkbox state