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

from gusto_embedded_payroll_python_sdk.type.tax_requirement_set import TaxRequirementSet

class RequiredTaxRequirementsState(TypedDict):
    pass

class OptionalTaxRequirementsState(TypedDict, total=False):
    company_uuid: str

    # One of the two-letter state abbreviations for the fifty United States and the District of Columbia (DC)
    state: str

    requirement_sets: typing.List[TaxRequirementSet]

class TaxRequirementsState(RequiredTaxRequirementsState, OptionalTaxRequirementsState):
    pass
