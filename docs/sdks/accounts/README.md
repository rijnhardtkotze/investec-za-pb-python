# Accounts
(*accounts*)

## Overview

### Available Operations

* [get_all](#get_all) - Get Accounts
* [get_balance](#get_balance) - Get Account Balance
* [get_transactions](#get_transactions) - Get Account Transactions
* [get_pending_transactions](#get_pending_transactions) - Get Account Pending Transactions
* [get_profile_accounts](#get_profile_accounts) - Get Profile Accounts
* [get_authorization_setup](#get_authorization_setup) - Get Authorisation Setup Details
* [get_profile_beneficiaries](#get_profile_beneficiaries) - Get Profile Beneficiaries

## get_all

Get a list of accounts with metadata regarding the account like Account name, Account type  and the profile it is associated to

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

    res = investec.accounts.get_all()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AccountsResponseBody](../../models/accountsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_balance

Obtain a specified account's balance.

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

    res = investec.accounts.get_balance(account_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.BalanceResponseBody](../../models/balanceresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_transactions

Obtain a specified account's transactions.

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

    res = investec.accounts.get_transactions(account_id="<id>", from_date="2021-05-01", to_date="2021-06-01", transaction_type="FeesAndInterest")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   | Example                                                                                                       |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `account_id`                                                                                                  | *str*                                                                                                         | :heavy_check_mark:                                                                                            | N/A                                                                                                           |                                                                                                               |
| `from_date`                                                                                                   | *Optional[str]*                                                                                               | :heavy_minus_sign:                                                                                            | Refers to the date range filter's start date. Will default to today's date, minus 180 days, if not specified. | 2021-05-01                                                                                                    |
| `to_date`                                                                                                     | *Optional[str]*                                                                                               | :heavy_minus_sign:                                                                                            | Refers to the date range filter's end date. Will default to today's date if not specified.                    | 2021-06-01                                                                                                    |
| `transaction_type`                                                                                            | *Optional[str]*                                                                                               | :heavy_minus_sign:                                                                                            | Refers to the transaction type filter's value.                                                                | FeesAndInterest                                                                                               |
| `include_pending`                                                                                             | *Optional[bool]*                                                                                              | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |                                                                                                               |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |                                                                                                               |

### Response

**[models.AccountsTransactionsResponseBody](../../models/accountstransactionsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_pending_transactions

Obtain a specified account's pending transactions.

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

    res = investec.accounts.get_pending_transactions(account_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `account_id`                                                        | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AccountsPendingTransactionsResponseBody](../../models/accountspendingtransactionsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_profile_accounts

List all the accounts for the profile specified.

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

    res = investec.accounts.get_profile_accounts(profileid="10190798011073")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `profileid`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 10190798011073                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ProfileaccountsResponseBody](../../models/profileaccountsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_authorization_setup

List the authorisation setup details for the specified profile and accounts.

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

    res = investec.accounts.get_authorization_setup(profileid="4643233712010169349094403", accountid="10190798011073")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `profileid`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 4643233712010169349094403                                           |
| `accountid`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 10190798011073                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.AuthorisationsetupdetailsResponseBody](../../models/authorisationsetupdetailsresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## get_profile_beneficiaries

List all the beneficiaries available for the profile and account specified.

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

    res = investec.accounts.get_profile_beneficiaries(profileid="4643233712010169349094403", accountid="10190798011073")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `profileid`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 4643233712010169349094403                                           |
| `accountid`                                                         | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 10190798011073                                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ProfilebenefiariesResponseBody](../../models/profilebenefiariesresponsebody.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |