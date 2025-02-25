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

from gusto_embedded_payroll_python_sdk.pydantic.tax_requirements_update_state_taxes_request_requirement_sets import TaxRequirementsUpdateStateTaxesRequestRequirementSets

class TaxRequirementsUpdateStateTaxesRequest(BaseModel):
    requirement_sets: typing.Optional[TaxRequirementsUpdateStateTaxesRequestRequirementSets] = Field(None, alias='requirement_sets')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
