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


class CompaniesGetTermsOfServiceStatusResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "ip_address",
            "email",
            "external_user_id",
        }
        
        class properties:
            latest_terms_accepted = schemas.BoolSchema
            __annotations__ = {
                "latest_terms_accepted": latest_terms_accepted,
            }
    
    ip_address: schemas.AnyTypeSchema
    email: schemas.AnyTypeSchema
    external_user_id: schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latest_terms_accepted"]) -> MetaOapg.properties.latest_terms_accepted: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["latest_terms_accepted", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latest_terms_accepted"]) -> typing.Union[MetaOapg.properties.latest_terms_accepted, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["latest_terms_accepted", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        latest_terms_accepted: typing.Union[MetaOapg.properties.latest_terms_accepted, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompaniesGetTermsOfServiceStatusResponse':
        return super().__new__(
            cls,
            *args,
            latest_terms_accepted=latest_terms_accepted,
            _configuration=_configuration,
            **kwargs,
        )
