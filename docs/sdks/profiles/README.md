# Profiles
(*profiles*)

## Overview

### Available Operations

* [get](#get) - Get Profiles

## get

List all the profiles consented to.

### Example Usage

```python
from investec_za_pb import Investec
import os

with Investec(
    oauth2=os.getenv("INVESTEC_OAUTH2", ""),
) as investec:

    res = investec.profiles.get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ProfilesResponseBody](../../models/profilesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |