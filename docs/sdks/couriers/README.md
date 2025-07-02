# Couriers
(*couriers*)

## Overview

### Available Operations

* [get_couriers](#get_couriers) - Get all couriers

## get_couriers

This endpoint will return the list of all couriers supported by Ship24, identified by their `courierCode`.

### Example Usage

```python
import os
from ship24 import Ship24


with Ship24(
    authorization=os.getenv("SHIP24_AUTHORIZATION", ""),
) as s_client:

    res = s_client.couriers.get_couriers()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetCouriersResponse](../../models/getcouriersresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ErrorResponseFormat | 401, 403                   | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |