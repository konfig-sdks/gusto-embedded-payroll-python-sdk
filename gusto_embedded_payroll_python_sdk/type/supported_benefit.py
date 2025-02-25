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


class RequiredSupportedBenefit(TypedDict):
    pass

class OptionalSupportedBenefit(TypedDict, total=False):
    # The description of the benefit.
    description: str

    # The benefit type in Gusto.
    benefit_type: typing.Union[int, float]

    # The name of the benefit.
    name: str

    # Whether the benefit is deducted before tax calculations, thus reducing one’s taxable income
    pretax: bool

    # Whether the benefit is deducted after tax calculations.
    posttax: bool

    # Whether the benefit is considered imputed income.
    imputed: bool

    # Whether the benefit is healthcare related.
    healthcare: bool

    # Whether the benefit is associated with retirement planning.
    retirement: bool

    # Whether the benefit has a government mandated yearly limit.
    yearly_limit: bool

    # Category where the benefit belongs to.
    category: str

class SupportedBenefit(RequiredSupportedBenefit, OptionalSupportedBenefit):
    pass
