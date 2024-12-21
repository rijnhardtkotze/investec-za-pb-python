# AuthorisationsetupdetailsData

Set of elements used to define the authorisation setup details for the profile and account combination.


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `number_of_authorisation_required`                             | *Optional[str]*                                                | :heavy_minus_sign:                                             | The number of authorisors needed for a payment.                |
| `period`                                                       | List[[models.Period](../models/period.md)]                     | :heavy_minus_sign:                                             | N/A                                                            |
| `authorisers_list_a`                                           | List[[models.AuthorisersListA](../models/authoriserslista.md)] | :heavy_minus_sign:                                             | N/A                                                            |
| `authorisers_list_b`                                           | List[[models.AuthorisersListB](../models/authoriserslistb.md)] | :heavy_minus_sign:                                             | N/A                                                            |