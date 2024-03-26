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


class EmployeeEmploymentsGetHistoryResponse(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['EmployeeEmploymentsGetHistoryResponseItem']:
            return EmployeeEmploymentsGetHistoryResponseItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['EmployeeEmploymentsGetHistoryResponseItem'], typing.List['EmployeeEmploymentsGetHistoryResponseItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'EmployeeEmploymentsGetHistoryResponse':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'EmployeeEmploymentsGetHistoryResponseItem':
        return super().__getitem__(i)

from gusto_embedded_payroll_python_sdk.model.employee_employments_get_history_response_item import EmployeeEmploymentsGetHistoryResponseItem
