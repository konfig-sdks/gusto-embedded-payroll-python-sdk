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


class RequiredLocationsCreateCompanyLocationRequest(TypedDict):
    phone_number: str

    street_1: str

    city: str

    state: str

    zip: str

class OptionalLocationsCreateCompanyLocationRequest(TypedDict, total=False):
    street_2: typing.Optional[str]

    country: str

    # Specify if this location is the company's mailing address.
    mailing_address: bool

    # Specify if this location is the company's filing address.
    filing_address: bool

class LocationsCreateCompanyLocationRequest(RequiredLocationsCreateCompanyLocationRequest, OptionalLocationsCreateCompanyLocationRequest):
    pass
