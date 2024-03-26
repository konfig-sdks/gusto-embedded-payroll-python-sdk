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

from gusto_embedded_payroll_python_sdk.type.company_primary_signatory_home_address import CompanyPrimarySignatoryHomeAddress

class RequiredCompanyPrimarySignatory(TypedDict):
    pass

class OptionalCompanyPrimarySignatory(TypedDict, total=False):
    first_name: str

    middle_initial: str

    last_name: str

    phone: str

    email: str

    home_address: CompanyPrimarySignatoryHomeAddress

class CompanyPrimarySignatory(RequiredCompanyPrimarySignatory, OptionalCompanyPrimarySignatory):
    pass
