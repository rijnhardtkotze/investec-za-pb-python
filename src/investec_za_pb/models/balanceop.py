"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from investec_za_pb.types import BaseModel
from investec_za_pb.utils import FieldMetadata, PathParamMetadata
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class BalanceRequestTypedDict(TypedDict):
    account_id: str


class BalanceRequest(BaseModel):
    account_id: Annotated[
        str,
        pydantic.Field(alias="accountId"),
        FieldMetadata(path=PathParamMetadata(style="simple", explode=False)),
    ]


class BalanceDataTypedDict(TypedDict):
    r"""Set of elements used to define the balance details."""

    account_id: str
    r"""A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner."""
    current_balance: float
    r"""A number of monetary units specified in an active currency where the unit of currency is explicit and compliant with ISO 4217."""
    available_balance: float
    r"""A number of monetary units specified in an active currency where the unit of currency is explicit and compliant with ISO 4217."""
    budget_balance: float
    r"""A number of monetary units specified in an active currency where the unit of currency is explicit and compliant with ISO 4217."""
    straight_balance: float
    r"""A number of monetary units specified in an active currency where the unit of currency is explicit and compliant with ISO 4217."""
    cash_balance: float
    r"""A number of monetary units specified in an active currency where the unit of currency is explicit and compliant with ISO 4217."""
    currency: str
    r"""A code allocated to a currency by a Maintenance Agency under an international identification scheme, as described in the latest edition of the international standard ISO 4217 \"Codes for the representation of currencies and funds\"."""


class BalanceData(BaseModel):
    r"""Set of elements used to define the balance details."""

    account_id: Annotated[str, pydantic.Field(alias="accountId")]
    r"""A unique and immutable identifier used to identify the account resource. This identifier has no meaning to the account owner."""

    current_balance: Annotated[float, pydantic.Field(alias="currentBalance")]
    r"""A number of monetary units specified in an active currency where the unit of currency is explicit and compliant with ISO 4217."""

    available_balance: Annotated[float, pydantic.Field(alias="availableBalance")]
    r"""A number of monetary units specified in an active currency where the unit of currency is explicit and compliant with ISO 4217."""

    budget_balance: Annotated[float, pydantic.Field(alias="budgetBalance")]
    r"""A number of monetary units specified in an active currency where the unit of currency is explicit and compliant with ISO 4217."""

    straight_balance: Annotated[float, pydantic.Field(alias="straightBalance")]
    r"""A number of monetary units specified in an active currency where the unit of currency is explicit and compliant with ISO 4217."""

    cash_balance: Annotated[float, pydantic.Field(alias="cashBalance")]
    r"""A number of monetary units specified in an active currency where the unit of currency is explicit and compliant with ISO 4217."""

    currency: str
    r"""A code allocated to a currency by a Maintenance Agency under an international identification scheme, as described in the latest edition of the international standard ISO 4217 \"Codes for the representation of currencies and funds\"."""


class BalanceLinksTypedDict(TypedDict):
    r"""Links relevant to the payload"""

    self_: str


class BalanceLinks(BaseModel):
    r"""Links relevant to the payload"""

    self_: Annotated[str, pydantic.Field(alias="self")]


class BalanceMetaTypedDict(TypedDict):
    r"""Meta Data relevant to the payload"""

    total_pages: NotRequired[int]


class BalanceMeta(BaseModel):
    r"""Meta Data relevant to the payload"""

    total_pages: Annotated[Optional[int], pydantic.Field(alias="totalPages")] = None


class BalanceResponseBodyTypedDict(TypedDict):
    r"""Resource has been retrieved"""

    data: BalanceDataTypedDict
    r"""Set of elements used to define the balance details."""
    links: BalanceLinksTypedDict
    r"""Links relevant to the payload"""
    meta: BalanceMetaTypedDict
    r"""Meta Data relevant to the payload"""


class BalanceResponseBody(BaseModel):
    r"""Resource has been retrieved"""

    data: BalanceData
    r"""Set of elements used to define the balance details."""

    links: BalanceLinks
    r"""Links relevant to the payload"""

    meta: BalanceMeta
    r"""Meta Data relevant to the payload"""
