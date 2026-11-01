To install run (in terminal): 
```bash
pip install curl_cffi --upgrade
```
To import write:
```py
from curl_cffi import requests
```

The module almost similar to the [[Request Module]].
For example, 
```py
var = curl_cffi.get("https://en.wikipedia.org/wiki/Species")

var.text
```

In curl_cffi, if you set impersonate=..., by default, the corresponding headers will be added, you can:
- Add your headers to override them.
- Use `default_headers=False` to completely turn off the default headers.
- Use `curl_cffi.get_fingerprint(...)` and pass the result to impersonate=... for fully editable custom fingerprints.

```py
var = curl_cffi.get_fingerprint("https://en.wikipedia.org/wiki/Species", impersonate = "chrome")
```