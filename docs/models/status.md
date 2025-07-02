# Status

Status of the bulk creation.

`success`: All trackers were created successfully or already existed. (Status code 200)

`partial`: Operation contains both successes and errors. (Status code 207)

`error`: All creations failed or error on request level. (Status codes 400, 403)


## Values

| Name      | Value     |
| --------- | --------- |
| `SUCCESS` | success   |
| `PARTIAL` | partial   |
| `ERROR`   | error     |