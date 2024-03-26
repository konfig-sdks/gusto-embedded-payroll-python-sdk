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

from gusto_embedded_payroll_python_sdk.pydantic.invoice_data_active_companies import InvoiceDataActiveCompanies

class InvoiceData(BaseModel):
    active_companies: typing.Optional[InvoiceDataActiveCompanies] = Field(None, alias='active_companies')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
