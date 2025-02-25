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


class PayrollReversal(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            reversed_payroll_uuid = schemas.StrSchema
            reversal_payroll_uuid = schemas.StrSchema
            reason = schemas.StrSchema
            
            
            class approved_at(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'approved_at':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class category(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.IntSchema
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'category':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def reversed_employee_uuids() -> typing.Type['PayrollReversalReversedEmployeeUuids']:
                return PayrollReversalReversedEmployeeUuids
            __annotations__ = {
                "reversed_payroll_uuid": reversed_payroll_uuid,
                "reversal_payroll_uuid": reversal_payroll_uuid,
                "reason": reason,
                "approved_at": approved_at,
                "category": category,
                "reversed_employee_uuids": reversed_employee_uuids,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reversed_payroll_uuid"]) -> MetaOapg.properties.reversed_payroll_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reversal_payroll_uuid"]) -> MetaOapg.properties.reversal_payroll_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reason"]) -> MetaOapg.properties.reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approved_at"]) -> MetaOapg.properties.approved_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reversed_employee_uuids"]) -> 'PayrollReversalReversedEmployeeUuids': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["reversed_payroll_uuid", "reversal_payroll_uuid", "reason", "approved_at", "category", "reversed_employee_uuids", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reversed_payroll_uuid"]) -> typing.Union[MetaOapg.properties.reversed_payroll_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reversal_payroll_uuid"]) -> typing.Union[MetaOapg.properties.reversal_payroll_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reason"]) -> typing.Union[MetaOapg.properties.reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approved_at"]) -> typing.Union[MetaOapg.properties.approved_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reversed_employee_uuids"]) -> typing.Union['PayrollReversalReversedEmployeeUuids', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["reversed_payroll_uuid", "reversal_payroll_uuid", "reason", "approved_at", "category", "reversed_employee_uuids", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        reversed_payroll_uuid: typing.Union[MetaOapg.properties.reversed_payroll_uuid, str, schemas.Unset] = schemas.unset,
        reversal_payroll_uuid: typing.Union[MetaOapg.properties.reversal_payroll_uuid, str, schemas.Unset] = schemas.unset,
        reason: typing.Union[MetaOapg.properties.reason, str, schemas.Unset] = schemas.unset,
        approved_at: typing.Union[MetaOapg.properties.approved_at, None, str, schemas.Unset] = schemas.unset,
        category: typing.Union[MetaOapg.properties.category, list, tuple, schemas.Unset] = schemas.unset,
        reversed_employee_uuids: typing.Union['PayrollReversalReversedEmployeeUuids', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayrollReversal':
        return super().__new__(
            cls,
            *args,
            reversed_payroll_uuid=reversed_payroll_uuid,
            reversal_payroll_uuid=reversal_payroll_uuid,
            reason=reason,
            approved_at=approved_at,
            category=category,
            reversed_employee_uuids=reversed_employee_uuids,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.payroll_reversal_reversed_employee_uuids import PayrollReversalReversedEmployeeUuids
