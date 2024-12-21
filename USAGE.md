<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import investec_za_pb
from investec_za_pb import Investec
import os

with Investec(
    security=investec_za_pb.Security(
        client_id=os.getenv("INVESTEC_CLIENT_ID", ""),
        client_secret=os.getenv("INVESTEC_CLIENT_SECRET", ""),
    ),
) as investec:

    res = investec.accounts.get_all()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import investec_za_pb
from investec_za_pb import Investec
import os

async def main():
    async with Investec(
        security=investec_za_pb.Security(
            client_id=os.getenv("INVESTEC_CLIENT_ID", ""),
            client_secret=os.getenv("INVESTEC_CLIENT_SECRET", ""),
        ),
    ) as investec:

        res = await investec.accounts.get_all_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->