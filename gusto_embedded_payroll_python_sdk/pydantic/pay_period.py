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

from gusto_embedded_payroll_python_sdk.pydantic.pay_period_payroll import PayPeriodPayroll

class PayPeriod(BaseModel):
    # The start date, inclusive, of the pay period.
    start_date: typing.Optional[str] = Field(None, alias='start_date')

    # The end date, inclusive, of the pay period.
    end_date: typing.Optional[str] = Field(None, alias='end_date')

    # A unique identifier of the pay schedule to which the pay period belongs.
    pay_schedule_uuid: typing.Optional[str] = Field(None, alias='pay_schedule_uuid')

    payroll: typing.Optional[PayPeriodPayroll] = Field(None, alias='payroll')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
