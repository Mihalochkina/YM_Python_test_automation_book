from playwright.sync_api import Page


class TextBoxPage:
    def __init__(self, page: Page):
        self.page = page
        self.full_name_input = page.locator("#userName")
        self.email_input = page.locator("#userEmail")
        self.current_address_input = page.locator("#currentAddress")
        self.permanent_address_input = page.locator("#permanentAddress")
        self.submit_button = page.locator("#submit")
        self.output_name = page.locator("#name")
        self.output_email = page.locator("#email")
        self.output_current_address = page.locator("p#currentAddress")
        self.output_permanent_address = page.locator("p#permanentAddress")

    def navigate(self, url: str):
        self.page.goto(url)

    def fill_form(self, full_name, email, current_address, permanent_address):
        self.full_name_input.fill(full_name)
        self.email_input.fill(email)
        self.current_address_input.fill(current_address)
        self.permanent_address_input.fill(permanent_address)

    def submit_form(self):
        self.submit_button.click()

    def get_output_values(self):
        return {
            "name": self.output_name.text_content(),
            "email": self.output_email.text_content(),
            "current_address": self.output_current_address.text_content(),
            "permanent_address": self.output_permanent_address.text_content()
        }
