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


class ContractorPaymentSummaryTotal(BaseModel):
    # The total reimbursements for contractor payments within a given time period.
    reimbursements: typing.Optional[str] = Field(None, alias='reimbursements')

    # The total wages for contractor payments within a given time period.
    wages: typing.Optional[str] = Field(None, alias='wages')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
