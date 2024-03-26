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


class PayPeriodPayroll(BaseModel):
    # The UUID of the payroll for this pay period.
    payroll_uuid: typing.Optional[str] = Field(None, alias='payroll_uuid')

    # The date on which employees will be paid for the payroll if the payroll is submitted on time.
    check_date: typing.Optional[str] = Field(None, alias='check_date')

    # Whether or not the payroll has been successfully processed. Note that processed payrolls cannot be updated. Additionally, a payroll is not guaranteed to be processed just because the payroll deadline has passed. Late payrolls are not uncommon. Conversely, users may choose to run payroll before the payroll deadline.
    processed: typing.Optional[bool] = Field(None, alias='processed')

    # The date by which payroll should be run for employees to be paid on time. Payroll data, such as time and attendance data, should be submitted on or before this date.
    payroll_deadline: typing.Optional[datetime] = Field(None, alias='payroll_deadline')

    # Whether it is regular pay period or transition pay period.
    payroll_type: typing.Optional[Literal["regular", "transition"]] = Field(None, alias='payroll_type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
