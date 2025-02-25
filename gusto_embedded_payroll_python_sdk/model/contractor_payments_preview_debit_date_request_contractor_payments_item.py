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


class ContractorPaymentsPreviewDebitDateRequestContractorPaymentsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            bonus = schemas.IntSchema
            contractor_uuid = schemas.StrSchema
            date = schemas.StrSchema
            hourly_rate = schemas.IntSchema
            hours = schemas.IntSchema
            payment_method = schemas.StrSchema
            reimbursement = schemas.IntSchema
            wage = schemas.IntSchema
            __annotations__ = {
                "bonus": bonus,
                "contractor_uuid": contractor_uuid,
                "date": date,
                "hourly_rate": hourly_rate,
                "hours": hours,
                "payment_method": payment_method,
                "reimbursement": reimbursement,
                "wage": wage,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bonus"]) -> MetaOapg.properties.bonus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractor_uuid"]) -> MetaOapg.properties.contractor_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hourly_rate"]) -> MetaOapg.properties.hourly_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hours"]) -> MetaOapg.properties.hours: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_method"]) -> MetaOapg.properties.payment_method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reimbursement"]) -> MetaOapg.properties.reimbursement: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wage"]) -> MetaOapg.properties.wage: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bonus", "contractor_uuid", "date", "hourly_rate", "hours", "payment_method", "reimbursement", "wage", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bonus"]) -> typing.Union[MetaOapg.properties.bonus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractor_uuid"]) -> typing.Union[MetaOapg.properties.contractor_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hourly_rate"]) -> typing.Union[MetaOapg.properties.hourly_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hours"]) -> typing.Union[MetaOapg.properties.hours, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_method"]) -> typing.Union[MetaOapg.properties.payment_method, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reimbursement"]) -> typing.Union[MetaOapg.properties.reimbursement, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wage"]) -> typing.Union[MetaOapg.properties.wage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bonus", "contractor_uuid", "date", "hourly_rate", "hours", "payment_method", "reimbursement", "wage", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bonus: typing.Union[MetaOapg.properties.bonus, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        contractor_uuid: typing.Union[MetaOapg.properties.contractor_uuid, str, schemas.Unset] = schemas.unset,
        date: typing.Union[MetaOapg.properties.date, str, schemas.Unset] = schemas.unset,
        hourly_rate: typing.Union[MetaOapg.properties.hourly_rate, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        hours: typing.Union[MetaOapg.properties.hours, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        payment_method: typing.Union[MetaOapg.properties.payment_method, str, schemas.Unset] = schemas.unset,
        reimbursement: typing.Union[MetaOapg.properties.reimbursement, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        wage: typing.Union[MetaOapg.properties.wage, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ContractorPaymentsPreviewDebitDateRequestContractorPaymentsItem':
        return super().__new__(
            cls,
            *args,
            bonus=bonus,
            contractor_uuid=contractor_uuid,
            date=date,
            hourly_rate=hourly_rate,
            hours=hours,
            payment_method=payment_method,
            reimbursement=reimbursement,
            wage=wage,
            _configuration=_configuration,
            **kwargs,
        )
