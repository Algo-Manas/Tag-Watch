The actual scripting to extract data from webpages can be known as **Scraping**. Using **Python** we are going to scrap different webpages.

As a request is to be send from python (as a client) to the server. We are going to use [**Requests** python module](https://requests.readthedocs.io/en/latest/) For in-depth learning of request use [[Request Module]] or go to [docs](https://requests.readthedocs.io/en/latest/user/quickstart/).

Following script tries to extract data from wikipedia (it's a random article) from the URL: https://en.wikipedia.org/wiki/Species.

```py
import requests

URL = "https://en.wikipedia.org/wiki/Species"

r = requests.get(URL) # HTTP request

print(r.encoding) # encoding of the content
print(r.content) # HTTP response body
```

But there no content with `r.cotent` instead shows: 
```bash
ISO-8859-1
b'Please set a user-agent and respect our robot policy https://w.wiki/4wJS. See also https://phabricator.wikimedia.org/T400119.\n'
```

This issue can resolved using browser behaviour as a client-bot. Here I have used `curl_cffi` along with `Playwright`. Following script resolves this issue:
```py
import curl_cffi

URL = "https://en.wikipedia.org/wiki/Species"

r = curl_cffi.get(URL, impersonate="chrome")

print(r.encoding) # tell about encoding
print(r.text) # actual content (not content as I need raw text instead of bytes)
```

Now, script can easily access the content. But, now we have to store it into a file for this the following script needed to be employed:
```py
import curl_cffi

URL = "https://en.wikipedia.org/wiki/Species"

r = curl_cffi.requests.get(URL, impersonate="chrome") # behaving as chrome browser

with open("Data/data.html", 'w', encoding = r.encoding) as file: # saving the HTTP response into Data/data.html file
    file.write(r.text)
```

But, sometimes the data's format (or say syntax) isn't in a quiet good and understandable manner. To solve this issue I have used Beautiful-Soup. To learn this in-depth go to [Docs](https://beautiful-soup-4.readthedocs.io/en/latest/#) or [[BeautifulSoup]]

```py
import curl_cffi
from bs4 import BeautifulSoup

URL = "https://www.quantamagazine.org/how-spiders-spin-silk-dope-into-natures-toughest-material-20261028/"

r = curl_cffi.requests.get(URL, impersonate="chrome")

with open("Data/data.html", 'w', encoding = r.encoding) as file:
    soup = BeautifulSoup(r.text, 'html.parser')
    file.write(soup.prettify())
```

For scraping, I am going to use [[Selectolax]]. Though it is only good for HTML parser any JS heavy of XML webpages will not work using this. But, it is much faster than beautifulSoup and other parsing tools.

```py
import curl_cffi
from bs4 import BeautifulSoup
from selectolax.lexbor import LexborHTMLParser

URL = "https://www.thehindu.com/entertainment/dharamshala-international-film-festival-ritu-sarin-bina-paul-interview/article71632549.ece"

# sending request and to avoid user-agent error/policy
r = curl_cffi.get(URL, impersonate = "chrome") 

# to write the data into local file with better syntax
with open("Data/data.html", 'w', encoding = r.encoding or 'utf-8') as file:
        soup = BeautifulSoup(r.text, 'html.parser')
        file.write(soup.prettify())

# extracting all the links used in the whole webpage
with open("Data/data.html", 'r', encoding = r.encoding or 'utf-8') as file:

    parser = LexborHTMLParser(file.read()) # parser added to parse the provided file

    # logic for extracting links from the webpage
    for links in parser.css("a"): # links is storing all "a" tags components
          print(links.text()) # prints what is written using "a" tag

          # to print the address of links used in the webpage
          href = links.attributes.get("href")
          print(href)
```

The following code is able to scrap all the static webpages. 

> [!note]+ NOTE
> The code ins't ready for any status code. Code only works if status is `200` or equivalent.