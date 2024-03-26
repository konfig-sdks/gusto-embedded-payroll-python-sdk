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


class EmployeePaymentMethodUpdatePaymentMethodRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "type",
            "version",
        }
        
        class properties:
            version = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Direct Deposit": "DIRECT_DEPOSIT",
                        "Check": "CHECK",
                    }
                
                @schemas.classproperty
                def DIRECT_DEPOSIT(cls):
                    return cls("Direct Deposit")
                
                @schemas.classproperty
                def CHECK(cls):
                    return cls("Check")
            
            
            class split_by(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Amount": "AMOUNT",
                        "Percentage": "PERCENTAGE",
                    }
                
                @schemas.classproperty
                def AMOUNT(cls):
                    return cls("Amount")
                
                @schemas.classproperty
                def PERCENTAGE(cls):
                    return cls("Percentage")
        
            @staticmethod
            def splits() -> typing.Type['EmployeePaymentMethodUpdatePaymentMethodRequestSplits']:
                return EmployeePaymentMethodUpdatePaymentMethodRequestSplits
            __annotations__ = {
                "version": version,
                "type": type,
                "split_by": split_by,
                "splits": splits,
            }
    
    type: MetaOapg.properties.type
    version: MetaOapg.properties.version
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["split_by"]) -> MetaOapg.properties.split_by: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["splits"]) -> 'EmployeePaymentMethodUpdatePaymentMethodRequestSplits': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "type", "split_by", "splits", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["split_by"]) -> typing.Union[MetaOapg.properties.split_by, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["splits"]) -> typing.Union['EmployeePaymentMethodUpdatePaymentMethodRequestSplits', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "type", "split_by", "splits", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        version: typing.Union[MetaOapg.properties.version, str, ],
        split_by: typing.Union[MetaOapg.properties.split_by, str, schemas.Unset] = schemas.unset,
        splits: typing.Union['EmployeePaymentMethodUpdatePaymentMethodRequestSplits', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeePaymentMethodUpdatePaymentMethodRequest':
        return super().__new__(
            cls,
            *args,
            type=type,
            version=version,
            split_by=split_by,
            splits=splits,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.employee_payment_method_update_payment_method_request_splits import EmployeePaymentMethodUpdatePaymentMethodRequestSplits
