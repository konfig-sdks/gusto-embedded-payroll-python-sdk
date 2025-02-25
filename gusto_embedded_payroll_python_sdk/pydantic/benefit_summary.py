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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from gusto_embedded_payroll_python_sdk.pydantic.benefit_summary_employees import BenefitSummaryEmployees

class BenefitSummary(BaseModel):
    # Description of the benefit.
    description: typing.Optional[str] = Field(None, alias='description')

    # The start date of benefit summary.
    start_date: typing.Optional[str] = Field(None, alias='start_date')

    # The end date of benefit summary.
    end_date: typing.Optional[str] = Field(None, alias='end_date')

    # The aggregate of employee deduction for all employees given the period of time and benefit type.
    company_benefit_deduction: typing.Optional[str] = Field(None, alias='company_benefit_deduction')

    # The aggregate of company contribution for all employees given the period of time and benefit type.
    company_benefit_contribution: typing.Optional[str] = Field(None, alias='company_benefit_contribution')

    employees: typing.Optional[BenefitSummaryEmployees] = Field(None, alias='employees')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
