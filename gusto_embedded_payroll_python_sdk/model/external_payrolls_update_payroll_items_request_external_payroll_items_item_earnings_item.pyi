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


class ExternalPayrollsUpdatePayrollItemsRequestExternalPayrollItemsItemEarningsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An array of earnings for the employee. Depends on your company selections, earnings includes wages, hours, bonuses, tips, commission and more.
    """


    class MetaOapg:
        
        class properties:
            hours = schemas.StrSchema
            amount = schemas.StrSchema
            earning_id = schemas.IntSchema
            
            
            class earning_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def COMPANY_PAY_TYPE(cls):
                    return cls("CompanyPayType")
                
                @schemas.classproperty
                def COMPANY_EARNING_TYPE(cls):
                    return cls("CompanyEarningType")
            __annotations__ = {
                "hours": hours,
                "amount": amount,
                "earning_id": earning_id,
                "earning_type": earning_type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hours"]) -> MetaOapg.properties.hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["earning_id"]) -> MetaOapg.properties.earning_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["earning_type"]) -> MetaOapg.properties.earning_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hours", "amount", "earning_id", "earning_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hours"]) -> typing.Union[MetaOapg.properties.hours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["earning_id"]) -> typing.Union[MetaOapg.properties.earning_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["earning_type"]) -> typing.Union[MetaOapg.properties.earning_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hours", "amount", "earning_id", "earning_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        hours: typing.Union[MetaOapg.properties.hours, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, str, schemas.Unset] = schemas.unset,
        earning_id: typing.Union[MetaOapg.properties.earning_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        earning_type: typing.Union[MetaOapg.properties.earning_type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExternalPayrollsUpdatePayrollItemsRequestExternalPayrollItemsItemEarningsItem':
        return super().__new__(
            cls,
            *args,
            hours=hours,
            amount=amount,
            earning_id=earning_id,
            earning_type=earning_type,
            _configuration=_configuration,
            **kwargs,
        )
