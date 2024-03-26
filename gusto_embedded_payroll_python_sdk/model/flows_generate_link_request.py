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


class FlowsGenerateLinkRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "flow_type",
        }
        
        class properties:
            flow_type = schemas.StrSchema
            entity_uuid = schemas.StrSchema
            
            
            class entity_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Company": "COMPANY",
                        "Employee": "EMPLOYEE",
                    }
                
                @schemas.classproperty
                def COMPANY(cls):
                    return cls("Company")
                
                @schemas.classproperty
                def EMPLOYEE(cls):
                    return cls("Employee")
            __annotations__ = {
                "flow_type": flow_type,
                "entity_uuid": entity_uuid,
                "entity_type": entity_type,
            }
    
    flow_type: MetaOapg.properties.flow_type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flow_type"]) -> MetaOapg.properties.flow_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entity_uuid"]) -> MetaOapg.properties.entity_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entity_type"]) -> MetaOapg.properties.entity_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["flow_type", "entity_uuid", "entity_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flow_type"]) -> MetaOapg.properties.flow_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entity_uuid"]) -> typing.Union[MetaOapg.properties.entity_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entity_type"]) -> typing.Union[MetaOapg.properties.entity_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["flow_type", "entity_uuid", "entity_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        flow_type: typing.Union[MetaOapg.properties.flow_type, str, ],
        entity_uuid: typing.Union[MetaOapg.properties.entity_uuid, str, schemas.Unset] = schemas.unset,
        entity_type: typing.Union[MetaOapg.properties.entity_type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FlowsGenerateLinkRequest':
        return super().__new__(
            cls,
            *args,
            flow_type=flow_type,
            entity_uuid=entity_uuid,
            entity_type=entity_type,
            _configuration=_configuration,
            **kwargs,
        )
