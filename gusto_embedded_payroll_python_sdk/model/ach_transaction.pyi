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


class AchTransaction(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Representation of an ACH transaction
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            uuid = schemas.StrSchema
            company_uuid = schemas.StrSchema
            
            
            class payment_event_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def PAYROLL(cls):
                    return cls("Payroll")
                
                @schemas.classproperty
                def CONTRACTOR_PAYMENT(cls):
                    return cls("ContractorPayment")
            payment_event_uuid = schemas.StrSchema
            
            
            class recipient_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EMPLOYEE(cls):
                    return cls("Employee")
                
                @schemas.classproperty
                def CONTRACTOR(cls):
                    return cls("Contractor")
            recipient_uuid = schemas.StrSchema
            error_code = schemas.StrSchema
            transaction_type = schemas.StrSchema
            
            
            class payment_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def UNSUBMITTED(cls):
                    return cls("unsubmitted")
                
                @schemas.classproperty
                def SUBMITTED(cls):
                    return cls("submitted")
                
                @schemas.classproperty
                def SUCCESSFUL(cls):
                    return cls("successful")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("failed")
            
            
            class payment_direction(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CREDIT(cls):
                    return cls("credit")
                
                @schemas.classproperty
                def DEBIT(cls):
                    return cls("debit")
            payment_event_check_date = schemas.StrSchema
            payment_date = schemas.StrSchema
            amount = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "uuid": uuid,
                "company_uuid": company_uuid,
                "payment_event_type": payment_event_type,
                "payment_event_uuid": payment_event_uuid,
                "recipient_type": recipient_type,
                "recipient_uuid": recipient_uuid,
                "error_code": error_code,
                "transaction_type": transaction_type,
                "payment_status": payment_status,
                "payment_direction": payment_direction,
                "payment_event_check_date": payment_event_check_date,
                "payment_date": payment_date,
                "amount": amount,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_uuid"]) -> MetaOapg.properties.company_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_event_type"]) -> MetaOapg.properties.payment_event_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_event_uuid"]) -> MetaOapg.properties.payment_event_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipient_type"]) -> MetaOapg.properties.recipient_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recipient_uuid"]) -> MetaOapg.properties.recipient_uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error_code"]) -> MetaOapg.properties.error_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_type"]) -> MetaOapg.properties.transaction_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_status"]) -> MetaOapg.properties.payment_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_direction"]) -> MetaOapg.properties.payment_direction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_event_check_date"]) -> MetaOapg.properties.payment_event_check_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_date"]) -> MetaOapg.properties.payment_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "uuid", "company_uuid", "payment_event_type", "payment_event_uuid", "recipient_type", "recipient_uuid", "error_code", "transaction_type", "payment_status", "payment_direction", "payment_event_check_date", "payment_date", "amount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_uuid"]) -> typing.Union[MetaOapg.properties.company_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_event_type"]) -> typing.Union[MetaOapg.properties.payment_event_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_event_uuid"]) -> typing.Union[MetaOapg.properties.payment_event_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipient_type"]) -> typing.Union[MetaOapg.properties.recipient_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recipient_uuid"]) -> typing.Union[MetaOapg.properties.recipient_uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error_code"]) -> typing.Union[MetaOapg.properties.error_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_type"]) -> typing.Union[MetaOapg.properties.transaction_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_status"]) -> typing.Union[MetaOapg.properties.payment_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_direction"]) -> typing.Union[MetaOapg.properties.payment_direction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_event_check_date"]) -> typing.Union[MetaOapg.properties.payment_event_check_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_date"]) -> typing.Union[MetaOapg.properties.payment_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "uuid", "company_uuid", "payment_event_type", "payment_event_uuid", "recipient_type", "recipient_uuid", "error_code", "transaction_type", "payment_status", "payment_direction", "payment_event_check_date", "payment_date", "amount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        uuid: typing.Union[MetaOapg.properties.uuid, str, schemas.Unset] = schemas.unset,
        company_uuid: typing.Union[MetaOapg.properties.company_uuid, str, schemas.Unset] = schemas.unset,
        payment_event_type: typing.Union[MetaOapg.properties.payment_event_type, str, schemas.Unset] = schemas.unset,
        payment_event_uuid: typing.Union[MetaOapg.properties.payment_event_uuid, str, schemas.Unset] = schemas.unset,
        recipient_type: typing.Union[MetaOapg.properties.recipient_type, str, schemas.Unset] = schemas.unset,
        recipient_uuid: typing.Union[MetaOapg.properties.recipient_uuid, str, schemas.Unset] = schemas.unset,
        error_code: typing.Union[MetaOapg.properties.error_code, str, schemas.Unset] = schemas.unset,
        transaction_type: typing.Union[MetaOapg.properties.transaction_type, str, schemas.Unset] = schemas.unset,
        payment_status: typing.Union[MetaOapg.properties.payment_status, str, schemas.Unset] = schemas.unset,
        payment_direction: typing.Union[MetaOapg.properties.payment_direction, str, schemas.Unset] = schemas.unset,
        payment_event_check_date: typing.Union[MetaOapg.properties.payment_event_check_date, str, schemas.Unset] = schemas.unset,
        payment_date: typing.Union[MetaOapg.properties.payment_date, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AchTransaction':
        return super().__new__(
            cls,
            *args,
            description=description,
            uuid=uuid,
            company_uuid=company_uuid,
            payment_event_type=payment_event_type,
            payment_event_uuid=payment_event_uuid,
            recipient_type=recipient_type,
            recipient_uuid=recipient_uuid,
            error_code=error_code,
            transaction_type=transaction_type,
            payment_status=payment_status,
            payment_direction=payment_direction,
            payment_event_check_date=payment_event_check_date,
            payment_date=payment_date,
            amount=amount,
            _configuration=_configuration,
            **kwargs,
        )
