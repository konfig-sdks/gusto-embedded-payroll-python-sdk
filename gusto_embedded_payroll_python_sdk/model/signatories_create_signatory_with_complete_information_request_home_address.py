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


class SignatoriesCreateSignatoryWithCompleteInformationRequestHomeAddress(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The signatory's home address
    """


    class MetaOapg:
        required = {
            "zip",
            "street_1",
            "city",
            "state",
        }
        
        class properties:
            street_1 = schemas.StrSchema
            city = schemas.StrSchema
            state = schemas.StrSchema
            zip = schemas.StrSchema
            street_2 = schemas.StrSchema
            __annotations__ = {
                "street_1": street_1,
                "city": city,
                "state": state,
                "zip": zip,
                "street_2": street_2,
            }
    
    zip: MetaOapg.properties.zip
    street_1: MetaOapg.properties.street_1
    city: MetaOapg.properties.city
    state: MetaOapg.properties.state
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["street_1"]) -> MetaOapg.properties.street_1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zip"]) -> MetaOapg.properties.zip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["street_2"]) -> MetaOapg.properties.street_2: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["street_1", "city", "state", "zip", "street_2", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["street_1"]) -> MetaOapg.properties.street_1: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zip"]) -> MetaOapg.properties.zip: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["street_2"]) -> typing.Union[MetaOapg.properties.street_2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["street_1", "city", "state", "zip", "street_2", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        zip: typing.Union[MetaOapg.properties.zip, str, ],
        street_1: typing.Union[MetaOapg.properties.street_1, str, ],
        city: typing.Union[MetaOapg.properties.city, str, ],
        state: typing.Union[MetaOapg.properties.state, str, ],
        street_2: typing.Union[MetaOapg.properties.street_2, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SignatoriesCreateSignatoryWithCompleteInformationRequestHomeAddress':
        return super().__new__(
            cls,
            *args,
            zip=zip,
            street_1=street_1,
            city=city,
            state=state,
            street_2=street_2,
            _configuration=_configuration,
            **kwargs,
        )
