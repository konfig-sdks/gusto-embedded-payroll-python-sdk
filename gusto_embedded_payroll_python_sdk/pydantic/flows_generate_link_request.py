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


class FlowsGenerateLinkRequest(BaseModel):
    # flow type
    flow_type: str = Field(alias='flow_type')

    # UUID of the target entity applicable to the flow. This field is optional for company flows, please refer to the flow_types table above for more details.
    entity_uuid: typing.Optional[str] = Field(None, alias='entity_uuid')

    # the type of target entity applicable to the flow. This field is optional for company flows, please refer to the flow_types table above for more details.
    entity_type: typing.Optional[Literal["Company", "Employee"]] = Field(None, alias='entity_type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
