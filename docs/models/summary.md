# Summary

Summary of the bulk creation. Null if status is `error`.


## Fields

| Field                                      | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `total_inputs`                             | *Optional[int]*                            | :heavy_minus_sign:                         | Total number of trackers to create.        |
| `total_created`                            | *Optional[int]*                            | :heavy_minus_sign:                         | Total number of trackers created.          |
| `total_existing`                           | *Optional[int]*                            | :heavy_minus_sign:                         | Total number of already existing trackers. |
| `total_errors`                             | *Optional[int]*                            | :heavy_minus_sign:                         | Total number of errors (failed creations). |