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


class EmployeeFormsSignFormRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "signed_by_ip_address",
            "signature_text",
            "agree",
        }
        
        class properties:
            signature_text = schemas.StrSchema
            agree = schemas.BoolSchema
            signed_by_ip_address = schemas.StrSchema
            __annotations__ = {
                "signature_text": signature_text,
                "agree": agree,
                "signed_by_ip_address": signed_by_ip_address,
            }
    
    signed_by_ip_address: MetaOapg.properties.signed_by_ip_address
    signature_text: MetaOapg.properties.signature_text
    agree: MetaOapg.properties.agree
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signature_text"]) -> MetaOapg.properties.signature_text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agree"]) -> MetaOapg.properties.agree: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signed_by_ip_address"]) -> MetaOapg.properties.signed_by_ip_address: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["signature_text", "agree", "signed_by_ip_address", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signature_text"]) -> MetaOapg.properties.signature_text: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agree"]) -> MetaOapg.properties.agree: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signed_by_ip_address"]) -> MetaOapg.properties.signed_by_ip_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["signature_text", "agree", "signed_by_ip_address", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        signed_by_ip_address: typing.Union[MetaOapg.properties.signed_by_ip_address, str, ],
        signature_text: typing.Union[MetaOapg.properties.signature_text, str, ],
        agree: typing.Union[MetaOapg.properties.agree, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeFormsSignFormRequest':
        return super().__new__(
            cls,
            *args,
            signed_by_ip_address=signed_by_ip_address,
            signature_text=signature_text,
            agree=agree,
            _configuration=_configuration,
            **kwargs,
        )
