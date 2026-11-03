Conversion of JSON (JavaScript Object Notation) into Python dictionaries. JSON isn't in-buid so to import write:
```py
import json
```

In-memory string:
```py
Data = {
    'Name': "Harry",
    'age': 99
}

json.dumps(Data, indent = int) # to convert data into JSON 
```

With file I/O:
```py
Data = {
    'Name': "Harry",
    'age': 99
}

with open("data.json", 'w', encoding = 'utf-8') as file:
    json.dump(Data, file, indent = int)

with open("data.json", 'r', encoding = 'utf-8') as file:
    data = json.load(file)
```

# Python Dictionaries
```py
name = {
    "A": value1,
    "B": value2,
    "C": value3
}
```
- `name`: It is the name of dictionary
- `"A","B","C"`: Few variables containing values, can use `int` as well
- `value1`, `value2`, `value3`: Values of variables
- Can make many variables by `,` seperated values.

> It does not follow indexing

Instead, 

```py
name["A"]
```

Is used to access it's value.

# Loops for dictionary

```py
for key, value in dictionary.items():
    # logic
```
- `for`: Indicates for loop
- `key`: variable to store keys
- `value`: variable to store values
- `dictionary.items()`: Function which gives 

A basic example:
```py
import json

Data = { # data to be converted to json
    "Price": 3000,
    "Product Name": "Headphones"
}

# creates a file and enters the data stored in the above dict
with open("Data/price.json", 'w', encoding = 'utf-8') as file:
    json.dump(Data, file, indent=4)

# Opens the file and tells info about the dict/JSON stored
with open("Data/price.json", 'r', encoding = 'utf-8') as file:
    data = json.load(file)

    print(data["Price"])
    print(data["Product Name"])
```