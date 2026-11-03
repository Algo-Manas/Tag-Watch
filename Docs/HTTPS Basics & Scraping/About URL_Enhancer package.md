The script takes a URL and removes all the query strings and cookies. 

```py
def url_enhanced(UserResponse: str): # : for the type of input

    URL = ""

    for index in UserResponse:
        if (index == '?'):
            break
        else:
            URL = URL + index 

    return URL
```