<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import os
from ship24 import Ship24


with Ship24(
    authorization=os.getenv("SHIP24_AUTHORIZATION", ""),
) as s_client:

    res = s_client.trackers.create_tracker()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
from ship24 import Ship24

async def main():

    async with Ship24(
        authorization=os.getenv("SHIP24_AUTHORIZATION", ""),
    ) as s_client:

        res = await s_client.trackers.create_tracker_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->