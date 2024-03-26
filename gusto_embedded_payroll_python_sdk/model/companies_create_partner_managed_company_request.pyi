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


class CompaniesCreatePartnerManagedCompanyRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "company",
            "user",
        }
        
        class properties:
        
            @staticmethod
            def user() -> typing.Type['CompaniesCreatePartnerManagedCompanyRequestUser']:
                return CompaniesCreatePartnerManagedCompanyRequestUser
        
            @staticmethod
            def company() -> typing.Type['CompaniesCreatePartnerManagedCompanyRequestCompany']:
                return CompaniesCreatePartnerManagedCompanyRequestCompany
            __annotations__ = {
                "user": user,
                "company": company,
            }
    
    company: 'CompaniesCreatePartnerManagedCompanyRequestCompany'
    user: 'CompaniesCreatePartnerManagedCompanyRequestUser'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'CompaniesCreatePartnerManagedCompanyRequestUser': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company"]) -> 'CompaniesCreatePartnerManagedCompanyRequestCompany': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["user", "company", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> 'CompaniesCreatePartnerManagedCompanyRequestUser': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company"]) -> 'CompaniesCreatePartnerManagedCompanyRequestCompany': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["user", "company", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        company: 'CompaniesCreatePartnerManagedCompanyRequestCompany',
        user: 'CompaniesCreatePartnerManagedCompanyRequestUser',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CompaniesCreatePartnerManagedCompanyRequest':
        return super().__new__(
            cls,
            *args,
            company=company,
            user=user,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.companies_create_partner_managed_company_request_company import CompaniesCreatePartnerManagedCompanyRequestCompany
from gusto_embedded_payroll_python_sdk.model.companies_create_partner_managed_company_request_user import CompaniesCreatePartnerManagedCompanyRequestUser
