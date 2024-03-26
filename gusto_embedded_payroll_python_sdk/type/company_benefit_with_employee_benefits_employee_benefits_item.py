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

from gusto_embedded_payroll_python_sdk.type.company_benefit_with_employee_benefits_employee_benefits_item_contribution import CompanyBenefitWithEmployeeBenefitsEmployeeBenefitsItemContribution

class RequiredCompanyBenefitWithEmployeeBenefitsEmployeeBenefitsItem(TypedDict):
    pass

class OptionalCompanyBenefitWithEmployeeBenefitsEmployeeBenefitsItem(TypedDict, total=False):
    # The UUID of the employee to which the benefit belongs.
    employee_uuid: str

    # The UUID of the company benefit.
    company_benefit_uuid: str

    # Whether the employee benefit is active.
    active: bool

    # Whether the employee deduction amount should be treated as a percentage to be deducted from each payroll.
    deduct_as_percentage: bool

    # The amount to be deducted, per pay period, from the employee's pay.
    employee_deduction: str

    # The value of the company contribution
    company_contribution: str

    uuid: str

    contribution: CompanyBenefitWithEmployeeBenefitsEmployeeBenefitsItemContribution

class CompanyBenefitWithEmployeeBenefitsEmployeeBenefitsItem(RequiredCompanyBenefitWithEmployeeBenefitsEmployeeBenefitsItem, OptionalCompanyBenefitWithEmployeeBenefitsEmployeeBenefitsItem):
    pass
