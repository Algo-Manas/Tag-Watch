To scrap any thing from any static webpages like Wikipedia or Quanta Magazine use the following code:
```py
import curl_cffi
from bs4 import BeautifulSoup
from selectolax.lexbor import LexborHTMLParser
import time
from Packages import Enhance

initial_time = time.perf_counter()

# Enhancing the URL
URL = Enhance("https://www.amazon.com/Soundcore-Cancelling-Headphones-Comfortable-Bluetooth/dp/B08HMWZBXC/ref=sr_1_12?sr=8-12") 

print(URL)

r = curl_cffi.get(URL, impersonate = "chrome") # going to URL with a user-agent

# Scraping the whole webpage and storing it into a file
with open("Data/data.html", 'w', encoding = r.encoding or 'utf-8') as file:
        soup = BeautifulSoup(r.text, 'html.parser')
        file.write(soup.prettify())


# Collecting data from stored webpage file
with open("Data/data.html", 'r', encoding = r.encoding or 'utf-8') as file:

    parser = LexborHTMLParser(file.read())

    for content in parser.css("a"):

        # to print the link string
        print(links.text())

        # to print all the links 
        href = links.attributes.get("href")
        print(href)


# Things required to know 
print(f"Status Code:{r.status_code}")

final_time = time.perf_counter()

run_time = final_time - initial_time
print(f"Run time taken:{run_time: .3f} seconds")

```

- To get a particular data from the webpage change `"a"` to the following data data you required. Also do the changes are per required. An examples can be:
```py
for content in parser.css("title"):
    print(content.text()) # to get the title
```