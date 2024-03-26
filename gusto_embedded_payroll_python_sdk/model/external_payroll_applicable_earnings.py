# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from gusto_embedded_payroll_python_sdk import schemas  # noqa: F401


class ExternalPayrollApplicableEarnings(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Applicable earnings based on company provisioning.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ExternalPayrollApplicableEarningsItem']:
            return ExternalPayrollApplicableEarningsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['ExternalPayrollApplicableEarningsItem'], typing.List['ExternalPayrollApplicableEarningsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ExternalPayrollApplicableEarnings':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ExternalPayrollApplicableEarningsItem':
        return super().__getitem__(i)

from gusto_embedded_payroll_python_sdk.model.external_payroll_applicable_earnings_item import ExternalPayrollApplicableEarningsItem
