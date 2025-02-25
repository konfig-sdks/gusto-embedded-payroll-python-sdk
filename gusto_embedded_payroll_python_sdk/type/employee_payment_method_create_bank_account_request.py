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


class RequiredEmployeePaymentMethodCreateBankAccountRequest(TypedDict):
    name: str

    routing_number: str

    account_number: str

    account_type: str

class OptionalEmployeePaymentMethodCreateBankAccountRequest(TypedDict, total=False):
    pass

class EmployeePaymentMethodCreateBankAccountRequest(RequiredEmployeePaymentMethodCreateBankAccountRequest, OptionalEmployeePaymentMethodCreateBankAccountRequest):
    pass
