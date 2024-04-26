import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import pickle

async def main():
    batch_names = ["W24", "S23", "W23", "S22", "W22", "S21", "W21",
                "S20", "W20", "S19", "W19", "S18", "W18", "S17", "W17", "IK12",
                  "S16", "W16", "S15", "W15", "S14", "W14", "S13", "W13", "S12",
                    "W12", "S11", "W11", "S10", "W10", "S09", "W09", "S08", "W08",
                      "S07", "W07", "S06", "W06", "S05"]
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        for tag_name in batch_names:
            url = "https://www.ycombinator.com/companies?batch=" + tag_name
            await page.goto(url)
            await page.wait_for_load_state("networkidle")
        
            for _ in range(1, 15):
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
                print("Scrolling:", _)
                await asyncio.sleep(1)

            html_content = await page.content()
            soup = BeautifulSoup(html_content, "html.parser")

            soup_file = tag_name.lower() + ".pkl" # 
            soup_file='data/'+soup_file
            with open(soup_file, 'wb') as f:
                pickle.dump(soup, f)

        await browser.close()

asyncio.run(main())
