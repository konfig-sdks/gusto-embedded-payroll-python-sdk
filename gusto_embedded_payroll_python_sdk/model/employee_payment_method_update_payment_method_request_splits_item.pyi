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


class EmployeePaymentMethodUpdatePaymentMethodRequestSplitsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            uuid = schemas.StrSchema
            name = schemas.StrSchema
            priority = schemas.IntSchema
            
            
            class split_amount(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'split_amount':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "uuid": uuid,
                "name": name,
                "priority": priority,
                "split_amount": split_amount,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["split_amount"]) -> MetaOapg.properties.split_amount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["uuid", "name", "priority", "split_amount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> typing.Union[MetaOapg.properties.priority, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["split_amount"]) -> typing.Union[MetaOapg.properties.split_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uuid", "name", "priority", "split_amount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        uuid: typing.Union[MetaOapg.properties.uuid, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        priority: typing.Union[MetaOapg.properties.priority, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        split_amount: typing.Union[MetaOapg.properties.split_amount, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeePaymentMethodUpdatePaymentMethodRequestSplitsItem':
        return super().__new__(
            cls,
            *args,
            uuid=uuid,
            name=name,
            priority=priority,
            split_amount=split_amount,
            _configuration=_configuration,
            **kwargs,
        )
