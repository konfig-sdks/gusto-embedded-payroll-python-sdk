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


class RequiredPaySchedulesUpdatePayScheduleRequest(TypedDict):
    # The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field.
    version: str

class OptionalPaySchedulesUpdatePayScheduleRequest(TypedDict, total=False):
    # The frequency that employees on this pay schedule are paid with Gusto.
    frequency: str

    # The first date that employees on this pay schedule are paid with Gusto.
    anchor_pay_date: str

    # The last date of the first pay period. This can be the same date as the anchor pay date.
    anchor_end_of_pay_period: str

    # An integer between 1 and 31 indicating the first day of the month that employees are paid. This field is only relevant for pay schedules with the “Twice per month” and “Monthly” frequencies. It will be null for pay schedules with other frequencies.
    day_1: typing.Optional[int]

    # An integer between 1 and 31 indicating the second day of the month that employees are paid. This field is the second pay date for pay schedules with the \"Twice per month\" frequency. For semi-monthly pay schedules, set this field to 31. For months shorter than 31 days, we will set the second pay date to the last day of the month. It will be null for pay schedules with other frequencies.
    day_2: typing.Optional[int]

    # A custom pay schedule name.
    custom_name: str

    # With Autopilot® enabled, payroll will run automatically one day before your payroll deadlines.
    auto_pilot: bool

class PaySchedulesUpdatePayScheduleRequest(RequiredPaySchedulesUpdatePayScheduleRequest, OptionalPaySchedulesUpdatePayScheduleRequest):
    pass
