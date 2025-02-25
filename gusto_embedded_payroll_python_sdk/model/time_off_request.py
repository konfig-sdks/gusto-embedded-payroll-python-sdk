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


class TimeOffRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The representation of a time off request. 
    """


    class MetaOapg:
        
        class properties:
            id = schemas.IntSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "pending": "PENDING",
                        "approved": "APPROVED",
                        "denied": "DENIED",
                    }
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("pending")
                
                @schemas.classproperty
                def APPROVED(cls):
                    return cls("approved")
                
                @schemas.classproperty
                def DENIED(cls):
                    return cls("denied")
            employee_note = schemas.StrSchema
            employer_note = schemas.StrSchema
            
            
            class request_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "vacation": "VACATION",
                        "sick": "SICK",
                    }
                
                @schemas.classproperty
                def VACATION(cls):
                    return cls("vacation")
                
                @schemas.classproperty
                def SICK(cls):
                    return cls("sick")
            days = schemas.DictSchema
        
            @staticmethod
            def employee() -> typing.Type['TimeOffRequestEmployee']:
                return TimeOffRequestEmployee
        
            @staticmethod
            def initiator() -> typing.Type['TimeOffRequestInitiator']:
                return TimeOffRequestInitiator
        
            @staticmethod
            def approver() -> typing.Type['TimeOffRequestApprover']:
                return TimeOffRequestApprover
            __annotations__ = {
                "id": id,
                "status": status,
                "employee_note": employee_note,
                "employer_note": employer_note,
                "request_type": request_type,
                "days": days,
                "employee": employee,
                "initiator": initiator,
                "approver": approver,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_note"]) -> MetaOapg.properties.employee_note: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employer_note"]) -> MetaOapg.properties.employer_note: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["request_type"]) -> MetaOapg.properties.request_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["days"]) -> MetaOapg.properties.days: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee"]) -> 'TimeOffRequestEmployee': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["initiator"]) -> 'TimeOffRequestInitiator': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approver"]) -> 'TimeOffRequestApprover': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "status", "employee_note", "employer_note", "request_type", "days", "employee", "initiator", "approver", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_note"]) -> typing.Union[MetaOapg.properties.employee_note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employer_note"]) -> typing.Union[MetaOapg.properties.employer_note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["request_type"]) -> typing.Union[MetaOapg.properties.request_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["days"]) -> typing.Union[MetaOapg.properties.days, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee"]) -> typing.Union['TimeOffRequestEmployee', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["initiator"]) -> typing.Union['TimeOffRequestInitiator', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approver"]) -> typing.Union['TimeOffRequestApprover', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "status", "employee_note", "employer_note", "request_type", "days", "employee", "initiator", "approver", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        employee_note: typing.Union[MetaOapg.properties.employee_note, str, schemas.Unset] = schemas.unset,
        employer_note: typing.Union[MetaOapg.properties.employer_note, str, schemas.Unset] = schemas.unset,
        request_type: typing.Union[MetaOapg.properties.request_type, str, schemas.Unset] = schemas.unset,
        days: typing.Union[MetaOapg.properties.days, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        employee: typing.Union['TimeOffRequestEmployee', schemas.Unset] = schemas.unset,
        initiator: typing.Union['TimeOffRequestInitiator', schemas.Unset] = schemas.unset,
        approver: typing.Union['TimeOffRequestApprover', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TimeOffRequest':
        return super().__new__(
            cls,
            *args,
            id=id,
            status=status,
            employee_note=employee_note,
            employer_note=employer_note,
            request_type=request_type,
            days=days,
            employee=employee,
            initiator=initiator,
            approver=approver,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.time_off_request_approver import TimeOffRequestApprover
from gusto_embedded_payroll_python_sdk.model.time_off_request_employee import TimeOffRequestEmployee
from gusto_embedded_payroll_python_sdk.model.time_off_request_initiator import TimeOffRequestInitiator
