import logging
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.INFO)

def login(email, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://ads.tiktok.com/i18n/login?redirect=https%3A%2F%2Fads.tiktok.com%2Fi18n%2Fhome')
        page.fill('input[name="email"]', email)
        page.fill('input[name="password"]', password)
        page.click('button[type="button"]')
        page.wait_for_timeout(60000)
        context.storage_state(path="state.json")
        browser.close()
