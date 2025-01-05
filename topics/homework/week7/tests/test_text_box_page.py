import pytest
from text_box_page import TextBoxPage
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


def test_fill_text_box(page):
    text_box_page = TextBoxPage(page)
    text_box_page.navigate("https://demoqa.com/text-box")

    # Fill the form with data
    text_box_page.fill_form(
        full_name="Donald Duck",
        email="donald.duck@example.com",
        current_address="56 Main St",
        permanent_address="379 Apple Rd"
    )

    # Submit the form
    text_box_page.submit_form()

    # Verify the output
    output = text_box_page.get_output_values()
    assert output["name"] == "Name:Donald Duck"
    assert output["email"] == "Email:donald.duck@example.com"
    assert output["current_address"] == "Current Address :56 Main St "  # Updated to match the exact output format
    assert output["permanent_address"] == "Permananet Address :379 Apple Rd"  # Corrected to match the actual output but contains typo
