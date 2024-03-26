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


class EmployeesCreateEmployeeRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "last_name",
            "first_name",
        }
        
        class properties:
            first_name = schemas.StrSchema
            last_name = schemas.StrSchema
            middle_initial = schemas.StrSchema
            date_of_birth = schemas.StrSchema
            email = schemas.StrSchema
            
            
            class ssn(
                schemas.StrSchema
            ):
                pass
            self_onboarding = schemas.BoolSchema
            __annotations__ = {
                "first_name": first_name,
                "last_name": last_name,
                "middle_initial": middle_initial,
                "date_of_birth": date_of_birth,
                "email": email,
                "ssn": ssn,
                "self_onboarding": self_onboarding,
            }
    
    last_name: MetaOapg.properties.last_name
    first_name: MetaOapg.properties.first_name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["middle_initial"]) -> MetaOapg.properties.middle_initial: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_of_birth"]) -> MetaOapg.properties.date_of_birth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssn"]) -> MetaOapg.properties.ssn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["self_onboarding"]) -> MetaOapg.properties.self_onboarding: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["first_name", "last_name", "middle_initial", "date_of_birth", "email", "ssn", "self_onboarding", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["middle_initial"]) -> typing.Union[MetaOapg.properties.middle_initial, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_of_birth"]) -> typing.Union[MetaOapg.properties.date_of_birth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssn"]) -> typing.Union[MetaOapg.properties.ssn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["self_onboarding"]) -> typing.Union[MetaOapg.properties.self_onboarding, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["first_name", "last_name", "middle_initial", "date_of_birth", "email", "ssn", "self_onboarding", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        last_name: typing.Union[MetaOapg.properties.last_name, str, ],
        first_name: typing.Union[MetaOapg.properties.first_name, str, ],
        middle_initial: typing.Union[MetaOapg.properties.middle_initial, str, schemas.Unset] = schemas.unset,
        date_of_birth: typing.Union[MetaOapg.properties.date_of_birth, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        ssn: typing.Union[MetaOapg.properties.ssn, str, schemas.Unset] = schemas.unset,
        self_onboarding: typing.Union[MetaOapg.properties.self_onboarding, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeesCreateEmployeeRequest':
        return super().__new__(
            cls,
            *args,
            last_name=last_name,
            first_name=first_name,
            middle_initial=middle_initial,
            date_of_birth=date_of_birth,
            email=email,
            ssn=ssn,
            self_onboarding=self_onboarding,
            _configuration=_configuration,
            **kwargs,
        )
