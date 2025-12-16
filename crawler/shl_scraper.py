from playwright.sync_api import sync_playwright
import json
import time

BASE_URL = "https://www.shl.com"
CATALOG_URL = "https://www.shl.com/solutions/products/product-catalog/"

def main():
    assessments = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("Opening SHL product catalog...")
        page.goto(CATALOG_URL, timeout=60000)
        page.wait_for_timeout(5000)

        links = set()

        anchors = page.query_selector_all("a")
        for a in anchors:
            href = a.get_attribute("href")
            if href and "/product/" in href and "pre-packaged" not in href.lower():
                links.add(BASE_URL + href)

        print(f"Found {len(links)} assessment links")

        for i, link in enumerate(links):
            try:
                page.goto(link, timeout=60000)
                page.wait_for_timeout(2000)

                name = page.query_selector("h1")
                name = name.inner_text().strip() if name else ""

                description = page.inner_text("body")[:1500]

                text_blob = description.lower()

                assessments.append({
                    "name": name,
                    "url": link,
                    "description": description,
                    "duration": "",
                    "remote_support": "Yes" if "remote" in text_blob else "No",
                    "adaptive_support": "Yes" if "adaptive" in text_blob else "No",
                    "test_type": []
                })

                if i % 20 == 0:
                    print(f"Processed {i}/{len(links)}")

            except Exception as e:
                print("Error:", link, e)

        browser.close()

    with open("data/shl_catalog.json", "w", encoding="utf-8") as f:
        json.dump(assessments, f, indent=2, ensure_ascii=False)

    print(f"Saved {len(assessments)} assessments")

if __name__ == "__main__":
    main()
