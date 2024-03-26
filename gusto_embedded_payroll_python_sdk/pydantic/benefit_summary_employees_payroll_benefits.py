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

from gusto_embedded_payroll_python_sdk.pydantic.benefit_summary_employees_payroll_benefits_pay_period import BenefitSummaryEmployeesPayrollBenefitsPayPeriod

class BenefitSummaryEmployeesPayrollBenefits(BaseModel):
    payroll_uuid: typing.Optional[str] = Field(None, alias='payroll_uuid')

    # Whether it is regular or bonus payroll
    payroll_type: typing.Optional[str] = Field(None, alias='payroll_type')

    check_date: typing.Optional[str] = Field(None, alias='check_date')

    gross_pay: typing.Optional[str] = Field(None, alias='gross_pay')

    company_benefit_deduction: typing.Optional[str] = Field(None, alias='company_benefit_deduction')

    company_benefit_contribution: typing.Optional[str] = Field(None, alias='company_benefit_contribution')

    pay_period: typing.Optional[BenefitSummaryEmployeesPayrollBenefitsPayPeriod] = Field(None, alias='pay_period')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
