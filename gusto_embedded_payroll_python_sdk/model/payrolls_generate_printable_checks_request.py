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


class PayrollsGeneratePrintableChecksRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "printing_format",
        }
        
        class properties:
            printing_format = schemas.StrSchema
            starting_check_number = schemas.IntSchema
            __annotations__ = {
                "printing_format": printing_format,
                "starting_check_number": starting_check_number,
            }
    
    printing_format: MetaOapg.properties.printing_format
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["printing_format"]) -> MetaOapg.properties.printing_format: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["starting_check_number"]) -> MetaOapg.properties.starting_check_number: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["printing_format", "starting_check_number", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["printing_format"]) -> MetaOapg.properties.printing_format: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["starting_check_number"]) -> typing.Union[MetaOapg.properties.starting_check_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["printing_format", "starting_check_number", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        printing_format: typing.Union[MetaOapg.properties.printing_format, str, ],
        starting_check_number: typing.Union[MetaOapg.properties.starting_check_number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayrollsGeneratePrintableChecksRequest':
        return super().__new__(
            cls,
            *args,
            printing_format=printing_format,
            starting_check_number=starting_check_number,
            _configuration=_configuration,
            **kwargs,
        )
