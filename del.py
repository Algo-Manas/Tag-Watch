import curl_cffi
from bs4 import BeautifulSoup
from selectolax.lexbor import LexborHTMLParser

URL = "https://www.thehindu.com/entertainment/dharamshala-international-film-festival-ritu-sarin-bina-paul-interview/article71632549.ece"

# sending request and to avoid user-agent error/policy
r = curl_cffi.get(URL, impersonate = "chrome") 

# to write the data into local file with better syntax
with open("del.html", 'w', encoding = r.encoding or 'utf-8') as file:
        soup = BeautifulSoup(r.text, 'html.parser')
        file.write(soup.prettify())

# extracting all the links used in the whole webpage
with open("del.html", 'r', encoding = r.encoding or 'utf-8') as file:

    parser = LexborHTMLParser(file.read()) # parser added to parse the provided file

    # logic for extracting links from the webpage
    for links in parser.css("a"): # links is storing all "a" tags components
          print(links.text()) # prints what is written using "a" tag

          # to print the address of links used in the webpage
          href = links.attributes.get("href")
          print(href)