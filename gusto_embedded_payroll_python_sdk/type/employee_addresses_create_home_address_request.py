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


class RequiredEmployeeAddressesCreateHomeAddressRequest(TypedDict):
    pass

class OptionalEmployeeAddressesCreateHomeAddressRequest(TypedDict, total=False):
    street_1: str

    street_2: typing.Optional[str]

    city: str

    state: str

    zip: str

    effective_date: date

    courtesy_withholding: bool

class EmployeeAddressesCreateHomeAddressRequest(RequiredEmployeeAddressesCreateHomeAddressRequest, OptionalEmployeeAddressesCreateHomeAddressRequest):
    pass
