import sys
from playwright.sync_api import sync_playwright

url = "https://github.com/Amburadullzz/makefun-start-here"
out = "/home/amburadullz/makefun/entry-humans-02/screenshot.png"

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1280, "height": 900}, device_scale_factor=1)
    pg.goto(url, wait_until="networkidle", timeout=90000)
    pg.wait_for_timeout(4000)
    pg.screenshot(path=out, full_page=True)
    b.close()
print("saved", out)
