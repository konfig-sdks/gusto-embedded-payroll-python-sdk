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


class RequiredCompaniesCreatePartnerManagedCompanyResponse(TypedDict):
    pass

class OptionalCompaniesCreatePartnerManagedCompanyResponse(TypedDict, total=False):
    # Access token that can be used for OAuth access to the account. Access tokens expire 2 hours after they are issued.
    access_token: str

    # Refresh token that can be exchanged for a new access token.
    refresh_token: str

    # Gusto’s UUID for the company
    company_uuid: str

    # Time of access_token expiration in seconds
    expires_in: int

class CompaniesCreatePartnerManagedCompanyResponse(RequiredCompaniesCreatePartnerManagedCompanyResponse, OptionalCompaniesCreatePartnerManagedCompanyResponse):
    pass
