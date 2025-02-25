# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict


class ContractorAddress(BaseModel):
    street_1: typing.Optional[str] = Field(None, alias='street_1')

    street_2: typing.Optional[typing.Optional[str]] = Field(None, alias='street_2')

    city: typing.Optional[str] = Field(None, alias='city')

    state: typing.Optional[str] = Field(None, alias='state')

    zip: typing.Optional[str] = Field(None, alias='zip')

    country: typing.Optional[str] = Field(None, alias='country')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
