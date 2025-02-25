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


class ExternalPayrollApplicableEarningsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            earning_type = schemas.StrSchema
            earning_id = schemas.NumberSchema
            name = schemas.StrSchema
            input_type = schemas.StrSchema
            category = schemas.StrSchema
            __annotations__ = {
                "earning_type": earning_type,
                "earning_id": earning_id,
                "name": name,
                "input_type": input_type,
                "category": category,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["earning_type"]) -> MetaOapg.properties.earning_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["earning_id"]) -> MetaOapg.properties.earning_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["input_type"]) -> MetaOapg.properties.input_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["earning_type", "earning_id", "name", "input_type", "category", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["earning_type"]) -> typing.Union[MetaOapg.properties.earning_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["earning_id"]) -> typing.Union[MetaOapg.properties.earning_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["input_type"]) -> typing.Union[MetaOapg.properties.input_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["earning_type", "earning_id", "name", "input_type", "category", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        earning_type: typing.Union[MetaOapg.properties.earning_type, str, schemas.Unset] = schemas.unset,
        earning_id: typing.Union[MetaOapg.properties.earning_id, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        input_type: typing.Union[MetaOapg.properties.input_type, str, schemas.Unset] = schemas.unset,
        category: typing.Union[MetaOapg.properties.category, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExternalPayrollApplicableEarningsItem':
        return super().__new__(
            cls,
            *args,
            earning_type=earning_type,
            earning_id=earning_id,
            name=name,
            input_type=input_type,
            category=category,
            _configuration=_configuration,
            **kwargs,
        )
