For installation run (in terminal):
```bash
pip install selectolax
```
To use write:
```py
from selectolax.lexbor import LexborHTMLParser
```

## Syntax
```py
var = LexborHTMLParser(file)
```
- `var`: Variable. To be used for methods
- `LexborHTMLParser`: The function
- `file`: The HTML file

### Methods
- `var.css_first("a")`: Returns first tag only
    * `css_first()`: It is the function
    * `"a"`: Any HTML (or custom) tag
- `var.css("a")`: Returns all the tags
- `var.text()`: To extract the text

# Examples
To get string from a tag:
```py
parser = LexborHTMLParser(file)
var = parser.css("a")
text = var.text()
```


To get a particular attribute's value: 
```py
parser = LexborHTMLParser(file)
var = parser.css("a")
href = var.attribute.get("href")
```

For multiple values (or using loops with parsing):
```py
for links in parser.css("a"):
    href = links.attributes.get("href")

    print(links) # for nodes: Totally useless data
    print(href) # for links address
    print(links.text()) # for name of the links
```