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

from gusto_embedded_payroll_python_sdk.type.tax_requirements_update_state_taxes_request_requirement_sets import TaxRequirementsUpdateStateTaxesRequestRequirementSets

class RequiredTaxRequirementsUpdateStateTaxesRequest(TypedDict):
    pass

class OptionalTaxRequirementsUpdateStateTaxesRequest(TypedDict, total=False):
    requirement_sets: TaxRequirementsUpdateStateTaxesRequestRequirementSets

class TaxRequirementsUpdateStateTaxesRequest(RequiredTaxRequirementsUpdateStateTaxesRequest, OptionalTaxRequirementsUpdateStateTaxesRequest):
    pass
