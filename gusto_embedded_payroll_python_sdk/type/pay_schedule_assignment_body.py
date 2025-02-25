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

from gusto_embedded_payroll_python_sdk.type.pay_schedule_assignment_body_departments import PayScheduleAssignmentBodyDepartments
from gusto_embedded_payroll_python_sdk.type.pay_schedule_assignment_body_employees import PayScheduleAssignmentBodyEmployees

class RequiredPayScheduleAssignmentBody(TypedDict):
    # The pay schedule assignment type.
    type: str

class OptionalPayScheduleAssignmentBody(TypedDict, total=False):
    # Pay schedule for hourly employees.
    hourly_pay_schedule_uuid: str

    # Pay schedule for salaried employees.
    salaried_pay_schedule_uuid: str

    # Default pay schedule for employees.
    default_pay_schedule_uuid: str

    employees: PayScheduleAssignmentBodyEmployees

    departments: PayScheduleAssignmentBodyDepartments

class PayScheduleAssignmentBody(RequiredPayScheduleAssignmentBody, OptionalPayScheduleAssignmentBody):
    pass
