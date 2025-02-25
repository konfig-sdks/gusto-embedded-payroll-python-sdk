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


class RequiredCompaniesCreatePartnerManagedCompanyRequestCompany(TypedDict):
    # The legal name of the company.
    name: str

class OptionalCompaniesCreatePartnerManagedCompanyRequestCompany(TypedDict, total=False):
    # The name of the company.
    trade_name: str

    # The employer identification number (EIN) of the company.
    ein: str

class CompaniesCreatePartnerManagedCompanyRequestCompany(RequiredCompaniesCreatePartnerManagedCompanyRequestCompany, OptionalCompaniesCreatePartnerManagedCompanyRequestCompany):
    pass
