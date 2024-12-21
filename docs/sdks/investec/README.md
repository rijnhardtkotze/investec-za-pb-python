# Investec SDK

## Overview

SA PB Account Information: # Introduction
The Investec Private Banking API is a set of programmatic endpoints that can access Private Bank personal and business banking accounts. This API allows you to access the following:
- Accounts
- Balances
- Transactions
- Beneficiaries
- Beneficiary Payments
- Account Transfers
- Documents

There are many possible use cases for the Account Information API: from extracting the data to aggregate it with financial data from other banking institutions to personal money management tools. 

# Getting Started
To start using the Programmable Card API, you'll need API credentials, which you can access in your [Investec Online Banking](https://login.secure.investec.com) profile. Create a new API key (x-api-key) with specified API scopes. Remember to include the *cards* scope

Optionally, use the Investec Sandbox account and credentials to generate mock responses to test your applications. You can use the Sandbox account without opening an Investec Private Bank account. 

## Run with Postman
[Open the collection in postman](https://www.postman.com/investec-open-api/workspace/programmable-banking/collection/26868804-00260d55-0009-42ee-b148-d439992e64ff?action=share&creator=26868804)  
or fork  
[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/26868804-00260d55-0009-42ee-b148-d439992e64ff?action=collection%2Ffork&collection-url=entityId%3D26868804-00260d55-0009-42ee-b148-d439992e64ff%26entityType%3Dcollection%26workspaceId%3D905c2bab-81a1-4297-8b70-2456c776a7a0)

The instructions below will guide you through the process of authenticating in the Postman app: 
1. Set the verb to POST and enter the auth URL [https://openapi.investec.com/identity/v2/oauth2/token](https://openapi.investec.com/identity/v2/oauth2/token) as the request URL.
2. The endpoint receives your client ID and client secret as [BASIC](https://en.wikipedia.org/wiki/BASIC) authentication headers. Select the Authorization tab and select BASIC AUTH from the Type list.
3. Enter your client_ID into the USERNAME field and your secret into the PASSWORD field 
4. Select the Headers tab and enter the **x-api-key** into the KEY field
5. Enter your API key into the VALUE field
6. Select the Body tab and select the x-www-form-urlencoded option
7. Enter grant_type into the KEY field and client_credentials into the VALUE field.
8. Send off your request.

If your keys are valid, the response will contain an access token and the number of seconds the access token is valid. 
Sample response:
```json
{ "access_token": "Z1CRQarGOSogNuUhRlENi5iKAGqh�, "token_type": "Bearer", "expires_in": 1799, "scope": "accounts" }
```

# Authentication
1. OAuth 2.0 access tokens are used to authenticate requests. Your access token authorises you to use the Programmable Card API.
2. To call the API, you must exchange your client ID, secret and API (x-api-key) key for an access token. 
3. You need to include the access token in the Authorisation header with the designation bearer when making calls to the API
4. The access token returned during the authentication request is valid for 30 minutes, at which point it will expire, and you will need to request a new one by calling /identity/v2/oauth2/token again.

When you make calls to the API, include the access token in the Authorisation header with the designation as Bearer. 
<SecurityDefinitions /> 

# Release Notes 
2024-11-07
*   **Enhancement**: Added an additional pending transactions endpoint za/pb/v1/accounts/{accountid}/pending-transactions just returning the pending ones with only the properties available.
*   **Enhancement**: Added the pending transactions to the existing transactions endpoint. Append `?includePending=true` to the querystring
*   **Enhancement**: Added a uuid property to the transactions endpoint. `( accountId.Substring(accountId.Length - 5) + postingDate.Replace("-", "") + postedOrder.PadLeft(7, '0') )` This will only be populated for posted transaction on Private Bank Accounts. This is not a backend banking generated ID and will change if any of the properties making it up changes.
*   **Enhancement**: Added approved beneficiaries to the beneficiary endpoint. They can be identified by the `"beneficiaryType": "INVESTECAPPROVED"` property with another new property eg. `"approvedBeneficiaryCategory": "Municipalities"`

2023-09-07
*   **Enhancement**: Added payment initiation requiring authorisation

2023-08-24
*   **Enhancement**: Added document retreival
*   **Enhancement**: Added more balances to the Balance endpoint

2023-05-29
*   **Enhancement**: Updated response codes returned

2023-03-05
*   **Enhancement**: Added a sandbox environment

2022-11-25
*   **Enhancement**: Included inter account transfers v2 - Transfer Multiple v2
*   **Enhancement**: Included beneficiary payments - Pay Multiple
*   **Enhancement**: Included beneficiaries - Get Beneficiaries
*   **Enhancement**: Included beneficiary categories - Get Beneficiary Categories
*   **Enhancement**: Added properties kycCompliant and profileId to accounts - Get Accounts
*   **Enhancement**: Added property profileId to beneficiaries - Beneficiaries

2022-02-21
*   **Enhancement**: Included inter account transfers - Transfer Multiple

2021-10-01
*   **Fix**: The runningBalance on transactions shows (-) if it is a negative balance - Get Account Transactions

2020-07-21
*   **Enhancement**: Included transactionDate to - Get Account Transactions
*   **Enhancement**: Included date range filter to - Get Account Transactions

2020-09-08
*   **Fix**: Implemented CORS support
*   **Fix**: Implemented multi User-Agent support

2020-11-10
*   **Enhancement**: Included postedOrder to - Get Account Transactions
*   **Enhancement**: Included transactionType to - Get Account Transactions

2020-11-13
*   **Enhancement**: Included transaction type filter to - Get Account Transactions

<.>

### Available Operations
