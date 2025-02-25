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


class EmployeeWorkAddress(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            version = schemas.StrSchema
            uuid = schemas.StrSchema
            effective_date = schemas.StrSchema
            active = schemas.BoolSchema
            location_uuid = schemas.StrSchema
            employee_uuid = schemas.StrSchema
            street_1 = schemas.StrSchema
            
            
            class street_2(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'street_2':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            city = schemas.StrSchema
            state = schemas.StrSchema
            zip = schemas.StrSchema
            country = schemas.StrSchema
            __annotations__ = {
                "version": version,
                "uuid": uuid,
                "effective_date": effective_date,
                "active": active,
                "location_uuid": location_uuid,
                "employee_uuid": employee_uuid,
                "street_1": street_1,
                "street_2": street_2,
                "city": city,
                "state": state,
                "zip": zip,
                "country": country,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effective_date"]) -> MetaOapg.properties.effective_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["location_uuid"]) -> MetaOapg.properties.location_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_uuid"]) -> MetaOapg.properties.employee_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["street_1"]) -> MetaOapg.properties.street_1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["street_2"]) -> MetaOapg.properties.street_2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zip"]) -> MetaOapg.properties.zip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "uuid", "effective_date", "active", "location_uuid", "employee_uuid", "street_1", "street_2", "city", "state", "zip", "country", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effective_date"]) -> typing.Union[MetaOapg.properties.effective_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["location_uuid"]) -> typing.Union[MetaOapg.properties.location_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_uuid"]) -> typing.Union[MetaOapg.properties.employee_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["street_1"]) -> typing.Union[MetaOapg.properties.street_1, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["street_2"]) -> typing.Union[MetaOapg.properties.street_2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zip"]) -> typing.Union[MetaOapg.properties.zip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "uuid", "effective_date", "active", "location_uuid", "employee_uuid", "street_1", "street_2", "city", "state", "zip", "country", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        version: typing.Union[MetaOapg.properties.version, str, schemas.Unset] = schemas.unset,
        uuid: typing.Union[MetaOapg.properties.uuid, str, schemas.Unset] = schemas.unset,
        effective_date: typing.Union[MetaOapg.properties.effective_date, str, schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        location_uuid: typing.Union[MetaOapg.properties.location_uuid, str, schemas.Unset] = schemas.unset,
        employee_uuid: typing.Union[MetaOapg.properties.employee_uuid, str, schemas.Unset] = schemas.unset,
        street_1: typing.Union[MetaOapg.properties.street_1, str, schemas.Unset] = schemas.unset,
        street_2: typing.Union[MetaOapg.properties.street_2, None, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        zip: typing.Union[MetaOapg.properties.zip, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeWorkAddress':
        return super().__new__(
            cls,
            *args,
            version=version,
            uuid=uuid,
            effective_date=effective_date,
            active=active,
            location_uuid=location_uuid,
            employee_uuid=employee_uuid,
            street_1=street_1,
            street_2=street_2,
            city=city,
            state=state,
            zip=zip,
            country=country,
            _configuration=_configuration,
            **kwargs,
        )
