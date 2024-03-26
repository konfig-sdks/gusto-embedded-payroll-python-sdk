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


class PayScheduleAssignmentEmployeeChange(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            employee_uuid = schemas.StrSchema
            first_name = schemas.StrSchema
            last_name = schemas.StrSchema
            pay_frequency = schemas.StrSchema
        
            @staticmethod
            def first_pay_period() -> typing.Type['PayScheduleAssignmentPayPeriod']:
                return PayScheduleAssignmentPayPeriod
        
            @staticmethod
            def transition_pay_period() -> typing.Type['PayScheduleAssignmentTransitionPayPeriod']:
                return PayScheduleAssignmentTransitionPayPeriod
            __annotations__ = {
                "employee_uuid": employee_uuid,
                "first_name": first_name,
                "last_name": last_name,
                "pay_frequency": pay_frequency,
                "first_pay_period": first_pay_period,
                "transition_pay_period": transition_pay_period,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_uuid"]) -> MetaOapg.properties.employee_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pay_frequency"]) -> MetaOapg.properties.pay_frequency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_pay_period"]) -> 'PayScheduleAssignmentPayPeriod': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transition_pay_period"]) -> 'PayScheduleAssignmentTransitionPayPeriod': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["employee_uuid", "first_name", "last_name", "pay_frequency", "first_pay_period", "transition_pay_period", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_uuid"]) -> typing.Union[MetaOapg.properties.employee_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> typing.Union[MetaOapg.properties.first_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> typing.Union[MetaOapg.properties.last_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pay_frequency"]) -> typing.Union[MetaOapg.properties.pay_frequency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_pay_period"]) -> typing.Union['PayScheduleAssignmentPayPeriod', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transition_pay_period"]) -> typing.Union['PayScheduleAssignmentTransitionPayPeriod', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["employee_uuid", "first_name", "last_name", "pay_frequency", "first_pay_period", "transition_pay_period", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        employee_uuid: typing.Union[MetaOapg.properties.employee_uuid, str, schemas.Unset] = schemas.unset,
        first_name: typing.Union[MetaOapg.properties.first_name, str, schemas.Unset] = schemas.unset,
        last_name: typing.Union[MetaOapg.properties.last_name, str, schemas.Unset] = schemas.unset,
        pay_frequency: typing.Union[MetaOapg.properties.pay_frequency, str, schemas.Unset] = schemas.unset,
        first_pay_period: typing.Union['PayScheduleAssignmentPayPeriod', schemas.Unset] = schemas.unset,
        transition_pay_period: typing.Union['PayScheduleAssignmentTransitionPayPeriod', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayScheduleAssignmentEmployeeChange':
        return super().__new__(
            cls,
            *args,
            employee_uuid=employee_uuid,
            first_name=first_name,
            last_name=last_name,
            pay_frequency=pay_frequency,
            first_pay_period=first_pay_period,
            transition_pay_period=transition_pay_period,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.pay_schedule_assignment_pay_period import PayScheduleAssignmentPayPeriod
from gusto_embedded_payroll_python_sdk.model.pay_schedule_assignment_transition_pay_period import PayScheduleAssignmentTransitionPayPeriod
