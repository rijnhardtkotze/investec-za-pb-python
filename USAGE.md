<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from investec_za_pb import Investec
import os


with Investec(
    oauth2=os.getenv("INVESTEC_OAUTH2", ""),
) as investec:

    res = investec.accounts.get_all()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from investec_za_pb import Investec
import os

async def main():

    async with Investec(
        oauth2=os.getenv("INVESTEC_OAUTH2", ""),
    ) as investec:

        res = await investec.accounts.get_all_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->