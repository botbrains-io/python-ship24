# Trackers
(*trackers*)

## Overview

### Available Operations

* [create_tracker](#create_tracker) - Create a tracker
* [list_trackers](#list_trackers) - List existing Trackers
* [bulk_create_trackers](#bulk_create_trackers) - Bulk create trackers
* [create_tracker_and_get_tracking_results](#create_tracker_and_get_tracking_results) - Create a tracker and get tracking results
* [get_tracker_by_tracker_id](#get_tracker_by_tracker_id) - Get an existing tracker
* [update_tracker_by_tracker_id](#update_tracker_by_tracker_id) - Update an existing tracker
* [get_tracking_results_of_trackers_by_tracking_number](#get_tracking_results_of_trackers_by_tracking_number) - Get tracking results for existing trackers by tracking number
* [get_tracking_results_of_tracker_by_tracker_id](#get_tracking_results_of_tracker_by_tracker_id) - Get tracking results for an existing tracker
* [resend_webhooks](#resend_webhooks) - Resend webhooks of an existing tracker

## create_tracker

This endpoint allows you to create a new `Tracker`, based on the specified information. Once a `Tracker` is created, you will be able to receive webhook notifications and/or fetch its tracking result.

> This endpoint is idempotent, any subsequent calls with the same parameters won't duplicate `Tracker`. However, providing different information in any of the fields will create a new `Tracker`, as it will be considered as a new shipment.

### Example Usage

```python
import os
from ship_24 import Ship24


with Ship24(
    authorization=os.getenv("SHIP24_AUTHORIZATION", ""),
) as ship24:

    res = ship24.trackers.create_tracker()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TrackerCreateRequest](../../models/trackercreaterequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateTrackerResponse](../../models/createtrackerresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ErrorResponseFormat | 400, 401, 403              | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## list_trackers

This endpoint return a list of all existing `Trackers`, using page-based pagination.

### Example Usage

```python
import os
from ship_24 import Ship24


with Ship24(
    authorization=os.getenv("SHIP24_AUTHORIZATION", ""),
) as ship24:

    res = ship24.trackers.list_trackers(page=275139, limit=821673)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                               | Type                                                                                                                                                                                                    | Required                                                                                                                                                                                                | Description                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `page`                                                                                                                                                                                                  | *int*                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                      | The page index, starting from 1.                                                                                                                                                                        |
| `limit`                                                                                                                                                                                                 | *int*                                                                                                                                                                                                   | :heavy_check_mark:                                                                                                                                                                                      | The maximum number of trackers returned per page.                                                                                                                                                       |
| `sort`                                                                                                                                                                                                  | [Optional[models.Sort]](../../models/sort.md)                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                      | Defines the sorting order of trackers. Use `1` for ascending (`createdAt` oldest first) and `-1` for descending (`createdAt` newest first). The default is ascending (`1`) to ensure stable pagination. |
| `retries`                                                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                                                     |

### Response

**[models.ListTrackersResponse](../../models/listtrackersresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ErrorResponseFormat | 401, 403                   | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## bulk_create_trackers

This endpoint allows you to create up to 100 new `Trackers` in a single operation, based on the specified information. Once the `Trackers` are created, you will be able to receive webhook notifications and/or fetch their tracking results.

> While tracker creation is idempotent, this endpoint itself is not. Any duplicate within the request or any tracker parameters matching an existing tracker will not create a duplicate `Tracker`. However, providing different information in any of the fields will create a new `Tracker`, as it will be considered as a new shipment.

The response will include a summary of:
- The number of trackers successfully created.
- The number of trackers ignored because they already exist.
- The number of trackers that could not be created due to errors.

Additionally, the response will provide details about the created trackers and any errors that occurred during the tracker creation process.

### Example Usage

```python
import os
from ship_24 import Ship24


with Ship24(
    authorization=os.getenv("SHIP24_AUTHORIZATION", ""),
) as ship24:

    res = ship24.trackers.bulk_create_trackers()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.BulkCreateTrackersRequest](../../models/bulkcreatetrackersrequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.BulkCreateTrackersResponseResponse](../../models/bulkcreatetrackersresponseresponse.md)**

### Errors

| Error Type                             | Status Code                            | Content Type                           |
| -------------------------------------- | -------------------------------------- | -------------------------------------- |
| errors.ErrorResponseFormat             | 401                                    | application/json                       |
| errors.BulkCreateTrackersResponseError | 400, 403                               | application/json                       |
| errors.APIError                        | 4XX, 5XX                               | \*/\*                                  |

## create_tracker_and_get_tracking_results

This endpoint creates a new `Tracker` on the specified tracking number , if it does not exist, and returns the tracking results directly. We advise using this endpoint if you are not interested in receiving webhook notifications and just want to fetch tracking results. This way, you can always call this unified endpoint to get tracking results, without worrying about `Tracker` creation and management.


> 🛑 During the very first call for a tracking number, this endpoint will create a `Tracker` and try to return tracking results synchronously if the courier allows it, which can delay the initial answer, at the benefit of getting the tracking results from the first call. **Initial response time may range from a few seconds, up to 1 minute, and results will depend on the courier's system availability at that time.** Subsequent calls will be instantaneous as the `Tracker` will already exist with tracking results ready to use and constantly updated.

> This endpoint is idempotent, any subsequent calls with the same parameters won't duplicate `Tracker`. However, providing different information in any of the fields will create a new `Tracker` as it will be considered as a new shipment.

### Example Usage

```python
import os
from ship_24 import Ship24


with Ship24(
    authorization=os.getenv("SHIP24_AUTHORIZATION", ""),
) as ship24:

    res = ship24.trackers.create_tracker_and_get_tracking_results()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [models.TrackerCreateRequest](../../models/trackercreaterequest.md) | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.CreateTrackerAndGetTrackingResultsResponse](../../models/createtrackerandgettrackingresultsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ErrorResponseFormat | 401, 403                   | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_tracker_by_tracker_id

This endpoint return an existing `Tracker` for a given identifier.

### Example Usage

```python
import os
from ship_24 import Ship24


with Ship24(
    authorization=os.getenv("SHIP24_AUTHORIZATION", ""),
) as ship24:

    res = ship24.trackers.get_tracker_by_tracker_id(tracker_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tracker_id`                                                                                                                                            | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | **Required** Id of the tracker, provided by Ship24 at creation. `clientTrackerId` can also be used in this field by employing the `searchBy` parameter. |
| `search_by`                                                                                                                                             | [Optional[models.GetTrackerByTrackerIDSearchBy]](../../models/gettrackerbytrackeridsearchby.md)                                                         | :heavy_minus_sign:                                                                                                                                      | Parameter allowing to search either by `trackerId`or `clientTrackerId`. Default behavior is by `trackerId`.                                             |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |

### Response

**[models.GetTrackerByTrackerIDResponse](../../models/gettrackerbytrackeridresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ErrorResponseFormat | 401, 403, 404              | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## update_tracker_by_tracker_id

This endpoint allows to modify an existing `Tracker` matching with the given identifier.  

> Once the Tracker has gathered shipment tracking information, certain fields related to the shipment data cannot be modified. These include: 
> - `courierCode` 
> - `originCountryCode` 
> - `destinationCountryCode` 
> - `destinationPostCode` 
> - `shippingDate`

### Example Usage

```python
import os
from ship_24 import Ship24


with Ship24(
    authorization=os.getenv("SHIP24_AUTHORIZATION", ""),
) as ship24:

    res = ship24.trackers.update_tracker_by_tracker_id(tracker_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tracker_id`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Required** Id of the tracker, provided by Ship24 at creation. `clientTrackerId` can also be used in this field by employing the `searchBy` parameter.                                                                                                                                                                                                                                                                                                                                                             |
| `search_by`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[models.UpdateTrackerByTrackerIDSearchBy]](../../models/updatetrackerbytrackeridsearchby.md)                                                                                                                                                                                                                                                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Parameter allowing to search either by `trackerId`or `clientTrackerId`. Default behavior is by `trackerId`.                                                                                                                                                                                                                                                                                                                                                                                                         |
| `is_subscribed`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Setting at `false` will unsubscribe you from the `Tracker`. Once unsubscribed, you will still be able to fetch the existing tracking results but Ship24 won't search for new data or send webhook notifications. `Trackers` are automatically disabled after the parcel delivery or after a long period without any new events. Manually unsubscribing your tracker is not useful, except if you wish to stop receiving webhooks on it or if you need to reuse the `clientTrackerId` value in a new `Tracker`.      |
| `courier_code`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [Optional[models.UpdateTrackerByTrackerIDCourierCode]](../../models/updatetrackerbytrackeridcouriercode.md)                                                                                                                                                                                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Code of the courier(s) handling the shipment (Up to 3 max) (see Couriers list section)  - 📌 Recommended to improve tracking accuracy                                                                                                                                                                                                                                                                                                                                                                               |
| `origin_country_code`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Sender country code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `destination_country_code`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Recipient country code - 📌 Recommended to improve tracking accuracy                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `destination_post_code`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Recipient Post code (or ZIP code)  - 📌 Recommended to improve tracking accuracy                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `shipping_date`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Date at which the shipment has been shipped  - 📌 Recommended to improve tracking accuracy: providing the shipping date helps us accurately identify the shipment and improves our ability to retrieve the correct data. However, an inaccurate shipping date could cause our system to exclude the right shipment. Therefore, please ensure the provided shipping date aligns closely with the actual shipment date, give or take a few days. [Format](http://docs.ship24.com/data-format#logistics-date-and-time) |
| `retries`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Response

**[models.UpdateTrackerByTrackerIDResponse](../../models/updatetrackerbytrackeridresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ErrorResponseFormat | 400, 401, 403, 404         | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_tracking_results_of_trackers_by_tracking_number

This endpoint will return the `tracking` result corresponding to the tracking number provided as a parameter. 

The `tracking` object is detailed in the [SCHEMAS](/schemas/tracking) section. 

Unlike the `/v1/trackers/track` endpoint, a **`Tracker`** **must first be created on this tracking number before using this endpoint.** As a tracking number is not unique, the endpoint may return multiple `trackings` associated with different `Trackers`.

### Example Usage

```python
import os
from ship_24 import Ship24


with Ship24(
    authorization=os.getenv("SHIP24_AUTHORIZATION", ""),
) as ship24:

    res = ship24.trackers.get_tracking_results_of_trackers_by_tracking_number(tracking_number="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `tracking_number`                                                   | *str*                                                               | :heavy_check_mark:                                                  | **Required** Tracking number of the parcel.                         |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetTrackingResultsOfTrackersByTrackingNumberResponse](../../models/gettrackingresultsoftrackersbytrackingnumberresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ErrorResponseFormat | 401, 403                   | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## get_tracking_results_of_tracker_by_tracker_id

This endpoint return the `Tracking` results of an existing `Tracker` matching with the given trackerId. As trackerId are unique, the `Trackings` array will always have only one item. 

The `tracking` object is detailed in the [SCHEMAS](/schemas/tracking) section.

Unlike the `/v1/trackers/track` endpoint, a **`Tracker`** **must first be created on this tracking number before using this endpoint.** As a tracking number is not unique, the endpoint may return multiple `trackings` associated with different `Trackers`.

### Example Usage

```python
import os
from ship_24 import Ship24


with Ship24(
    authorization=os.getenv("SHIP24_AUTHORIZATION", ""),
) as ship24:

    res = ship24.trackers.get_tracking_results_of_tracker_by_tracker_id(tracker_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tracker_id`                                                                                                                                            | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | **Required** Id of the tracker, provided by Ship24 at creation. `clientTrackerId` can also be used in this field by employing the `searchBy` parameter. |
| `search_by`                                                                                                                                             | [Optional[models.GetTrackingResultsOfTrackerByTrackerIDSearchBy]](../../models/gettrackingresultsoftrackerbytrackeridsearchby.md)                       | :heavy_minus_sign:                                                                                                                                      | Parameter allowing to search either by `trackerId`or `clientTrackerId`. Default behavior is by `trackerId`.                                             |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |

### Response

**[models.GetTrackingResultsOfTrackerByTrackerIDResponse](../../models/gettrackingresultsoftrackerbytrackeridresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ErrorResponseFormat | 401, 403, 404              | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |

## resend_webhooks

This endpoint allows to resend all webhook messages of an existing tracker. 

This can be useful in case you missed some webhook messages or if you need to reprocess them for any reason.

### Example Usage

```python
import os
from ship_24 import Ship24


with Ship24(
    authorization=os.getenv("SHIP24_AUTHORIZATION", ""),
) as ship24:

    res = ship24.trackers.resend_webhooks(tracker_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                               | Type                                                                                                                                                    | Required                                                                                                                                                | Description                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tracker_id`                                                                                                                                            | *str*                                                                                                                                                   | :heavy_check_mark:                                                                                                                                      | **Required** Id of the tracker, provided by Ship24 at creation. `clientTrackerId` can also be used in this field by employing the `searchBy` parameter. |
| `search_by`                                                                                                                                             | [Optional[models.ResendWebhooksSearchBy]](../../models/resendwebhookssearchby.md)                                                                       | :heavy_minus_sign:                                                                                                                                      | Parameter allowing to search either by `trackerId`or `clientTrackerId`. Default behavior is by `trackerId`.                                             |
| `retries`                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                        | :heavy_minus_sign:                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                     |

### Response

**[models.ResendWebhooksResponse](../../models/resendwebhooksresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.ErrorResponseFormat | 401, 403, 404              | application/json           |
| errors.APIError            | 4XX, 5XX                   | \*/\*                      |