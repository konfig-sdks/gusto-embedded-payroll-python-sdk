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


class CompanyOnboardingStatus(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The representation of a company's onboarding status
    """


    class MetaOapg:
        
        class properties:
            uuid = schemas.StrSchema
            onboarding_completed = schemas.BoolSchema
        
            @staticmethod
            def onboarding_steps() -> typing.Type['CompanyOnboardingStatusOnboardingSteps']:
                return CompanyOnboardingStatusOnboardingSteps
             = schemas.StrSchema
            __annotations__ = {
                "uuid": uuid,
                "onboarding_completed": onboarding_completed,
                "onboarding_steps": onboarding_steps,
                "": ,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["onboarding_completed"]) -> MetaOapg.properties.onboarding_completed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["onboarding_steps"]) -> 'CompanyOnboardingStatusOnboardingSteps': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal[""]) -> MetaOapg.properties.: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["uuid", "onboarding_completed", "onboarding_steps", "", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["onboarding_completed"]) -> typing.Union[MetaOapg.properties.onboarding_completed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["onboarding_steps"]) -> typing.Union['CompanyOnboardingStatusOnboardingSteps', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal[""]) -> typing.Union[MetaOapg.properties., schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uuid", "onboarding_completed", "onboarding_steps", "", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        uuid: typing.Union[MetaOapg.properties.uuid, str, schemas.Unset] = schemas.unset,
        onboarding_completed: typing.Union[MetaOapg.properties.onboarding_completed, bool, schemas.Unset] = schemas.unset,
        onboarding_steps: typing.Union['CompanyOnboardingStatusOnboardingSteps', schemas.Unset] = schemas.unset,
        : typing.Union[MetaOapg.properties., str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompanyOnboardingStatus':
        return super().__new__(
            cls,
            *args,
            uuid=uuid,
            onboarding_completed=onboarding_completed,
            onboarding_steps=onboarding_steps,
            =,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.company_onboarding_status_onboarding_steps import CompanyOnboardingStatusOnboardingSteps
