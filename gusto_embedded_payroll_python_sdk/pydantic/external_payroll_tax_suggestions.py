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

from gusto_embedded_payroll_python_sdk.pydantic.external_payroll_tax_suggestions_tax_suggestions import ExternalPayrollTaxSuggestionsTaxSuggestions

class ExternalPayrollTaxSuggestions(BaseModel):
    # The UUID of the employee.
    employee_uuid: typing.Optional[str] = Field(None, alias='employee_uuid')

    tax_suggestions: typing.Optional[ExternalPayrollTaxSuggestionsTaxSuggestions] = Field(None, alias='tax_suggestions')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
