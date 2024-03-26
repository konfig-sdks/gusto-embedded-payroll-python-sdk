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


class RequiredExternalPayrollsCreateNewPayrollRequest(TypedDict):
    # External payroll's check date.
    check_date: str

    # External payroll's pay period start date.
    payment_period_start_date: str

    # External payroll's pay period end date.
    payment_period_end_date: str

class OptionalExternalPayrollsCreateNewPayrollRequest(TypedDict, total=False):
    pass

class ExternalPayrollsCreateNewPayrollRequest(RequiredExternalPayrollsCreateNewPayrollRequest, OptionalExternalPayrollsCreateNewPayrollRequest):
    pass
