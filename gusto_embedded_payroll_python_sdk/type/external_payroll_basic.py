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


class RequiredExternalPayrollBasic(TypedDict):
    pass

class OptionalExternalPayrollBasic(TypedDict, total=False):
    # The UUID of the external payroll.
    uuid: str

    # The UUID of the company.
    company_uuid: str

    # External payroll's check date.
    check_date: str

    # External payroll's pay period start date.
    payment_period_start_date: str

    # External payroll's pay period end date.
    payment_period_end_date: str

    # The status of the external payroll. The status will be `unprocessed` when the external payroll is created and transition to `processed` once tax liabilities are entered and finalized.  Once in the `processed` status all actions that can edit an external payroll will be disabled.
    status: str

class ExternalPayrollBasic(RequiredExternalPayrollBasic, OptionalExternalPayrollBasic):
    pass
