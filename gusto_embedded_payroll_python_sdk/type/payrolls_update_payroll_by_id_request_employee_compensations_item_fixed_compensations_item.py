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


class RequiredPayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemFixedCompensationsItem(TypedDict):
    pass

class OptionalPayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemFixedCompensationsItem(TypedDict, total=False):
    # The name of the compensation. This also serves as the unique, immutable identifier for this compensation.
    name: str

    # The amount of the compensation for the pay period.
    amount: str

    # The UUID of the job for the compensation.
    job_uuid: int

class PayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemFixedCompensationsItem(RequiredPayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemFixedCompensationsItem, OptionalPayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemFixedCompensationsItem):
    pass
