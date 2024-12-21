# InterAccountTransfers
(*inter_account_transfers*)

## Overview

### Available Operations

* [~~transfer~~](#transfer) - Transfer Multiple (TO BE DEPRECATED) :warning: **Deprecated**
* [transfer_v2](#transfer_v2) - Transfer Multiple v2

## ~~transfer~~

Transfer funds to one or multiple accounts.

> :warning: **DEPRECATED**: This will be removed in a future release, please migrate away from it as soon as possible.

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

    res = investec.inter_account_transfers.transfer(account_id="XXXXXX", transfer_list=[
        {
            "beneficiary_account_id": "XXXXXXXXXX",
            "amount": "10.12",
            "my_reference": "Trans from PBA to PS",
            "their_reference": "Trans from PBA to PS",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | XXXXXX                                                              |
| `transfer_list`                                                     | List[[models.TransferList](../../models/transferlist.md)]           | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TransferResponseBody](../../models/transferresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## transfer_v2

Transfer funds to one or multiple accounts.

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

    res = investec.inter_account_transfers.transfer_v2(account_id="<id>", transfer_list=[
        {
            "beneficiary_account_id": "XXXXXXXXXX",
            "amount": "10.12",
            "my_reference": "Trans from PBA to PS",
            "their_reference": "Trans from PBA to PS",
        },
    ], profile_id="10163189587443")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `account_id`                                                                  | *str*                                                                         | :heavy_check_mark:                                                            | N/A                                                                           |
| `transfer_list`                                                               | List[[models.Transferv2TransferList](../../models/transferv2transferlist.md)] | :heavy_minus_sign:                                                            | N/A                                                                           |
| `profile_id`                                                                  | *Optional[str]*                                                               | :heavy_minus_sign:                                                            | N/A                                                                           |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.Transferv2ResponseBody](../../models/transferv2responsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |