# APIForPerCallPlans
(*api_for_per_call_plans*)

## Overview

The **Tracking API (Per-call Plans)** is a specific product and associated endpoint on which usage is measured per API Call made. Each API call is synchronously fetching data from couriers which make it slower and more depend on courier's system availability.

Our standard "Per-shipment" product & plans remain the best choice as it offers more features, allow faster tracking information fetching with less dependency on courier's system availability at a lower cost overall.

> ⚠ You need an active "Per-call" subscription to use this endpoint.

### Available Operations

* [get_tracking](#get_tracking) - Get tracking results by tracking number

## get_tracking

This endpoint will return the `tracking` corresponding to the tracking number provided as a parameter. 

The `tracking` object is detailed in the [SCHEMAS](/schemas/tracking) section.

For better accuracy, we strongly advise to provide extra information such as the origin country, destination postcode & country, and the shipping date.

> 🛑 You need an active "Per-call" subscription to use this endpoint. Our standard "Per-shipment" product & plans remain the best choice as it offers more features, allow faster tracking information fetching with less dependency on courier's system availability at a lower cost overall.


> 🛑 As this endpoint is synchronously fetching tracking results from couriers, **response time may be up to 1 minute, and results depend on the courier's system availability** at the time of the call.

### Example Usage

```python
import os
from ship24 import Ship24


with Ship24(
    authorization=os.getenv("SHIP24_AUTHORIZATION", ""),
) as s_client:

    res = s_client.api_for_per_call_plans.get_tracking()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.GetTrackingRequest](../../models/gettrackingrequest.md)     | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetTrackingResponse](../../models/gettrackingresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ErrorResponseFormat | 400, 401, 403              | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |