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


class RequiredEmployeeTaxSetupUpdateFederalTaxesRequest(TypedDict):
    # The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.
    version: str

class OptionalEmployeeTaxSetupUpdateFederalTaxesRequest(TypedDict, total=False):
    filing_status: str

    extra_withholding: typing.Optional[str]

    two_jobs: bool

    dependents_amount: str

    other_income: str

    deductions: str

    w4_data_type: str

class EmployeeTaxSetupUpdateFederalTaxesRequest(RequiredEmployeeTaxSetupUpdateFederalTaxesRequest, OptionalEmployeeTaxSetupUpdateFederalTaxesRequest):
    pass
