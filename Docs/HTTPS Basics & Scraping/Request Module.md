To install request module run (in terminal):
```bash
python -m pip install requests
```

To import write:
```py
import requests
```

## Syntax of requests

```py
var = requests.method(URL, headers, timeout = int)
```
- `var`: Variable where the response data will be stored
- `requests`: Function for request
- `method`: This is HTTP methods. Like, `PUT`, `GET`, etc...
- `URL`: Path to send the request.
- `headers`: My own given custom header (must be a `dict`)
- `timeout`: Timer for the request. Till this value only request will wait.

### Few actions with var

- `var.encoding`: Gives you the encoding
- `var.content`: To get the content's encoding
- `var.text`: Gives you the response content
- `var.json()`: For JSON reponse
- `var.status_code`: To know the status code
- `var.headers`: To know the header values
- `var.headers.get('content-type')`: To know the specific header value