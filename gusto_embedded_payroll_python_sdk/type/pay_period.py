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

from gusto_embedded_payroll_python_sdk.type.pay_period_payroll import PayPeriodPayroll

class RequiredPayPeriod(TypedDict):
    pass

class OptionalPayPeriod(TypedDict, total=False):
    # The start date, inclusive, of the pay period.
    start_date: str

    # The end date, inclusive, of the pay period.
    end_date: str

    # A unique identifier of the pay schedule to which the pay period belongs.
    pay_schedule_uuid: str

    payroll: PayPeriodPayroll

class PayPeriod(RequiredPayPeriod, OptionalPayPeriod):
    pass
