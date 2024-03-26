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


class Rehire(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            version = schemas.StrSchema
            effective_date = schemas.StrSchema
            file_new_hire_report = schemas.BoolSchema
            work_location_uuid = schemas.StrSchema
            
            
            class employment_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PART_TIME(cls):
                    return cls("part_time")
                
                @schemas.classproperty
                def FULL_TIME(cls):
                    return cls("full_time")
                
                @schemas.classproperty
                def PART_TIME_ELIGIBLE(cls):
                    return cls("part_time_eligible")
                
                @schemas.classproperty
                def VARIABLE(cls):
                    return cls("variable")
                
                @schemas.classproperty
                def SEASONAL(cls):
                    return cls("seasonal")
                
                @schemas.classproperty
                def NOT_SET(cls):
                    return cls("not_set")
            two_percent_shareholder = schemas.BoolSchema
            employee_uuid = schemas.StrSchema
            active = schemas.BoolSchema
            __annotations__ = {
                "version": version,
                "effective_date": effective_date,
                "file_new_hire_report": file_new_hire_report,
                "work_location_uuid": work_location_uuid,
                "employment_status": employment_status,
                "two_percent_shareholder": two_percent_shareholder,
                "employee_uuid": employee_uuid,
                "active": active,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effective_date"]) -> MetaOapg.properties.effective_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_new_hire_report"]) -> MetaOapg.properties.file_new_hire_report: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["work_location_uuid"]) -> MetaOapg.properties.work_location_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employment_status"]) -> MetaOapg.properties.employment_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["two_percent_shareholder"]) -> MetaOapg.properties.two_percent_shareholder: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_uuid"]) -> MetaOapg.properties.employee_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "effective_date", "file_new_hire_report", "work_location_uuid", "employment_status", "two_percent_shareholder", "employee_uuid", "active", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effective_date"]) -> typing.Union[MetaOapg.properties.effective_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_new_hire_report"]) -> typing.Union[MetaOapg.properties.file_new_hire_report, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["work_location_uuid"]) -> typing.Union[MetaOapg.properties.work_location_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employment_status"]) -> typing.Union[MetaOapg.properties.employment_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["two_percent_shareholder"]) -> typing.Union[MetaOapg.properties.two_percent_shareholder, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_uuid"]) -> typing.Union[MetaOapg.properties.employee_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "effective_date", "file_new_hire_report", "work_location_uuid", "employment_status", "two_percent_shareholder", "employee_uuid", "active", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        version: typing.Union[MetaOapg.properties.version, str, schemas.Unset] = schemas.unset,
        effective_date: typing.Union[MetaOapg.properties.effective_date, str, schemas.Unset] = schemas.unset,
        file_new_hire_report: typing.Union[MetaOapg.properties.file_new_hire_report, bool, schemas.Unset] = schemas.unset,
        work_location_uuid: typing.Union[MetaOapg.properties.work_location_uuid, str, schemas.Unset] = schemas.unset,
        employment_status: typing.Union[MetaOapg.properties.employment_status, str, schemas.Unset] = schemas.unset,
        two_percent_shareholder: typing.Union[MetaOapg.properties.two_percent_shareholder, bool, schemas.Unset] = schemas.unset,
        employee_uuid: typing.Union[MetaOapg.properties.employee_uuid, str, schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Rehire':
        return super().__new__(
            cls,
            *args,
            version=version,
            effective_date=effective_date,
            file_new_hire_report=file_new_hire_report,
            work_location_uuid=work_location_uuid,
            employment_status=employment_status,
            two_percent_shareholder=two_percent_shareholder,
            employee_uuid=employee_uuid,
            active=active,
            _configuration=_configuration,
            **kwargs,
        )
