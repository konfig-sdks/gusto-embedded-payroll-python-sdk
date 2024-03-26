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

from gusto_embedded_payroll_python_sdk.pydantic.tax_requirement_applicable_if import TaxRequirementApplicableIf
from gusto_embedded_payroll_python_sdk.pydantic.tax_requirement_metadata import TaxRequirementMetadata

class TaxRequirement(BaseModel):
    # A more detailed customer facing description of the requirement
    description: typing.Optional[str] = Field(None, alias='description')

    # An identifier for an individual requirement. Uniqueness is guaranteed within a requirement set.
    key: typing.Optional[str] = Field(None, alias='key')

    applicable_if: typing.Optional[TaxRequirementApplicableIf] = Field(None, alias='applicable_if')

    # A customer facing description of the requirement
    label: typing.Optional[str] = Field(None, alias='label')

    # The \"answer\"
    value: typing.Optional[str] = Field(None, alias='value')

    metadata: typing.Optional[TaxRequirementMetadata] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
