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

from gusto_embedded_payroll_python_sdk.type.employee_benefit_contribution import EmployeeBenefitContribution

class RequiredEmployeeBenefit(TypedDict):
    pass

class OptionalEmployeeBenefit(TypedDict, total=False):
    # The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.
    version: str

    # The UUID of the employee to which the benefit belongs.
    employee_uuid: str

    # The UUID of the company benefit.
    company_benefit_uuid: str

    # Whether the employee benefit is active.
    active: bool

    # The UUID of the employee benefit.
    uuid: str

    # The amount to be deducted, per pay period, from the employee's pay.
    employee_deduction: str

    # Whether the employee deduction amount should be treated as a percentage to be deducted from each payroll.
    deduct_as_percentage: bool

    # The maximum employee deduction amount per year. A null value signifies no limit.
    employee_deduction_annual_maximum: typing.Optional[str]

    contribution: EmployeeBenefitContribution

    # Whether the company contribution is elective (aka matching). For \"tiered\" contribution types, this is always true.
    elective: bool

    # The maximum company contribution amount per year. A null value signifies no limit.
    company_contribution_annual_maximum: typing.Optional[str]

    # Some benefits require additional information to determine their limit. For example, for an HSA benefit, the limit option should be either \"Family\" or \"Individual\". For a Dependent Care FSA benefit, the limit option should be either \"Joint Filing or Single\" or \"Married and Filing Separately\".
    limit_option: typing.Optional[str]

    # Whether the employee should use a benefit’s \"catch up\" rate. Only Roth 401k and 401k benefits use this value for employees over 50.
    catch_up: bool

    # Identifier for a 401(k) loan assigned by the 401(k) provider
    retirement_loan_identifier: str

    # The amount that the employee is insured for. Note: company contribution cannot be present if coverage amount is set.
    coverage_amount: typing.Optional[str]

    # Whether the employee deduction reduces taxable income or not. Only valid for Group Term Life benefits. Note: when the value is not \"unset\", coverage amount and coverage salary multiplier are ignored.
    deduction_reduces_taxable_income: typing.Optional[str]

    # The coverage amount as a multiple of the employee’s salary. Only applicable for Group Term Life benefits. Note: cannot be set if coverage amount is also set.
    coverage_salary_multiplier: str

    # WARNING: This property is deprecated
    # The amount to be paid, per pay period, by the company. This field will not appear for tiered contribution types.
    company_contribution: str

    # WARNING: This property is deprecated
    # Whether the company_contribution value should be treated as a percentage to be added to each payroll. This field will not appear for tiered contribution types.
    contribute_as_percentage: bool

class EmployeeBenefit(RequiredEmployeeBenefit, OptionalEmployeeBenefit):
    pass
