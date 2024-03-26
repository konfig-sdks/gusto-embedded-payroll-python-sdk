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


class Notification(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Representation of a notification
    """


    class MetaOapg:
        
        class properties:
            title = schemas.StrSchema
            uuid = schemas.StrSchema
            company_uuid = schemas.StrSchema
            message = schemas.StrSchema
            category = schemas.StrSchema
            actionable = schemas.BoolSchema
            published_at = schemas.StrSchema
            due_at = schemas.StrSchema
        
            @staticmethod
            def resources() -> typing.Type['NotificationResources']:
                return NotificationResources
            __annotations__ = {
                "title": title,
                "uuid": uuid,
                "company_uuid": company_uuid,
                "message": message,
                "category": category,
                "actionable": actionable,
                "published_at": published_at,
                "due_at": due_at,
                "resources": resources,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_uuid"]) -> MetaOapg.properties.company_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actionable"]) -> MetaOapg.properties.actionable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["published_at"]) -> MetaOapg.properties.published_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["due_at"]) -> MetaOapg.properties.due_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resources"]) -> 'NotificationResources': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "uuid", "company_uuid", "message", "category", "actionable", "published_at", "due_at", "resources", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_uuid"]) -> typing.Union[MetaOapg.properties.company_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actionable"]) -> typing.Union[MetaOapg.properties.actionable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["published_at"]) -> typing.Union[MetaOapg.properties.published_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["due_at"]) -> typing.Union[MetaOapg.properties.due_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resources"]) -> typing.Union['NotificationResources', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "uuid", "company_uuid", "message", "category", "actionable", "published_at", "due_at", "resources", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        title: typing.Union[MetaOapg.properties.title, str, schemas.Unset] = schemas.unset,
        uuid: typing.Union[MetaOapg.properties.uuid, str, schemas.Unset] = schemas.unset,
        company_uuid: typing.Union[MetaOapg.properties.company_uuid, str, schemas.Unset] = schemas.unset,
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        category: typing.Union[MetaOapg.properties.category, str, schemas.Unset] = schemas.unset,
        actionable: typing.Union[MetaOapg.properties.actionable, bool, schemas.Unset] = schemas.unset,
        published_at: typing.Union[MetaOapg.properties.published_at, str, schemas.Unset] = schemas.unset,
        due_at: typing.Union[MetaOapg.properties.due_at, str, schemas.Unset] = schemas.unset,
        resources: typing.Union['NotificationResources', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Notification':
        return super().__new__(
            cls,
            *args,
            title=title,
            uuid=uuid,
            company_uuid=company_uuid,
            message=message,
            category=category,
            actionable=actionable,
            published_at=published_at,
            due_at=due_at,
            resources=resources,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.notification_resources import NotificationResources
