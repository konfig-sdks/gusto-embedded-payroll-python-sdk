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

from gusto_embedded_payroll_python_sdk.pydantic.holiday_pay_policies_update_policy_request_federal_holidays import HolidayPayPoliciesUpdatePolicyRequestFederalHolidays

class HolidayPayPoliciesUpdatePolicyRequest(BaseModel):
    # The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.
    version: str = Field(alias='version')

    federal_holidays: typing.Optional[HolidayPayPoliciesUpdatePolicyRequestFederalHolidays] = Field(None, alias='federal_holidays')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
