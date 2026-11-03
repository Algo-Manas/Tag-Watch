This is a build-in feature in python. 

## Syntax
```py
with open(file.exe, mode, encoding) as file:
    file.verb
```
- `with`: It is the keyword
- `open`: It is the function
- `as`: It is a keyword
- `file`: Object having all the functions you get with open class (aka function).
- `file.exe`: It can be any file you want to perform the verb.
- `encoding`: It must be same as the encoding used in `file.exe`. Generally set it to `'utf-8'`
- `mode`: There are several modes but primarily used in this project is: `'w'` and `'r'`. 
    - `'w'` helps in writing and gives the function related to writing something into hte file.
    - `'r'` helps in reading and gives the function related to reading.
- `verb`: It entirely depends on the mode you chose.
    - In `'w'` you will encounter `file.write`
    - In `'r'` you will encounter `file.read()`