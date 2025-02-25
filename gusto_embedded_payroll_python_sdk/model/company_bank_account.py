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


class CompanyBankAccount(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The company bank account
    """


    class MetaOapg:
        
        class properties:
            uuid = schemas.StrSchema
            company_uuid = schemas.StrSchema
            
            
            class account_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Checking": "CHECKING",
                        "Savings": "SAVINGS",
                    }
                
                @schemas.classproperty
                def CHECKING(cls):
                    return cls("Checking")
                
                @schemas.classproperty
                def SAVINGS(cls):
                    return cls("Savings")
            routing_number = schemas.StrSchema
            hidden_account_number = schemas.StrSchema
            
            
            class verification_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "awaiting_deposits": "AWAITING_DEPOSITS",
                        "ready_for_verification": "READY_FOR_VERIFICATION",
                        "verified": "VERIFIED",
                    }
                
                @schemas.classproperty
                def AWAITING_DEPOSITS(cls):
                    return cls("awaiting_deposits")
                
                @schemas.classproperty
                def READY_FOR_VERIFICATION(cls):
                    return cls("ready_for_verification")
                
                @schemas.classproperty
                def VERIFIED(cls):
                    return cls("verified")
            
            
            class verification_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "bank_deposits": "BANK_DEPOSITS",
                        "plaid": "PLAID",
                        "plaid_external": "PLAID_EXTERNAL",
                    }
                
                @schemas.classproperty
                def BANK_DEPOSITS(cls):
                    return cls("bank_deposits")
                
                @schemas.classproperty
                def PLAID(cls):
                    return cls("plaid")
                
                @schemas.classproperty
                def PLAID_EXTERNAL(cls):
                    return cls("plaid_external")
            
            
            class plaid_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "connected": "CONNECTED",
                        "disconnected": "DISCONNECTED",
                    }
                
                @schemas.classproperty
                def CONNECTED(cls):
                    return cls("connected")
                
                @schemas.classproperty
                def DISCONNECTED(cls):
                    return cls("disconnected")
            last_cached_balance = schemas.StrSchema
            balance_fetched_date = schemas.StrSchema
            name = schemas.StrSchema
            __annotations__ = {
                "uuid": uuid,
                "company_uuid": company_uuid,
                "account_type": account_type,
                "routing_number": routing_number,
                "hidden_account_number": hidden_account_number,
                "verification_status": verification_status,
                "verification_type": verification_type,
                "plaid_status": plaid_status,
                "last_cached_balance": last_cached_balance,
                "balance_fetched_date": balance_fetched_date,
                "name": name,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_uuid"]) -> MetaOapg.properties.company_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_type"]) -> MetaOapg.properties.account_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["routing_number"]) -> MetaOapg.properties.routing_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hidden_account_number"]) -> MetaOapg.properties.hidden_account_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verification_status"]) -> MetaOapg.properties.verification_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["verification_type"]) -> MetaOapg.properties.verification_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["plaid_status"]) -> MetaOapg.properties.plaid_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_cached_balance"]) -> MetaOapg.properties.last_cached_balance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balance_fetched_date"]) -> MetaOapg.properties.balance_fetched_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["uuid", "company_uuid", "account_type", "routing_number", "hidden_account_number", "verification_status", "verification_type", "plaid_status", "last_cached_balance", "balance_fetched_date", "name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_uuid"]) -> typing.Union[MetaOapg.properties.company_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_type"]) -> typing.Union[MetaOapg.properties.account_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["routing_number"]) -> typing.Union[MetaOapg.properties.routing_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hidden_account_number"]) -> typing.Union[MetaOapg.properties.hidden_account_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verification_status"]) -> typing.Union[MetaOapg.properties.verification_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["verification_type"]) -> typing.Union[MetaOapg.properties.verification_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["plaid_status"]) -> typing.Union[MetaOapg.properties.plaid_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_cached_balance"]) -> typing.Union[MetaOapg.properties.last_cached_balance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balance_fetched_date"]) -> typing.Union[MetaOapg.properties.balance_fetched_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uuid", "company_uuid", "account_type", "routing_number", "hidden_account_number", "verification_status", "verification_type", "plaid_status", "last_cached_balance", "balance_fetched_date", "name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        uuid: typing.Union[MetaOapg.properties.uuid, str, schemas.Unset] = schemas.unset,
        company_uuid: typing.Union[MetaOapg.properties.company_uuid, str, schemas.Unset] = schemas.unset,
        account_type: typing.Union[MetaOapg.properties.account_type, str, schemas.Unset] = schemas.unset,
        routing_number: typing.Union[MetaOapg.properties.routing_number, str, schemas.Unset] = schemas.unset,
        hidden_account_number: typing.Union[MetaOapg.properties.hidden_account_number, str, schemas.Unset] = schemas.unset,
        verification_status: typing.Union[MetaOapg.properties.verification_status, str, schemas.Unset] = schemas.unset,
        verification_type: typing.Union[MetaOapg.properties.verification_type, str, schemas.Unset] = schemas.unset,
        plaid_status: typing.Union[MetaOapg.properties.plaid_status, str, schemas.Unset] = schemas.unset,
        last_cached_balance: typing.Union[MetaOapg.properties.last_cached_balance, str, schemas.Unset] = schemas.unset,
        balance_fetched_date: typing.Union[MetaOapg.properties.balance_fetched_date, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompanyBankAccount':
        return super().__new__(
            cls,
            *args,
            uuid=uuid,
            company_uuid=company_uuid,
            account_type=account_type,
            routing_number=routing_number,
            hidden_account_number=hidden_account_number,
            verification_status=verification_status,
            verification_type=verification_type,
            plaid_status=plaid_status,
            last_cached_balance=last_cached_balance,
            balance_fetched_date=balance_fetched_date,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )
