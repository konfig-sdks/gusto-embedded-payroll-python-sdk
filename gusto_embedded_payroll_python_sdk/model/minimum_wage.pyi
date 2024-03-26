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


class MinimumWage(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Representation of a Minimum Wage
    """


    class MetaOapg:
        required = {
            "authority",
            "effective_date",
            "uuid",
            "wage",
            "wage_type",
        }
        
        class properties:
            uuid = schemas.StrSchema
            wage = schemas.StrSchema
            wage_type = schemas.StrSchema
            effective_date = schemas.DateSchema
            authority = schemas.StrSchema
            notes = schemas.StrSchema
            __annotations__ = {
                "uuid": uuid,
                "wage": wage,
                "wage_type": wage_type,
                "effective_date": effective_date,
                "authority": authority,
                "notes": notes,
            }
    
    authority: MetaOapg.properties.authority
    effective_date: MetaOapg.properties.effective_date
    uuid: MetaOapg.properties.uuid
    wage: MetaOapg.properties.wage
    wage_type: MetaOapg.properties.wage_type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wage"]) -> MetaOapg.properties.wage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["wage_type"]) -> MetaOapg.properties.wage_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["effective_date"]) -> MetaOapg.properties.effective_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authority"]) -> MetaOapg.properties.authority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notes"]) -> MetaOapg.properties.notes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["uuid", "wage", "wage_type", "effective_date", "authority", "notes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wage"]) -> MetaOapg.properties.wage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["wage_type"]) -> MetaOapg.properties.wage_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["effective_date"]) -> MetaOapg.properties.effective_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authority"]) -> MetaOapg.properties.authority: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notes"]) -> typing.Union[MetaOapg.properties.notes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uuid", "wage", "wage_type", "effective_date", "authority", "notes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        authority: typing.Union[MetaOapg.properties.authority, str, ],
        effective_date: typing.Union[MetaOapg.properties.effective_date, str, date, ],
        uuid: typing.Union[MetaOapg.properties.uuid, str, ],
        wage: typing.Union[MetaOapg.properties.wage, str, ],
        wage_type: typing.Union[MetaOapg.properties.wage_type, str, ],
        notes: typing.Union[MetaOapg.properties.notes, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MinimumWage':
        return super().__new__(
            cls,
            *args,
            authority=authority,
            effective_date=effective_date,
            uuid=uuid,
            wage=wage,
            wage_type=wage_type,
            notes=notes,
            _configuration=_configuration,
            **kwargs,
        )
