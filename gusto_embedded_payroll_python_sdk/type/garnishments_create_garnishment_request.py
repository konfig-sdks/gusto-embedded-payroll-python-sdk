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


class RequiredGarnishmentsCreateGarnishmentRequest(TypedDict):
    # The description of the garnishment.
    description: str

    # The amount of the garnishment. Either a percentage or a fixed dollar amount. Represented as a float, e.g. \"8.00\".
    amount: float

    # Whether the garnishment is court ordered.
    court_ordered: bool

class OptionalGarnishmentsCreateGarnishmentRequest(TypedDict, total=False):
    # Whether or not this garnishment is currently active.
    active: bool

    # The number of times to apply the garnishment. Ignored if recurring is true.
    times: typing.Optional[int]

    # Whether the garnishment should recur indefinitely.
    recurring: bool

    # The maximum deduction per annum. A null value indicates no maximum. Represented as a float, e.g. \"200.00\".
    annual_maximum: typing.Optional[float]

    # The maximum deduction per pay period. A null value indicates no maximum. Represented as a float, e.g. \"16.00\".
    pay_period_maximum: typing.Optional[float]

    # Whether the amount should be treated as a percentage to be deducted per pay period.
    deduct_as_percentage: bool

class GarnishmentsCreateGarnishmentRequest(RequiredGarnishmentsCreateGarnishmentRequest, OptionalGarnishmentsCreateGarnishmentRequest):
    pass
