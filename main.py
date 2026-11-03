import curl_cffi
from selectolax.lexbor import LexborHTMLParser
import time
from Packages import Enhance
import re
import json

initial_time = time.perf_counter()

# Enhancing the URL
# URL = Enhance("https://www.flipkart.com/nothing-phone-4b-black-128-gb/p/itm939608b40adbb?pid=MOBHQENAAVZ8F6YP&param=22282&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InNvdXJjZUNvbnRlbnRUeXBlIjp7InNpbmdsZVZhbHVlQXR0cmlidXRlIjp7ImtleSI6InNvdXJjZUNvbnRlbnRUeXBlIiwiaW5mZXJlbmNlVHlwZSI6IlNDVCIsInZhbHVlIjoiSUFEIiwidmFsdWVUeXBlIjoiU0lOR0xFX1ZBTFVFRCJ9fX19fQ%3D%3D&nnc=9POW9FNMERLW_IAD&pageUID=1793633633688") 

URL = Enhance("https://www.flipkart.com/samsung-galaxy-f70e-5g-spotlight-blue-128-gb/p/itmfe8b93b7695f6?pid=MOBHQGZQYHNBZHNW&param=29910&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InNvdXJjZUNvbnRlbnRUeXBlIjp7InNpbmdsZVZhbHVlQXR0cmlidXRlIjp7ImtleSI6InNvdXJjZUNvbnRlbnRUeXBlIiwiaW5mZXJlbmNlVHlwZSI6IlNDVCIsInZhbHVlIjoiSUFEIiwidmFsdWVUeXBlIjoiU0lOR0xFX1ZBTFVFRCJ9fX19fQ%3D%3D&nnc=AST6CTZ08VN9_IAD&pageUID=1793709352920")



header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
}

# initial_request = curl_cffi.Session(URL, impersonate = "chrome") # going to URL with a user-agent

# print(initial_request.cookies)   

# r = curl_cffi.get(URL, impersonate="chrome", cookies=initial_request.cookies) # going to URL with session cookies

session = curl_cffi.Session(impersonate="chrome")
r = session.get(URL, headers=header)

# Scraping the whole webpage and storing it into a file
with open("Data/data.html", 'w', encoding = r.encoding or 'utf-8') as file:
        file.write(r.text)

# Collecting data from stored webpage file
with open("Data/data.html", 'r', encoding = r.encoding or 'utf-8') as file:

    parser = LexborHTMLParser(file.read())

    price_pattern = re.compile(r"₹\s?[\d,]+")

    price = None

    for node in parser.css("div, span"):
        # Check if node has no child elements to avoid matching top-level wrappers
        if node.child is None or node.html.startswith(("<span", "<div")):
            match = price_pattern.search(node.text(strip=True))
            if match:
                price = match.group(0)
                break

    print(f"Extracted Price: {price}")  

    with open("Data/price.json", 'w', encoding='utf-8') as file:

        price = price.replace("\u20b9", "").replace(",", "").strip()

        Data = {
             'Price': price
        }

        json.dump(Data, file, indent = 4)

    # for node in parser.css(f'div[class="{class_value}"]'):
    #     print(node.text(strip=True))


# Things required to know 
print(f"Status Code:{r.status_code}")

final_time = time.perf_counter()

run_time = final_time - initial_time
print(f"Run time taken:{run_time: .3f} seconds")
