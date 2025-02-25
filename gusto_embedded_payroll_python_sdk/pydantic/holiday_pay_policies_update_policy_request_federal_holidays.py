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

from gusto_embedded_payroll_python_sdk.pydantic.holiday_pay_policies_update_policy_request_federal_holidays_christmas_day import HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysChristmasDay
from gusto_embedded_payroll_python_sdk.pydantic.holiday_pay_policies_update_policy_request_federal_holidays_columbus_day import HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysColumbusDay
from gusto_embedded_payroll_python_sdk.pydantic.holiday_pay_policies_update_policy_request_federal_holidays_independence_day import HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysIndependenceDay
from gusto_embedded_payroll_python_sdk.pydantic.holiday_pay_policies_update_policy_request_federal_holidays_juneteenth import HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysJuneteenth
from gusto_embedded_payroll_python_sdk.pydantic.holiday_pay_policies_update_policy_request_federal_holidays_labor_day import HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysLaborDay
from gusto_embedded_payroll_python_sdk.pydantic.holiday_pay_policies_update_policy_request_federal_holidays_memorial_day import HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysMemorialDay
from gusto_embedded_payroll_python_sdk.pydantic.holiday_pay_policies_update_policy_request_federal_holidays_mlk_day import HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysMlkDay
from gusto_embedded_payroll_python_sdk.pydantic.holiday_pay_policies_update_policy_request_federal_holidays_new_years_day import HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysNewYearsDay
from gusto_embedded_payroll_python_sdk.pydantic.holiday_pay_policies_update_policy_request_federal_holidays_presidents_day import HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysPresidentsDay
from gusto_embedded_payroll_python_sdk.pydantic.holiday_pay_policies_update_policy_request_federal_holidays_thanksgiving import HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysThanksgiving
from gusto_embedded_payroll_python_sdk.pydantic.holiday_pay_policies_update_policy_request_federal_holidays_veterans_day import HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysVeteransDay

class HolidayPayPoliciesUpdatePolicyRequestFederalHolidays(BaseModel):
    new_years_day: typing.Optional[HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysNewYearsDay] = Field(None, alias='new_years_day')

    mlk_day: typing.Optional[HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysMlkDay] = Field(None, alias='mlk_day')

    presidents_day: typing.Optional[HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysPresidentsDay] = Field(None, alias='presidents_day')

    memorial_day: typing.Optional[HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysMemorialDay] = Field(None, alias='memorial_day')

    juneteenth: typing.Optional[HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysJuneteenth] = Field(None, alias='juneteenth')

    independence_day: typing.Optional[HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysIndependenceDay] = Field(None, alias='independence_day')

    labor_day: typing.Optional[HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysLaborDay] = Field(None, alias='labor_day')

    columbus_day: typing.Optional[HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysColumbusDay] = Field(None, alias='columbus_day')

    veterans_day: typing.Optional[HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysVeteransDay] = Field(None, alias='veterans_day')

    thanksgiving: typing.Optional[HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysThanksgiving] = Field(None, alias='thanksgiving')

    christmas_day: typing.Optional[HolidayPayPoliciesUpdatePolicyRequestFederalHolidaysChristmasDay] = Field(None, alias='christmas_day')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
