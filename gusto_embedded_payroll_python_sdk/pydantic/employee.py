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

from gusto_embedded_payroll_python_sdk.pydantic.employee_custom_field import EmployeeCustomField
from gusto_embedded_payroll_python_sdk.pydantic.garnishment import Garnishment
from gusto_embedded_payroll_python_sdk.pydantic.job import Job
from gusto_embedded_payroll_python_sdk.pydantic.paid_time_off import PaidTimeOff
from gusto_embedded_payroll_python_sdk.pydantic.termination import Termination

class Employee(BaseModel):
    # The current version of the employee. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.
    version: typing.Optional[str] = Field(None, alias='version')

    # The UUID of the employee in Gusto.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    first_name: typing.Optional[str] = Field(None, alias='first_name')

    middle_initial: typing.Optional[typing.Optional[str]] = Field(None, alias='middle_initial')

    last_name: typing.Optional[str] = Field(None, alias='last_name')

    # The email address of the employee. This is provided to support syncing users between our system and yours. You may not use this email address for any other purpose (e.g. marketing).
    email: typing.Optional[typing.Optional[str]] = Field(None, alias='email')

    # The UUID of the company the employee is employed by.
    company_uuid: typing.Optional[str] = Field(None, alias='company_uuid')

    # The UUID of the employee's manager.
    manager_uuid: typing.Optional[str] = Field(None, alias='manager_uuid')

    # The employee's department in the company.
    department: typing.Optional[typing.Optional[str]] = Field(None, alias='department')

    # Whether the employee is terminated.
    terminated: typing.Optional[bool] = Field(None, alias='terminated')

    # Whether the employee is a two percent shareholder of the company. This field only applies to companies with an S-Corp entity type.
    two_percent_shareholder: typing.Optional[bool] = Field(None, alias='two_percent_shareholder')

    # Whether the employee has completed onboarding.
    onboarded: typing.Optional[bool] = Field(None, alias='onboarded')

    # The current onboarding status of the employee
    onboarding_status: typing.Optional[Literal["onboarding_completed", "admin_onboarding_incomplete", "self_onboarding_pending_invite", "self_onboarding_invited", "self_onboarding_invited_started", "self_onboarding_invited_overdue", "self_onboarding_completed_by_employee", "self_onboarding_awaiting_admin_review"]] = Field(None, alias='onboarding_status')

    jobs: typing.Optional[typing.List[Job]] = Field(None, alias='jobs')

    eligible_paid_time_off: typing.Optional[typing.List[PaidTimeOff]] = Field(None, alias='eligible_paid_time_off')

    terminations: typing.Optional[typing.List[Termination]] = Field(None, alias='terminations')

    garnishments: typing.Optional[typing.List[Garnishment]] = Field(None, alias='garnishments')

    # Custom fields are only included for the employee if the include param has the custom_fields value set
    custom_fields: typing.Optional[typing.List[EmployeeCustomField]] = Field(None, alias='custom_fields')

    date_of_birth: typing.Optional[typing.Optional[str]] = Field(None, alias='date_of_birth')

    # Indicates whether the employee has an SSN in Gusto.
    has_ssn: typing.Optional[bool] = Field(None, alias='has_ssn')

    # Deprecated. This field always returns an empty string.
    ssn: typing.Optional[str] = Field(None, alias='ssn')

    phone: typing.Optional[str] = Field(None, alias='phone')

    preferred_first_name: typing.Optional[str] = Field(None, alias='preferred_first_name')

    # The employee's payment method
    payment_method: typing.Optional[Literal["Direct Deposit", "Check"]] = Field(None, alias='payment_method')

    # The work email address of the employee. This is provided to support syncing users between our system and yours. You may not use this email address for any other purpose (e.g. marketing).
    work_email: typing.Optional[typing.Optional[str]] = Field(None, alias='work_email')

    # The current employment status of the employee. Full-time employees work 30+ hours per week. Part-time employees are split into two groups: those that work 20-29 hours a week, and those that work under 20 hours a week. Variable employees have hours that vary each week. Seasonal employees are hired for 6 months of the year or less.
    current_employment_status: typing.Optional[Literal["full_time", "part_time_under_twenty_hours", "part_time_twenty_plus_hours", "variable", "seasonal"]] = Field(None, alias='current_employment_status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
