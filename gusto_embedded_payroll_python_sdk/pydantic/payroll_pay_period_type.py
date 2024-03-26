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


class PayrollPayPeriodType(BaseModel):
    # The start date, inclusive, of the pay period.
    start_date: typing.Optional[str] = Field(None, alias='start_date')

    # The start date, inclusive, of the pay period.
    end_date: typing.Optional[str] = Field(None, alias='end_date')

    # The UUID of the pay schedule for the payroll.
    pay_schedule_uuid: typing.Optional[typing.Optional[str]] = Field(None, alias='pay_schedule_uuid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
