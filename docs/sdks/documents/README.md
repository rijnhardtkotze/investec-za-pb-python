# Documents
(*documents*)

## Overview

List and retrieve documents.

### Available Operations

* [get_all](#get_all) - Get Documents
* [get_specific](#get_specific) - Get Document

## get_all

List all the documents available.

### Example Usage

```python
import investec_za_pb
from investec_za_pb import Investec
import os

with Investec(
    security=investec_za_pb.Security(
        client_id=os.getenv("INVESTEC_CLIENT_ID", ""),
        client_secret=os.getenv("INVESTEC_CLIENT_SECRET", ""),
    ),
) as investec:

    res = investec.documents.get_all(account_id="<id>", from_date="2023-04-01", to_date="2023-06-01")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | AccountId Id                                                        |                                                                     |
| `from_date`                                                         | *str*                                                               | :heavy_check_mark:                                                  | Refers to the date range filter's start date.                       | 2023-04-01                                                          |
| `to_date`                                                           | *str*                                                               | :heavy_check_mark:                                                  | Refers to the date range filter's end date.                         | 2023-06-01                                                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DocumentsResponseBody](../../models/documentsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_specific

Retrieve the document specified.

### Example Usage

```python
import investec_za_pb
from investec_za_pb import Investec
import os

with Investec(
    security=investec_za_pb.Security(
        client_id=os.getenv("INVESTEC_CLIENT_ID", ""),
        client_secret=os.getenv("INVESTEC_CLIENT_SECRET", ""),
    ),
) as investec:

    investec.documents.get_specific(account_id="<id>", document_type="<value>", document_date="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | AccountId Id                                                        |
| `document_type`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Document Type                                                       |
| `document_date`                                                     | *str*                                                               | :heavy_check_mark:                                                  | Document Date                                                       |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |