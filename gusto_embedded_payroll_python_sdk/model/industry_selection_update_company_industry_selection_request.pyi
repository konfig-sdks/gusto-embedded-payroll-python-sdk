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


class IndustrySelectionUpdateCompanyIndustrySelectionRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "naics_code",
            "title",
        }
        
        class properties:
            title = schemas.StrSchema
            naics_code = schemas.StrSchema
        
            @staticmethod
            def sic_codes() -> typing.Type['IndustrySelectionUpdateCompanyIndustrySelectionRequestSicCodes']:
                return IndustrySelectionUpdateCompanyIndustrySelectionRequestSicCodes
            __annotations__ = {
                "title": title,
                "naics_code": naics_code,
                "sic_codes": sic_codes,
            }
    
    naics_code: MetaOapg.properties.naics_code
    title: MetaOapg.properties.title
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["naics_code"]) -> MetaOapg.properties.naics_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sic_codes"]) -> 'IndustrySelectionUpdateCompanyIndustrySelectionRequestSicCodes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "naics_code", "sic_codes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["naics_code"]) -> MetaOapg.properties.naics_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sic_codes"]) -> typing.Union['IndustrySelectionUpdateCompanyIndustrySelectionRequestSicCodes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "naics_code", "sic_codes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        naics_code: typing.Union[MetaOapg.properties.naics_code, str, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        sic_codes: typing.Union['IndustrySelectionUpdateCompanyIndustrySelectionRequestSicCodes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IndustrySelectionUpdateCompanyIndustrySelectionRequest':
        return super().__new__(
            cls,
            *args,
            naics_code=naics_code,
            title=title,
            sic_codes=sic_codes,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.industry_selection_update_company_industry_selection_request_sic_codes import IndustrySelectionUpdateCompanyIndustrySelectionRequestSicCodes
