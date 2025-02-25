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


class EmployeeEmploymentsGetHistoryResponseItem(BaseModel):
    # The employee's start day of work for an employment.
    hire_date: typing.Optional[str] = Field(None, alias='hire_date')

    # The employee's last day of work for an employment.
    termination_date: typing.Optional[str] = Field(None, alias='termination_date')

    # The boolean flag indicating whether Gusto will file a new hire report for the employee.
    file_new_hire_report: typing.Optional[bool] = Field(None, alias='file_new_hire_report')

    # Whether the employee is a two percent shareholder of the company. This field only applies to companies with an S-Corp entity type.
    two_percent_shareholder: typing.Optional[bool] = Field(None, alias='two_percent_shareholder')

    # The employee's employment status. Supplying an invalid option will set the employment_status to *not_set*.
    employment_status: typing.Optional[Literal["part_time", "full_time", "part_time_eligible", "variable", "seasonal", "not_set"]] = Field(None, alias='employment_status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
