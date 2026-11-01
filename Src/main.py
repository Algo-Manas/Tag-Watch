import curl_cffi
from bs4 import BeautifulSoup
from selectolax.lexbor import LexborHTMLParser
import time

initial_time = time.perf_counter()

URL = "https://www.thehindu.com/entertainment/dharamshala-international-film-festival-ritu-sarin-bina-paul-interview/article71632549.ece"

r = curl_cffi.get(URL, impersonate = "chrome")

with open("Data/data.html", 'w', encoding = r.encoding or 'utf-8') as file:
        soup = BeautifulSoup(r.text, 'html.parser')
        file.write(soup.prettify())

with open("Data/data.html", 'r', encoding = r.encoding or 'utf-8') as file:

    parser = LexborHTMLParser(file.read())

    for links in parser.css("a"):
          href = links.attributes.get("href")

          print(href)

final_time = time.perf_counter()

run_time = final_time - initial_time
print(f"Run time taken:{run_time: .3f} seconds")