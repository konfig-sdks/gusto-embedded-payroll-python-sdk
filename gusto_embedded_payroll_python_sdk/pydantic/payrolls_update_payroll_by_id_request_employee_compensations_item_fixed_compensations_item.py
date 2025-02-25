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


class PayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemFixedCompensationsItem(BaseModel):
    # The name of the compensation. This also serves as the unique, immutable identifier for this compensation.
    name: typing.Optional[str] = Field(None, alias='name')

    # The amount of the compensation for the pay period.
    amount: typing.Optional[str] = Field(None, alias='amount')

    # The UUID of the job for the compensation.
    job_uuid: typing.Optional[int] = Field(None, alias='job_uuid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
