from playwright.sync_api import sync_playwright
from datetime import datetime

print("Starting the playwright automation script...")
print(F"Current date and time: {datetime.now()}")

#daily cricket report bot
#chromium --> cricket site --> Extract the report --> screenshot --> final excel file
with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False)

    # Create new page
    page = browser.new_page()

    # Open Cricbuzz
    page.goto("https://www.cricbuzz.com/live-cricket-stream/172731/zim-vs-afg-2nd-test-afghanistan-vs-zimbabwe-in-uae-2026")
    page.wait_for_load_state("domcontentloaded")

    # Take screenshot
    page.screenshot(path="crickbuzz_screenshot.png")
    print("Cricbuzz screenshot saved!")

    # Extract webpage text
    data = page.locator("body").inner_text()
    print("Cricket page data:")
    print(data)

    # Save extracted data
    with open("crickbuzz_data.txt", "w", encoding="utf-8") as file:
        file.write(data)

    print("Cricket data saved successfully!")

    # Close browser
    browser.close()