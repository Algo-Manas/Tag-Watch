There are many other ways of making packages. But, here I am only going to discuss about the in-project packages that you can use throughout the project. 

> [!note]+ NOTE
> I am not sure if you can use it in any project or not but, you surely can use anywhere inside the package's actual project location.

```dict
Project/
    |-pyproject.toml
    |-Src (due to convention packages must be insdie Src folder)
        |- Packages
            |- __init__.py
            |- func.py
```

- `func`: You can rename as per the which file you are importing it from.
- `Project`: This also is customizable.

Inside `pyproject.toml` write:
```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "Packages"
version = "0.1.0"
description = "Internal package for core project functionality"
readme = "README.md"
requires-python = ">=3.8"
authors = [
    { name = "Anonymous" }
]
dependencies = [
    "requests>=2.28.0",
    "pandas>=2.0.0"
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black"
]

[project.scripts]
mypackage-cli = "mypackage.core:main_cli"
```

There are many custom things inside this that you can change. Refer any AI tool for know more

Inside `__init__.py` write:

```py
from func import addition # assuming func have a function named addition
# You can simply import func only

__version__ = "0.1.0"
```

Open project's root terminal and run:
```bash
pip install -e .
```

To use the package you can import it like this:
```py
from Packages import func
```

## FOE (Frequently Occured Errors):
1. Make sure the dictrectory above mentioned is strictly followed.
2. Make sure to enable `(venv)` so that the package is installed in the virtual environment. 
