Async works without any dependencies of others. For example, there are 3 functions: Alpha, Beta and Gamma. So in Python the execution of function will be Alpha, Beta and Gamma, which is time killing. While, Async Function will run all three of them at the same time. Though it requires high computation but saves time in many cases.

It is not an in-build thing in Python. To import it write:
```py
import asyncio
```

## Syntax
```py
import asyncio

async def Alpha():
    # logic...

async def Beta():
    # logic...

async def Gamma():
    # logics

# convention
async def main():
    await asyncio.gather(Alpha(), Beta(), Gamma()) # returns a list

if __name__ == "__main__":
    asyncio.run(main())
```

