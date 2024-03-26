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


class CompanyBenefitWithEmployeeBenefitsEmployeeBenefitsItemContribution(BaseModel):
    # The company contribution scheme.  \"amount\": The company contributes a fixed amount per payroll. If elective is true, the contribution is matching, dollar-for-dollar.  \"percentage\": The company contributes a percentage of the payroll amount per payroll period. If elective is true, the contribution is matching, dollar-for-dollar.  \"tiered\": The company contribution varies according to the size of the employee deduction.
    type: typing.Optional[str] = Field(None, alias='type')

    # For the `amount` and `percentage` contribution types, the value of the corresponding amount or percentage.  For the `tiered` contribution type, an array of tiers.
    value: typing.Optional[typing.Union[str, typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='value')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
