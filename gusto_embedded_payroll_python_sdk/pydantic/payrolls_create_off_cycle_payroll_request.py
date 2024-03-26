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

from gusto_embedded_payroll_python_sdk.pydantic.payrolls_create_off_cycle_payroll_request_employee_uuids import PayrollsCreateOffCyclePayrollRequestEmployeeUuids

class PayrollsCreateOffCyclePayrollRequest(BaseModel):
    # Whether it is an off cycle payroll.
    off_cycle: bool = Field(alias='off_cycle')

    # An off cycle payroll reason. Select one from the following list.
    off_cycle_reason: Literal["Bonus", "Correction", "Dismissed employee", "Transition from old pay schedule"] = Field(alias='off_cycle_reason')

    # Pay period start date.
    start_date: str = Field(alias='start_date')

    # Pay period end date.
    end_date: str = Field(alias='end_date')

    # A pay schedule is required for Transition from old pay schedule payroll to identify the matching transition pay period.
    pay_schedule_uuid: typing.Optional[str] = Field(None, alias='pay_schedule_uuid')

    employee_uuids: typing.Optional[PayrollsCreateOffCyclePayrollRequestEmployeeUuids] = Field(None, alias='employee_uuids')

    # Payment date.
    check_date: typing.Optional[str] = Field(None, alias='check_date')

    # The payment schedule tax rate the payroll is based on
    withholding_pay_period: typing.Optional[Literal["Every week", "Every other week", "Twice per month", "Monthly", "Quarterly", "Semiannually", "Annually"]] = Field(None, alias='withholding_pay_period')

    # Block regular deductions and contributions for this payroll.
    skip_regular_deductions: typing.Optional[bool] = Field(None, alias='skip_regular_deductions')

    # Enable taxes to be withheld at the IRS's required rate of 22% for federal income taxes. State income taxes will be taxed at the state's supplemental tax rate. Otherwise, we'll sum the entirety of the employee's wages and withhold taxes on the entire amount at the rate for regular wages.
    fixed_withholding_rate: typing.Optional[bool] = Field(None, alias='fixed_withholding_rate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
