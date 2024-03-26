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

from gusto_embedded_payroll_python_sdk.type.employee_custom_field import EmployeeCustomField

class RequiredEmployeesGetCustomFieldsResponse(TypedDict):
    pass

class OptionalEmployeesGetCustomFieldsResponse(TypedDict, total=False):
    custom_fields: typing.List[EmployeeCustomField]

class EmployeesGetCustomFieldsResponse(RequiredEmployeesGetCustomFieldsResponse, OptionalEmployeesGetCustomFieldsResponse):
    pass
