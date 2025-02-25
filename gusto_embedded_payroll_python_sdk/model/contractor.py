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


class Contractor(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The representation of a contractor (individual or business) in Gusto.
    """


    class MetaOapg:
        
        class properties:
            version = schemas.StrSchema
            uuid = schemas.StrSchema
            company_uuid = schemas.StrSchema
            
            
            class wage_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Fixed": "FIXED",
                        "Hourly": "HOURLY",
                    }
                
                @schemas.classproperty
                def FIXED(cls):
                    return cls("Fixed")
                
                @schemas.classproperty
                def HOURLY(cls):
                    return cls("Hourly")
            is_active = schemas.BoolSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Individual": "INDIVIDUAL",
                        "Business": "BUSINESS",
                    }
                
                @schemas.classproperty
                def INDIVIDUAL(cls):
                    return cls("Individual")
                
                @schemas.classproperty
                def BUSINESS(cls):
                    return cls("Business")
            
            
            class first_name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'first_name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class last_name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'last_name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class middle_initial(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'middle_initial':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class business_name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'business_name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class ein(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ein':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class has_ein(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'has_ein':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class email(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'email':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            start_date = schemas.StrSchema
        
            @staticmethod
            def address() -> typing.Type['ContractorAddress']:
                return ContractorAddress
            hourly_rate = schemas.StrSchema
            file_new_hire_report = schemas.BoolSchema
            
            
            class work_state(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'work_state':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            onboarded = schemas.BoolSchema
            
            
            class onboarding_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "onboarding_completed": "ONBOARDING_COMPLETED",
                        "admin_onboarding_review": "ADMIN_ONBOARDING_REVIEW",
                        "admin_onboarding_incomplete": "ADMIN_ONBOARDING_INCOMPLETE",
                    }
                
                @schemas.classproperty
                def ONBOARDING_COMPLETED(cls):
                    return cls("onboarding_completed")
                
                @schemas.classproperty
                def ADMIN_ONBOARDING_REVIEW(cls):
                    return cls("admin_onboarding_review")
                
                @schemas.classproperty
                def ADMIN_ONBOARDING_INCOMPLETE(cls):
                    return cls("admin_onboarding_incomplete")
            __annotations__ = {
                "version": version,
                "uuid": uuid,
                "company_uuid": company_uuid,
                "wage_type": wage_type,
                "is_active": is_active,
                "type": type,
                "first_name": first_name,
                "last_name": last_name,
                "middle_initial": middle_initial,
                "business_name": business_name,
                "ein": ein,
                "has_ein": has_ein,
                "email": email,
                "start_date": start_date,
                "address": address,
                "hourly_rate": hourly_rate,
                "file_new_hire_report": file_new_hire_report,
                "work_state": work_state,
                "onboarded": onboarded,
                "onboarding_status": onboarding_status,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_uuid"]) -> MetaOapg.properties.company_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wage_type"]) -> MetaOapg.properties.wage_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["middle_initial"]) -> MetaOapg.properties.middle_initial: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["business_name"]) -> MetaOapg.properties.business_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ein"]) -> MetaOapg.properties.ein: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_ein"]) -> MetaOapg.properties.has_ein: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'ContractorAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hourly_rate"]) -> MetaOapg.properties.hourly_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file_new_hire_report"]) -> MetaOapg.properties.file_new_hire_report: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["work_state"]) -> MetaOapg.properties.work_state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["onboarded"]) -> MetaOapg.properties.onboarded: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["onboarding_status"]) -> MetaOapg.properties.onboarding_status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "uuid", "company_uuid", "wage_type", "is_active", "type", "first_name", "last_name", "middle_initial", "business_name", "ein", "has_ein", "email", "start_date", "address", "hourly_rate", "file_new_hire_report", "work_state", "onboarded", "onboarding_status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_uuid"]) -> typing.Union[MetaOapg.properties.company_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wage_type"]) -> typing.Union[MetaOapg.properties.wage_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_active"]) -> typing.Union[MetaOapg.properties.is_active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> typing.Union[MetaOapg.properties.first_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> typing.Union[MetaOapg.properties.last_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["middle_initial"]) -> typing.Union[MetaOapg.properties.middle_initial, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["business_name"]) -> typing.Union[MetaOapg.properties.business_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ein"]) -> typing.Union[MetaOapg.properties.ein, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_ein"]) -> typing.Union[MetaOapg.properties.has_ein, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union['ContractorAddress', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hourly_rate"]) -> typing.Union[MetaOapg.properties.hourly_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file_new_hire_report"]) -> typing.Union[MetaOapg.properties.file_new_hire_report, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["work_state"]) -> typing.Union[MetaOapg.properties.work_state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["onboarded"]) -> typing.Union[MetaOapg.properties.onboarded, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["onboarding_status"]) -> typing.Union[MetaOapg.properties.onboarding_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "uuid", "company_uuid", "wage_type", "is_active", "type", "first_name", "last_name", "middle_initial", "business_name", "ein", "has_ein", "email", "start_date", "address", "hourly_rate", "file_new_hire_report", "work_state", "onboarded", "onboarding_status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        version: typing.Union[MetaOapg.properties.version, str, schemas.Unset] = schemas.unset,
        uuid: typing.Union[MetaOapg.properties.uuid, str, schemas.Unset] = schemas.unset,
        company_uuid: typing.Union[MetaOapg.properties.company_uuid, str, schemas.Unset] = schemas.unset,
        wage_type: typing.Union[MetaOapg.properties.wage_type, str, schemas.Unset] = schemas.unset,
        is_active: typing.Union[MetaOapg.properties.is_active, bool, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        first_name: typing.Union[MetaOapg.properties.first_name, None, str, schemas.Unset] = schemas.unset,
        last_name: typing.Union[MetaOapg.properties.last_name, None, str, schemas.Unset] = schemas.unset,
        middle_initial: typing.Union[MetaOapg.properties.middle_initial, None, str, schemas.Unset] = schemas.unset,
        business_name: typing.Union[MetaOapg.properties.business_name, None, str, schemas.Unset] = schemas.unset,
        ein: typing.Union[MetaOapg.properties.ein, None, str, schemas.Unset] = schemas.unset,
        has_ein: typing.Union[MetaOapg.properties.has_ein, None, bool, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, None, str, schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, str, schemas.Unset] = schemas.unset,
        address: typing.Union['ContractorAddress', schemas.Unset] = schemas.unset,
        hourly_rate: typing.Union[MetaOapg.properties.hourly_rate, str, schemas.Unset] = schemas.unset,
        file_new_hire_report: typing.Union[MetaOapg.properties.file_new_hire_report, bool, schemas.Unset] = schemas.unset,
        work_state: typing.Union[MetaOapg.properties.work_state, None, str, schemas.Unset] = schemas.unset,
        onboarded: typing.Union[MetaOapg.properties.onboarded, bool, schemas.Unset] = schemas.unset,
        onboarding_status: typing.Union[MetaOapg.properties.onboarding_status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Contractor':
        return super().__new__(
            cls,
            *args,
            version=version,
            uuid=uuid,
            company_uuid=company_uuid,
            wage_type=wage_type,
            is_active=is_active,
            type=type,
            first_name=first_name,
            last_name=last_name,
            middle_initial=middle_initial,
            business_name=business_name,
            ein=ein,
            has_ein=has_ein,
            email=email,
            start_date=start_date,
            address=address,
            hourly_rate=hourly_rate,
            file_new_hire_report=file_new_hire_report,
            work_state=work_state,
            onboarded=onboarded,
            onboarding_status=onboarding_status,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.contractor_address import ContractorAddress
