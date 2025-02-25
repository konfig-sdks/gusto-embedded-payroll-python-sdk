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


class LocationsUpdateLocationRequest(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    
                    
                    class phone_number(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            regex=[{
                                'pattern': r'[0-9]{10}',
                            }]
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
                    mailing_address = schemas.BoolSchema
                    filing_address = schemas.BoolSchema
                    __annotations__ = {
                        "phone_number": phone_number,
                        "street_1": street_1,
                        "street_2": street_2,
                        "city": city,
                        "state": state,
                        "zip": zip,
                        "country": country,
                        "mailing_address": mailing_address,
                        "filing_address": filing_address,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
            
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
            def __getitem__(self, name: typing_extensions.Literal["mailing_address"]) -> MetaOapg.properties.mailing_address: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["filing_address"]) -> MetaOapg.properties.filing_address: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["phone_number", "street_1", "street_2", "city", "state", "zip", "country", "mailing_address", "filing_address", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["phone_number"]) -> typing.Union[MetaOapg.properties.phone_number, schemas.Unset]: ...
            
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
            def get_item_oapg(self, name: typing_extensions.Literal["mailing_address"]) -> typing.Union[MetaOapg.properties.mailing_address, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["filing_address"]) -> typing.Union[MetaOapg.properties.filing_address, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["phone_number", "street_1", "street_2", "city", "state", "zip", "country", "mailing_address", "filing_address", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                phone_number: typing.Union[MetaOapg.properties.phone_number, str, schemas.Unset] = schemas.unset,
                street_1: typing.Union[MetaOapg.properties.street_1, str, schemas.Unset] = schemas.unset,
                street_2: typing.Union[MetaOapg.properties.street_2, None, str, schemas.Unset] = schemas.unset,
                city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
                state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
                zip: typing.Union[MetaOapg.properties.zip, str, schemas.Unset] = schemas.unset,
                country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
                mailing_address: typing.Union[MetaOapg.properties.mailing_address, bool, schemas.Unset] = schemas.unset,
                filing_address: typing.Union[MetaOapg.properties.filing_address, bool, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    phone_number=phone_number,
                    street_1=street_1,
                    street_2=street_2,
                    city=city,
                    state=state,
                    zip=zip,
                    country=country,
                    mailing_address=mailing_address,
                    filing_address=filing_address,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                VersionableRequired,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LocationsUpdateLocationRequest':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.versionable_required import VersionableRequired
