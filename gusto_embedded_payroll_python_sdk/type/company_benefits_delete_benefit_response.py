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

from gusto_embedded_payroll_python_sdk.type.company_benefits_delete_benefit_response_errors import CompanyBenefitsDeleteBenefitResponseErrors

class RequiredCompanyBenefitsDeleteBenefitResponse(TypedDict):
    pass

class OptionalCompanyBenefitsDeleteBenefitResponse(TypedDict, total=False):
    errors: CompanyBenefitsDeleteBenefitResponseErrors

class CompanyBenefitsDeleteBenefitResponse(RequiredCompanyBenefitsDeleteBenefitResponse, OptionalCompanyBenefitsDeleteBenefitResponse):
    pass
