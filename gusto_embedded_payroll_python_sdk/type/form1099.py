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


class RequiredForm1099(TypedDict):
    pass

class OptionalForm1099(TypedDict, total=False):
    # The title of the form
    title: str

    # The description of the form
    description: str

    # The UUID of the form
    uuid: str

    # The type identifier of the form
    name: str

    # If the form is in a draft state. E.g. End of year tax forms may be provided in a draft state prior to being finalized.
    draft: bool

    # The year of this form. For some forms, e.g. tax forms, this is the year which the form represents. A 1099 for January - December 2022 would be delivered in January 2023 and have a year value of 2022. This value is nullable and will not be present on all forms.
    year: typing.Optional[int]

    # The quarter of this form. This value is currently always null since it is not present on any contractor forms.
    quarter: typing.Optional[int]

    # A boolean flag that indicates whether the form needs signing or not. Note that this value will change after the form is signed.
    requires_signing: bool

    # The contractor UUID
    contractor_uuid: str

class Form1099(RequiredForm1099, OptionalForm1099):
    pass
