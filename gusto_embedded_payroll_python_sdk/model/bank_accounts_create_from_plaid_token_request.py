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


class BankAccountsCreateFromPlaidTokenRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "owner_id",
            "processor_token",
            "owner_type",
        }
        
        class properties:
            
            
            class owner_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Company": "COMPANY",
                    }
                
                @schemas.classproperty
                def COMPANY(cls):
                    return cls("Company")
            owner_id = schemas.StrSchema
            processor_token = schemas.StrSchema
            __annotations__ = {
                "owner_type": owner_type,
                "owner_id": owner_id,
                "processor_token": processor_token,
            }
    
    owner_id: MetaOapg.properties.owner_id
    processor_token: MetaOapg.properties.processor_token
    owner_type: MetaOapg.properties.owner_type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner_type"]) -> MetaOapg.properties.owner_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["owner_id"]) -> MetaOapg.properties.owner_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["processor_token"]) -> MetaOapg.properties.processor_token: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["owner_type", "owner_id", "processor_token", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner_type"]) -> MetaOapg.properties.owner_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["owner_id"]) -> MetaOapg.properties.owner_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["processor_token"]) -> MetaOapg.properties.processor_token: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["owner_type", "owner_id", "processor_token", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        owner_id: typing.Union[MetaOapg.properties.owner_id, str, ],
        processor_token: typing.Union[MetaOapg.properties.processor_token, str, ],
        owner_type: typing.Union[MetaOapg.properties.owner_type, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BankAccountsCreateFromPlaidTokenRequest':
        return super().__new__(
            cls,
            *args,
            owner_id=owner_id,
            processor_token=processor_token,
            owner_type=owner_type,
            _configuration=_configuration,
            **kwargs,
        )
