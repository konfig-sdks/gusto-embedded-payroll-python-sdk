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


class EmployeeFederalTax(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            version = schemas.StrSchema
            filing_status = schemas.StrSchema
            extra_withholding = schemas.StrSchema
            two_jobs = schemas.BoolSchema
            dependents_amount = schemas.StrSchema
            other_income = schemas.StrSchema
            deductions = schemas.StrSchema
            
            
            class w4_data_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "pre_2020_w4": "PRE_2020_W4",
                        "rev_2020_w4": "REV_2020_W4",
                    }
                
                @schemas.classproperty
                def PRE_2020_W4(cls):
                    return cls("pre_2020_w4")
                
                @schemas.classproperty
                def REV_2020_W4(cls):
                    return cls("rev_2020_w4")
            federal_withholding_allowance = schemas.StrSchema
            additional_withholding = schemas.BoolSchema
            __annotations__ = {
                "version": version,
                "filing_status": filing_status,
                "extra_withholding": extra_withholding,
                "two_jobs": two_jobs,
                "dependents_amount": dependents_amount,
                "other_income": other_income,
                "deductions": deductions,
                "w4_data_type": w4_data_type,
                "federal_withholding_allowance": federal_withholding_allowance,
                "additional_withholding": additional_withholding,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filing_status"]) -> MetaOapg.properties.filing_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["extra_withholding"]) -> MetaOapg.properties.extra_withholding: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["two_jobs"]) -> MetaOapg.properties.two_jobs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dependents_amount"]) -> MetaOapg.properties.dependents_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["other_income"]) -> MetaOapg.properties.other_income: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deductions"]) -> MetaOapg.properties.deductions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["w4_data_type"]) -> MetaOapg.properties.w4_data_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["federal_withholding_allowance"]) -> MetaOapg.properties.federal_withholding_allowance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additional_withholding"]) -> MetaOapg.properties.additional_withholding: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "filing_status", "extra_withholding", "two_jobs", "dependents_amount", "other_income", "deductions", "w4_data_type", "federal_withholding_allowance", "additional_withholding", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filing_status"]) -> typing.Union[MetaOapg.properties.filing_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["extra_withholding"]) -> typing.Union[MetaOapg.properties.extra_withholding, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["two_jobs"]) -> typing.Union[MetaOapg.properties.two_jobs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dependents_amount"]) -> typing.Union[MetaOapg.properties.dependents_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["other_income"]) -> typing.Union[MetaOapg.properties.other_income, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deductions"]) -> typing.Union[MetaOapg.properties.deductions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["w4_data_type"]) -> typing.Union[MetaOapg.properties.w4_data_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["federal_withholding_allowance"]) -> typing.Union[MetaOapg.properties.federal_withholding_allowance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additional_withholding"]) -> typing.Union[MetaOapg.properties.additional_withholding, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "filing_status", "extra_withholding", "two_jobs", "dependents_amount", "other_income", "deductions", "w4_data_type", "federal_withholding_allowance", "additional_withholding", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        version: typing.Union[MetaOapg.properties.version, str, schemas.Unset] = schemas.unset,
        filing_status: typing.Union[MetaOapg.properties.filing_status, str, schemas.Unset] = schemas.unset,
        extra_withholding: typing.Union[MetaOapg.properties.extra_withholding, str, schemas.Unset] = schemas.unset,
        two_jobs: typing.Union[MetaOapg.properties.two_jobs, bool, schemas.Unset] = schemas.unset,
        dependents_amount: typing.Union[MetaOapg.properties.dependents_amount, str, schemas.Unset] = schemas.unset,
        other_income: typing.Union[MetaOapg.properties.other_income, str, schemas.Unset] = schemas.unset,
        deductions: typing.Union[MetaOapg.properties.deductions, str, schemas.Unset] = schemas.unset,
        w4_data_type: typing.Union[MetaOapg.properties.w4_data_type, str, schemas.Unset] = schemas.unset,
        federal_withholding_allowance: typing.Union[MetaOapg.properties.federal_withholding_allowance, str, schemas.Unset] = schemas.unset,
        additional_withholding: typing.Union[MetaOapg.properties.additional_withholding, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EmployeeFederalTax':
        return super().__new__(
            cls,
            *args,
            version=version,
            filing_status=filing_status,
            extra_withholding=extra_withholding,
            two_jobs=two_jobs,
            dependents_amount=dependents_amount,
            other_income=other_income,
            deductions=deductions,
            w4_data_type=w4_data_type,
            federal_withholding_allowance=federal_withholding_allowance,
            additional_withholding=additional_withholding,
            _configuration=_configuration,
            **kwargs,
        )
