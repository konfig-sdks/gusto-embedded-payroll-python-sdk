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


class DepartmentsAddPeopleToDepartmentRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            version = schemas.StrSchema
        
            @staticmethod
            def employees() -> typing.Type['DepartmentsAddPeopleToDepartmentRequestEmployees']:
                return DepartmentsAddPeopleToDepartmentRequestEmployees
        
            @staticmethod
            def contractors() -> typing.Type['DepartmentsAddPeopleToDepartmentRequestContractors']:
                return DepartmentsAddPeopleToDepartmentRequestContractors
            __annotations__ = {
                "version": version,
                "employees": employees,
                "contractors": contractors,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employees"]) -> 'DepartmentsAddPeopleToDepartmentRequestEmployees': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractors"]) -> 'DepartmentsAddPeopleToDepartmentRequestContractors': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "employees", "contractors", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employees"]) -> typing.Union['DepartmentsAddPeopleToDepartmentRequestEmployees', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractors"]) -> typing.Union['DepartmentsAddPeopleToDepartmentRequestContractors', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "employees", "contractors", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        version: typing.Union[MetaOapg.properties.version, str, schemas.Unset] = schemas.unset,
        employees: typing.Union['DepartmentsAddPeopleToDepartmentRequestEmployees', schemas.Unset] = schemas.unset,
        contractors: typing.Union['DepartmentsAddPeopleToDepartmentRequestContractors', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DepartmentsAddPeopleToDepartmentRequest':
        return super().__new__(
            cls,
            *args,
            version=version,
            employees=employees,
            contractors=contractors,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.departments_add_people_to_department_request_contractors import DepartmentsAddPeopleToDepartmentRequestContractors
from gusto_embedded_payroll_python_sdk.model.departments_add_people_to_department_request_employees import DepartmentsAddPeopleToDepartmentRequestEmployees
