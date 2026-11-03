To isntall run (in terminal):
```bash
python -m pip install beautifulsoup4   
```
To import write:
```py
from bs4 import BeautifulSoup
```

### Syntax
```py
var = BeautifulSoup(html_doc, parser)
```
- `var`: Variable. In this you can use beautifulsoup's methods.
- `BeautifulSoup`: The function
- `html_doc`: The file
- `parser`: File type (i.e .html, .md etc...)

## Methods in Beautiful Soup
- `var.prettify()`: To make syntax (or format) better.
- `var.get_text()`: To get all the text.

# Making Soup
Following method can use to assign the file to `BeautifulSoup`.
```py
from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp)
```