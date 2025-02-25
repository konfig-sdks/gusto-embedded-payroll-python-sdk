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

from gusto_embedded_payroll_python_sdk.type.benefit_type_requirements_coverage_salary_multiplier_choices import BenefitTypeRequirementsCoverageSalaryMultiplierChoices
from gusto_embedded_payroll_python_sdk.type.benefit_type_requirements_coverage_salary_multiplier_default_value import BenefitTypeRequirementsCoverageSalaryMultiplierDefaultValue

class RequiredBenefitTypeRequirementsCoverageSalaryMultiplier(TypedDict):
    pass

class OptionalBenefitTypeRequirementsCoverageSalaryMultiplier(TypedDict, total=False):
    required: bool

    editable: bool

    default_value: BenefitTypeRequirementsCoverageSalaryMultiplierDefaultValue

    choices: BenefitTypeRequirementsCoverageSalaryMultiplierChoices

class BenefitTypeRequirementsCoverageSalaryMultiplier(RequiredBenefitTypeRequirementsCoverageSalaryMultiplier, OptionalBenefitTypeRequirementsCoverageSalaryMultiplier):
    pass
