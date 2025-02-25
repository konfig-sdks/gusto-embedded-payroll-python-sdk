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


class TaxRequirementMetadataValidation(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    [for `tax_rate`] Describes the validation required for the tax rate
    """


    class MetaOapg:
        required = {
            "type",
        }
        
        class properties:
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ONE_OF(cls):
                    return cls("one_of")
                
                @schemas.classproperty
                def MIN_MAX(cls):
                    return cls("min_max")
            min = schemas.StrSchema
            max = schemas.StrSchema
        
            @staticmethod
            def rates() -> typing.Type['TaxRequirementMetadataValidationRates']:
                return TaxRequirementMetadataValidationRates
            __annotations__ = {
                "type": type,
                "min": min,
                "max": max,
                "rates": rates,
            }
    
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["min"]) -> MetaOapg.properties.min: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["max"]) -> MetaOapg.properties.max: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rates"]) -> 'TaxRequirementMetadataValidationRates': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "min", "max", "rates", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["min"]) -> typing.Union[MetaOapg.properties.min, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["max"]) -> typing.Union[MetaOapg.properties.max, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rates"]) -> typing.Union['TaxRequirementMetadataValidationRates', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "min", "max", "rates", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        min: typing.Union[MetaOapg.properties.min, str, schemas.Unset] = schemas.unset,
        max: typing.Union[MetaOapg.properties.max, str, schemas.Unset] = schemas.unset,
        rates: typing.Union['TaxRequirementMetadataValidationRates', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TaxRequirementMetadataValidation':
        return super().__new__(
            cls,
            *args,
            type=type,
            min=min,
            max=max,
            rates=rates,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.tax_requirement_metadata_validation_rates import TaxRequirementMetadataValidationRates
