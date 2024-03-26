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


class NotificationResourcesItem(BaseModel):
    # The type of entity being described, could be “Contractor”, “Employee”, “BankAccount”, “Payroll”, “ContractorPayment”, “RecoveryCase”, or “Signatory”
    entity_type: str = Field(alias='entity_type')

    # Unique identifier of the entity
    entity_uuid: str = Field(alias='entity_uuid')

    # Optional. The type of a resource that is related to the one described by entity_type and entity_uuid. For instance, if the entity_type is “BankAccount”, the reference_type could be the “Employee” or “Contractor” to whom the bank account belongs.
    reference_type: typing.Optional[str] = Field(None, alias='reference_type')

    # Optional. Unique identifier of the reference.
    reference_uuid: typing.Optional[str] = Field(None, alias='reference_uuid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
