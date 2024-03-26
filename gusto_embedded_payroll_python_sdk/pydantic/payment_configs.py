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


class PaymentConfigs(BaseModel):
    # Company uuid
    company_uuid: typing.Optional[str] = Field(None, alias='company_uuid')

    # Partner uuid
    partner_uuid: typing.Optional[str] = Field(None, alias='partner_uuid')

    # Payment limit for 1-day or 2-day payroll
    fast_payment_limit: typing.Optional[str] = Field(None, alias='fast_payment_limit')

    # Payment speed for 1-day, 2-day, 4-day
    payment_speed: typing.Optional[str] = Field(None, alias='payment_speed')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
