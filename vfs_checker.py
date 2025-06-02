import asyncio
import datetime
import os
import sys
from playwright.async_api import async_playwright

CHECK_INTERVAL = 180  # seconds

async def check_appointments(destination_country_code: str):
    base_url = f"https://visa.vfsglobal.com/arm/en/{destination_country_code.lower()}/login"

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            locale="en-US"
        )
        page = await context.new_page()

        print(f"[{datetime.datetime.now()}] Checking {base_url}")
        await page.goto(base_url)

        try:
            await page.wait_for_selector("text=No appointment slots available", timeout=10000)
            print("❌ No appointments yet.")
        except:
            print("✅ Appointment might be available!")
            os.system(f'notify-send "VFS Slot Available!" "Slot detected for {destination_country_code.upper()}!"')
            raise

        await browser.close()

async def monitor(destination_country_code: str):
    while True:
        try:
            await check_appointments(destination_country_code)
        except Exception as e:
            print("⚠️ Error during check:", e)
        await asyncio.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python vfs_checker.py <country_code>")
        sys.exit(1)

    destination = sys.argv[1].strip().lower()
    asyncio.run(monitor(destination))
