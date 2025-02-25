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


class PayrollsSkipPayrollRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "payroll_type",
        }
        
        class properties:
            
            
            class payroll_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Regular": "REGULAR",
                        "Hired employee": "HIRED_EMPLOYEE",
                        "Dismissed employee": "DISMISSED_EMPLOYEE",
                        "Transition from old pay schedule": "TRANSITION_FROM_OLD_PAY_SCHEDULE",
                    }
                
                @schemas.classproperty
                def REGULAR(cls):
                    return cls("Regular")
                
                @schemas.classproperty
                def HIRED_EMPLOYEE(cls):
                    return cls("Hired employee")
                
                @schemas.classproperty
                def DISMISSED_EMPLOYEE(cls):
                    return cls("Dismissed employee")
                
                @schemas.classproperty
                def TRANSITION_FROM_OLD_PAY_SCHEDULE(cls):
                    return cls("Transition from old pay schedule")
            start_date = schemas.StrSchema
            end_date = schemas.StrSchema
            pay_schedule_uuid = schemas.StrSchema
        
            @staticmethod
            def employee_uuids() -> typing.Type['PayrollsSkipPayrollRequestEmployeeUuids']:
                return PayrollsSkipPayrollRequestEmployeeUuids
            __annotations__ = {
                "payroll_type": payroll_type,
                "start_date": start_date,
                "end_date": end_date,
                "pay_schedule_uuid": pay_schedule_uuid,
                "employee_uuids": employee_uuids,
            }
    
    payroll_type: MetaOapg.properties.payroll_type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payroll_type"]) -> MetaOapg.properties.payroll_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pay_schedule_uuid"]) -> MetaOapg.properties.pay_schedule_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_uuids"]) -> 'PayrollsSkipPayrollRequestEmployeeUuids': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["payroll_type", "start_date", "end_date", "pay_schedule_uuid", "employee_uuids", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payroll_type"]) -> MetaOapg.properties.payroll_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pay_schedule_uuid"]) -> typing.Union[MetaOapg.properties.pay_schedule_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_uuids"]) -> typing.Union['PayrollsSkipPayrollRequestEmployeeUuids', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["payroll_type", "start_date", "end_date", "pay_schedule_uuid", "employee_uuids", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        payroll_type: typing.Union[MetaOapg.properties.payroll_type, str, ],
        start_date: typing.Union[MetaOapg.properties.start_date, str, schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, str, schemas.Unset] = schemas.unset,
        pay_schedule_uuid: typing.Union[MetaOapg.properties.pay_schedule_uuid, str, schemas.Unset] = schemas.unset,
        employee_uuids: typing.Union['PayrollsSkipPayrollRequestEmployeeUuids', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayrollsSkipPayrollRequest':
        return super().__new__(
            cls,
            *args,
            payroll_type=payroll_type,
            start_date=start_date,
            end_date=end_date,
            pay_schedule_uuid=pay_schedule_uuid,
            employee_uuids=employee_uuids,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.payrolls_skip_payroll_request_employee_uuids import PayrollsSkipPayrollRequestEmployeeUuids
