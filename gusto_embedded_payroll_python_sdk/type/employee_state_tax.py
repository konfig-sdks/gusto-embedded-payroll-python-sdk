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

from gusto_embedded_payroll_python_sdk.type.employee_state_tax_question import EmployeeStateTaxQuestion

class RequiredEmployeeStateTax(TypedDict):
    # The employee's uuid
    employee_uuid: str

    # Two letter US state abbreviation
    state: str

    questions: typing.List[EmployeeStateTaxQuestion]

class OptionalEmployeeStateTax(TypedDict, total=False):
    file_new_hire_report: bool

    is_work_state: bool

class EmployeeStateTax(RequiredEmployeeStateTax, OptionalEmployeeStateTax):
    pass
