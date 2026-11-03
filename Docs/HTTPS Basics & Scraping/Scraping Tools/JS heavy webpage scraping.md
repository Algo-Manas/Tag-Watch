```py
import curl_cffi
from bs4 import BeautifulSoup
from selectolax.lexbor import LexborHTMLParser
from Packages import Enhance


# Enhancing the URL
URL = Enhance("") 


r = curl_cffi.get(URL, impersonate = "chrome") # going to URL with a user-agent

# print(r.cookies)

# Scraping the whole webpage and storing it into a file
with open("Data/data.html", 'w', encoding = r.encoding or 'utf-8') as file:
        soup = BeautifulSoup(r.text, 'html.parser')
        file.write(soup.prettify())


# Collecting data from stored webpage file
with open("Data/data.html", 'r', encoding = r.encoding or 'utf-8') as file:

    parser = LexborHTMLParser(file.read())

    for links in parser.css("a"):

        # to print the link string
        print(links.text())

        # to print all the links 
        href = links.attributes.get("href")
        print(href)


# Things required to know 
print(f"Status Code:{r.status_code}")
```

The following script (which we use for static webpages) does the work but does not provide the response we want. Instead it gives a different webpage which provides different data than we actually want. To solve this issue add browser like headers (in this case only `user-agent` will not work).

```JSON
headers = {
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
```
With the above headers
```py
import curl_cffi
from bs4 import BeautifulSoup
from selectolax.lexbor import LexborHTMLParser
from Packages import Enhance

# Enhancing the URL
URL = Enhance("https://www.amazon.com/Soundcore-Cancelling-Headphones-Comfortable-Bluetooth/dp/B08HMWZBXC/ref=sr_1_12?sr=8-12") 

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

r = curl_cffi.get(URL, impersonate = "chrome", ) # going to URL with a user-agent

# Scraping the whole webpage and storing it into a file
with open("Data/data.html", 'w', encoding = r.encoding or 'utf-8') as file:
        soup = BeautifulSoup(r.text, 'html.parser')
        file.write(soup.prettify())


# Collecting data from stored webpage file
with open("Data/data.html", 'r', encoding = r.encoding or 'utf-8') as file:

    parser = LexborHTMLParser(file.read())

    for links in parser.css("a"):

        # to print the link string
        print(links.text())

        # to print all the links 
        href = links.attributes.get("href")
        print(href)


# Things required to know 
print(f"Status Code:{r.status_code}")
```
The following code will work but will not be able to give the prices. For that I 

