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

from gusto_embedded_payroll_python_sdk.type.payroll_blockers_error_errors import PayrollBlockersErrorErrors

class RequiredPayrollBlockersError(TypedDict):
    pass

class OptionalPayrollBlockersError(TypedDict, total=False):
    errors: PayrollBlockersErrorErrors

class PayrollBlockersError(RequiredPayrollBlockersError, OptionalPayrollBlockersError):
    pass
