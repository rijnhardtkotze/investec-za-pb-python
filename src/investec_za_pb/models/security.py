"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from investec_za_pb.types import BaseModel
from investec_za_pb.utils import FieldMetadata, SecurityMetadata
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class SecurityTypedDict(TypedDict):
    client_id: NotRequired[str]
    client_secret: NotRequired[str]
    token_url: NotRequired[str]


class Security(BaseModel):
    client_id: Annotated[
        Optional[str],
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="oauth2",
                sub_type="client_credentials",
                field_name="clientID",
            )
        ),
    ] = None

    client_secret: Annotated[
        Optional[str],
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="oauth2",
                sub_type="client_credentials",
                field_name="clientSecret",
            )
        ),
    ] = None

    token_url: Optional[str] = "https://openapi.investec.com/identity/v2/oauth2/token"
