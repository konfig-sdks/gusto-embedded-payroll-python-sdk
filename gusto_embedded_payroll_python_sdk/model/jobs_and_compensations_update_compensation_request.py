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


class JobsAndCompensationsUpdateCompensationRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "version",
        }
        
        class properties:
            version = schemas.StrSchema
            rate = schemas.StrSchema
            
            
            class payment_unit(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Hour": "HOUR",
                        "Week": "WEEK",
                        "Month": "MONTH",
                        "Year": "YEAR",
                        "Paycheck": "PAYCHECK",
                    }
                
                @schemas.classproperty
                def HOUR(cls):
                    return cls("Hour")
                
                @schemas.classproperty
                def WEEK(cls):
                    return cls("Week")
                
                @schemas.classproperty
                def MONTH(cls):
                    return cls("Month")
                
                @schemas.classproperty
                def YEAR(cls):
                    return cls("Year")
                
                @schemas.classproperty
                def PAYCHECK(cls):
                    return cls("Paycheck")
        
            @staticmethod
            def flsa_status() -> typing.Type['FlsaStatusType']:
                return FlsaStatusType
            adjust_for_minimum_wage = schemas.BoolSchema
        
            @staticmethod
            def minimum_wages() -> typing.Type['JobsAndCompensationsUpdateCompensationRequestMinimumWages']:
                return JobsAndCompensationsUpdateCompensationRequestMinimumWages
            __annotations__ = {
                "version": version,
                "rate": rate,
                "payment_unit": payment_unit,
                "flsa_status": flsa_status,
                "adjust_for_minimum_wage": adjust_for_minimum_wage,
                "minimum_wages": minimum_wages,
            }
    
    version: MetaOapg.properties.version
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rate"]) -> MetaOapg.properties.rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_unit"]) -> MetaOapg.properties.payment_unit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flsa_status"]) -> 'FlsaStatusType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["adjust_for_minimum_wage"]) -> MetaOapg.properties.adjust_for_minimum_wage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minimum_wages"]) -> 'JobsAndCompensationsUpdateCompensationRequestMinimumWages': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "rate", "payment_unit", "flsa_status", "adjust_for_minimum_wage", "minimum_wages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rate"]) -> typing.Union[MetaOapg.properties.rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_unit"]) -> typing.Union[MetaOapg.properties.payment_unit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flsa_status"]) -> typing.Union['FlsaStatusType', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["adjust_for_minimum_wage"]) -> typing.Union[MetaOapg.properties.adjust_for_minimum_wage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minimum_wages"]) -> typing.Union['JobsAndCompensationsUpdateCompensationRequestMinimumWages', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "rate", "payment_unit", "flsa_status", "adjust_for_minimum_wage", "minimum_wages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        version: typing.Union[MetaOapg.properties.version, str, ],
        rate: typing.Union[MetaOapg.properties.rate, str, schemas.Unset] = schemas.unset,
        payment_unit: typing.Union[MetaOapg.properties.payment_unit, str, schemas.Unset] = schemas.unset,
        flsa_status: typing.Union['FlsaStatusType', schemas.Unset] = schemas.unset,
        adjust_for_minimum_wage: typing.Union[MetaOapg.properties.adjust_for_minimum_wage, bool, schemas.Unset] = schemas.unset,
        minimum_wages: typing.Union['JobsAndCompensationsUpdateCompensationRequestMinimumWages', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JobsAndCompensationsUpdateCompensationRequest':
        return super().__new__(
            cls,
            *args,
            version=version,
            rate=rate,
            payment_unit=payment_unit,
            flsa_status=flsa_status,
            adjust_for_minimum_wage=adjust_for_minimum_wage,
            minimum_wages=minimum_wages,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.flsa_status_type import FlsaStatusType
from gusto_embedded_payroll_python_sdk.model.jobs_and_compensations_update_compensation_request_minimum_wages import JobsAndCompensationsUpdateCompensationRequestMinimumWages
