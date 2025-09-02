from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.latitudemiami.com/", wait_until="networkidle")
    urls = page.eval_on_selector_all("iframe, video, source", "els => els.map(e => e.src || e.getAttribute('src')).filter(Boolean)")
    print(urls)
    browser.close()