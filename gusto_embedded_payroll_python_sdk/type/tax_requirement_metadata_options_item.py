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


class RequiredTaxRequirementMetadataOptionsItem(TypedDict):
    # A customer facing label for the answer
    label: str

    # The actual value to be submitted
    value: str

class OptionalTaxRequirementMetadataOptionsItem(TypedDict, total=False):
    # A less verbose label that may sometimes be available
    short_label: str

class TaxRequirementMetadataOptionsItem(RequiredTaxRequirementMetadataOptionsItem, OptionalTaxRequirementMetadataOptionsItem):
    pass
