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


class EmployeeOnboardingStatusOnboardingStepsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            id = schemas.StrSchema
            required = schemas.BoolSchema
            completed = schemas.BoolSchema
        
            @staticmethod
            def requirements() -> typing.Type['EmployeeOnboardingStatusOnboardingStepsItemRequirements']:
                return EmployeeOnboardingStatusOnboardingStepsItemRequirements
            __annotations__ = {
                "title": title,
                "id": id,
                "required": required,
                "completed": completed,
                "requirements": requirements,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["completed"]) -> MetaOapg.properties.completed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requirements"]) -> 'EmployeeOnboardingStatusOnboardingStepsItemRequirements': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "id", "required", "completed", "requirements", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> typing.Union[MetaOapg.properties.required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["completed"]) -> typing.Union[MetaOapg.properties.completed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requirements"]) -> typing.Union['EmployeeOnboardingStatusOnboardingStepsItemRequirements', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "id", "required", "completed", "requirements", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        required: typing.Union[MetaOapg.properties.required, bool, schemas.Unset] = schemas.unset,
        completed: typing.Union[MetaOapg.properties.completed, bool, schemas.Unset] = schemas.unset,
        requirements: typing.Union['EmployeeOnboardingStatusOnboardingStepsItemRequirements', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeOnboardingStatusOnboardingStepsItem':
        return super().__new__(
            cls,
            *args,
            title=title,
            id=id,
            required=required,
            completed=completed,
            requirements=requirements,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.employee_onboarding_status_onboarding_steps_item_requirements import EmployeeOnboardingStatusOnboardingStepsItemRequirements
