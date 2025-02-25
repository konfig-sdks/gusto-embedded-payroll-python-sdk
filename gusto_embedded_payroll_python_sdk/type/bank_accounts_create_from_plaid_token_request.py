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


class RequiredBankAccountsCreateFromPlaidTokenRequest(TypedDict):
    # The owner type of the bank account
    owner_type: str

    # The owner uuid of the bank account
    owner_id: str

    # The Plaid processor token
    processor_token: str

class OptionalBankAccountsCreateFromPlaidTokenRequest(TypedDict, total=False):
    pass

class BankAccountsCreateFromPlaidTokenRequest(RequiredBankAccountsCreateFromPlaidTokenRequest, OptionalBankAccountsCreateFromPlaidTokenRequest):
    pass
