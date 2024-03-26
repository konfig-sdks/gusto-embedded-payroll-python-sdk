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


class BenefitTypeRequirementsCompanyContributionAnnualMaximum(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            required = schemas.BoolSchema
            editable = schemas.BoolSchema
        
            @staticmethod
            def default_value() -> typing.Type['BenefitTypeRequirementsCompanyContributionAnnualMaximumDefaultValue']:
                return BenefitTypeRequirementsCompanyContributionAnnualMaximumDefaultValue
        
            @staticmethod
            def choices() -> typing.Type['BenefitTypeRequirementsCompanyContributionAnnualMaximumChoices']:
                return BenefitTypeRequirementsCompanyContributionAnnualMaximumChoices
            __annotations__ = {
                "required": required,
                "editable": editable,
                "default_value": default_value,
                "choices": choices,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["required"]) -> MetaOapg.properties.required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["editable"]) -> MetaOapg.properties.editable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_value"]) -> 'BenefitTypeRequirementsCompanyContributionAnnualMaximumDefaultValue': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["choices"]) -> 'BenefitTypeRequirementsCompanyContributionAnnualMaximumChoices': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["required", "editable", "default_value", "choices", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["required"]) -> typing.Union[MetaOapg.properties.required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["editable"]) -> typing.Union[MetaOapg.properties.editable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_value"]) -> typing.Union['BenefitTypeRequirementsCompanyContributionAnnualMaximumDefaultValue', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["choices"]) -> typing.Union['BenefitTypeRequirementsCompanyContributionAnnualMaximumChoices', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["required", "editable", "default_value", "choices", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        required: typing.Union[MetaOapg.properties.required, bool, schemas.Unset] = schemas.unset,
        editable: typing.Union[MetaOapg.properties.editable, bool, schemas.Unset] = schemas.unset,
        default_value: typing.Union['BenefitTypeRequirementsCompanyContributionAnnualMaximumDefaultValue', schemas.Unset] = schemas.unset,
        choices: typing.Union['BenefitTypeRequirementsCompanyContributionAnnualMaximumChoices', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BenefitTypeRequirementsCompanyContributionAnnualMaximum':
        return super().__new__(
            cls,
            *args,
            required=required,
            editable=editable,
            default_value=default_value,
            choices=choices,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.benefit_type_requirements_company_contribution_annual_maximum_choices import BenefitTypeRequirementsCompanyContributionAnnualMaximumChoices
from gusto_embedded_payroll_python_sdk.model.benefit_type_requirements_company_contribution_annual_maximum_default_value import BenefitTypeRequirementsCompanyContributionAnnualMaximumDefaultValue
