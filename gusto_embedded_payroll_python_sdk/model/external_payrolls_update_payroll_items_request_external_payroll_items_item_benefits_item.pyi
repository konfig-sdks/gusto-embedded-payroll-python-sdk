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


class ExternalPayrollsUpdatePayrollItemsRequestExternalPayrollItemsItemBenefitsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    An array of benefits for the employee. Depends on your company selections, benefits include 401k, health insurance and more.
    """


    class MetaOapg:
        
        class properties:
            company_contribution_amount = schemas.StrSchema
            employee_deduction_amount = schemas.StrSchema
            benefit_id = schemas.IntSchema
            __annotations__ = {
                "company_contribution_amount": company_contribution_amount,
                "employee_deduction_amount": employee_deduction_amount,
                "benefit_id": benefit_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_contribution_amount"]) -> MetaOapg.properties.company_contribution_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employee_deduction_amount"]) -> MetaOapg.properties.employee_deduction_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["benefit_id"]) -> MetaOapg.properties.benefit_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["company_contribution_amount", "employee_deduction_amount", "benefit_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_contribution_amount"]) -> typing.Union[MetaOapg.properties.company_contribution_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employee_deduction_amount"]) -> typing.Union[MetaOapg.properties.employee_deduction_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["benefit_id"]) -> typing.Union[MetaOapg.properties.benefit_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["company_contribution_amount", "employee_deduction_amount", "benefit_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        company_contribution_amount: typing.Union[MetaOapg.properties.company_contribution_amount, str, schemas.Unset] = schemas.unset,
        employee_deduction_amount: typing.Union[MetaOapg.properties.employee_deduction_amount, str, schemas.Unset] = schemas.unset,
        benefit_id: typing.Union[MetaOapg.properties.benefit_id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExternalPayrollsUpdatePayrollItemsRequestExternalPayrollItemsItemBenefitsItem':
        return super().__new__(
            cls,
            *args,
            company_contribution_amount=company_contribution_amount,
            employee_deduction_amount=employee_deduction_amount,
            benefit_id=benefit_id,
            _configuration=_configuration,
            **kwargs,
        )
