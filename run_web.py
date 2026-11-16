import time
from playwright.sync_api import sync_playwright

APP_URL = "https://wvscivilianinsurgentdashboard-idkaogysk7npdhz9p7seq3.streamlit.app/"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print(f"Visiting {APP_URL}...")
        page.goto(APP_URL, timeout=60000)
        page.wait_for_timeout(6000)

        wake_button = page.locator("button:has-text('Yes, get this app back up')")
        if wake_button.count() > 0:
            print("App was asleep. Clicking wake-up button...")
            wake_button.click()
            page.wait_for_timeout(15000)
            print("App is now awake!")
        else:
            print("App is already awake. Sleep timer reset!")

        browser.close()

if __name__ == "__main__":
    main()
