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

from gusto_embedded_payroll_python_sdk.pydantic.external_payrolls_update_payroll_items_request_external_payroll_items import ExternalPayrollsUpdatePayrollItemsRequestExternalPayrollItems

class ExternalPayrollsUpdatePayrollItemsRequest(BaseModel):
    # Patch update external payroll items when set to true, otherwise it will overwrite the previous changes.
    replace_fields: typing.Optional[bool] = Field(None, alias='replace_fields')

    external_payroll_items: typing.Optional[ExternalPayrollsUpdatePayrollItemsRequestExternalPayrollItems] = Field(None, alias='external_payroll_items')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
