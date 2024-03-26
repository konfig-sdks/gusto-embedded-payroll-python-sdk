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


class Company(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The representation of a company in Gusto.
    """


    class MetaOapg:
        
        class properties:
            ein = schemas.StrSchema
            
            
            class entity_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "C-Corporation": "CCORPORATION",
                        "S-Corporation": "SCORPORATION",
                        "Sole proprietor": "SOLE_PROPRIETOR",
                        "LLC": "LLC",
                        "LLP": "LLP",
                        "Limited partnership": "LIMITED_PARTNERSHIP",
                        "Co-ownership": "COOWNERSHIP",
                        "Association": "ASSOCIATION",
                        "Trusteeship": "TRUSTEESHIP",
                        "General partnership": "GENERAL_PARTNERSHIP",
                        "Joint venture": "JOINT_VENTURE",
                        "Non-Profit": "NONPROFIT",
                    }
                
                @schemas.classproperty
                def CCORPORATION(cls):
                    return cls("C-Corporation")
                
                @schemas.classproperty
                def SCORPORATION(cls):
                    return cls("S-Corporation")
                
                @schemas.classproperty
                def SOLE_PROPRIETOR(cls):
                    return cls("Sole proprietor")
                
                @schemas.classproperty
                def LLC(cls):
                    return cls("LLC")
                
                @schemas.classproperty
                def LLP(cls):
                    return cls("LLP")
                
                @schemas.classproperty
                def LIMITED_PARTNERSHIP(cls):
                    return cls("Limited partnership")
                
                @schemas.classproperty
                def COOWNERSHIP(cls):
                    return cls("Co-ownership")
                
                @schemas.classproperty
                def ASSOCIATION(cls):
                    return cls("Association")
                
                @schemas.classproperty
                def TRUSTEESHIP(cls):
                    return cls("Trusteeship")
                
                @schemas.classproperty
                def GENERAL_PARTNERSHIP(cls):
                    return cls("General partnership")
                
                @schemas.classproperty
                def JOINT_VENTURE(cls):
                    return cls("Joint venture")
                
                @schemas.classproperty
                def NONPROFIT(cls):
                    return cls("Non-Profit")
            
            
            class tier(
                schemas.EnumBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "simple": "SIMPLE",
                        "plus": "PLUS",
                        "premium": "PREMIUM",
                        "core": "CORE",
                        "complete": "COMPLETE",
                        "concierge": "CONCIERGE",
                        "contractor_only": "CONTRACTOR_ONLY",
                        "basic": "BASIC",
                    }
                
                @schemas.classproperty
                def SIMPLE(cls):
                    return cls("simple")
                
                @schemas.classproperty
                def PLUS(cls):
                    return cls("plus")
                
                @schemas.classproperty
                def PREMIUM(cls):
                    return cls("premium")
                
                @schemas.classproperty
                def CORE(cls):
                    return cls("core")
                
                @schemas.classproperty
                def COMPLETE(cls):
                    return cls("complete")
                
                @schemas.classproperty
                def CONCIERGE(cls):
                    return cls("concierge")
                
                @schemas.classproperty
                def CONTRACTOR_ONLY(cls):
                    return cls("contractor_only")
                
                @schemas.classproperty
                def BASIC(cls):
                    return cls("basic")
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tier':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            is_suspended = schemas.BoolSchema
            
            
            class company_status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "Approved": "APPROVED",
                        "Not Approved": "NOT_APPROVED",
                        "Suspended": "SUSPENDED",
                    }
                
                @schemas.classproperty
                def APPROVED(cls):
                    return cls("Approved")
                
                @schemas.classproperty
                def NOT_APPROVED(cls):
                    return cls("Not Approved")
                
                @schemas.classproperty
                def SUSPENDED(cls):
                    return cls("Suspended")
            uuid = schemas.StrSchema
            name = schemas.StrSchema
            trade_name = schemas.StrSchema
            is_partner_managed = schemas.BoolSchema
            
            
            class pay_schedule_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "single": "SINGLE",
                        "hourly_salaried": "HOURLY_SALARIED",
                        "by_employee": "BY_EMPLOYEE",
                        "by_department": "BY_DEPARTMENT",
                    }
                
                @schemas.classproperty
                def SINGLE(cls):
                    return cls("single")
                
                @schemas.classproperty
                def HOURLY_SALARIED(cls):
                    return cls("hourly_salaried")
                
                @schemas.classproperty
                def BY_EMPLOYEE(cls):
                    return cls("by_employee")
                
                @schemas.classproperty
                def BY_DEPARTMENT(cls):
                    return cls("by_department")
            join_date = schemas.StrSchema
            
            
            class funding_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ach": "ACH",
                        "reverse_wire": "REVERSE_WIRE",
                        "wire_in": "WIRE_IN",
                        "brex": "BREX",
                    }
                
                @schemas.classproperty
                def ACH(cls):
                    return cls("ach")
                
                @schemas.classproperty
                def REVERSE_WIRE(cls):
                    return cls("reverse_wire")
                
                @schemas.classproperty
                def WIRE_IN(cls):
                    return cls("wire_in")
                
                @schemas.classproperty
                def BREX(cls):
                    return cls("brex")
            
            
            class locations(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    unique_items = False
                    
                    @staticmethod
                    def items() -> typing.Type['CompanyAddress']:
                        return CompanyAddress
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CompanyAddress'], typing.List['CompanyAddress']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'locations':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CompanyAddress':
                    return super().__getitem__(i)
        
            @staticmethod
            def compensations() -> typing.Type['CompanyCompensations']:
                return CompanyCompensations
        
            @staticmethod
            def primary_signatory() -> typing.Type['CompanyPrimarySignatory']:
                return CompanyPrimarySignatory
        
            @staticmethod
            def primary_payroll_admin() -> typing.Type['CompanyPrimaryPayrollAdmin']:
                return CompanyPrimaryPayrollAdmin
            __annotations__ = {
                "ein": ein,
                "entity_type": entity_type,
                "tier": tier,
                "is_suspended": is_suspended,
                "company_status": company_status,
                "uuid": uuid,
                "name": name,
                "trade_name": trade_name,
                "is_partner_managed": is_partner_managed,
                "pay_schedule_type": pay_schedule_type,
                "join_date": join_date,
                "funding_type": funding_type,
                "locations": locations,
                "compensations": compensations,
                "primary_signatory": primary_signatory,
                "primary_payroll_admin": primary_payroll_admin,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ein"]) -> MetaOapg.properties.ein: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entity_type"]) -> MetaOapg.properties.entity_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tier"]) -> MetaOapg.properties.tier: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_suspended"]) -> MetaOapg.properties.is_suspended: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_status"]) -> MetaOapg.properties.company_status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trade_name"]) -> MetaOapg.properties.trade_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_partner_managed"]) -> MetaOapg.properties.is_partner_managed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pay_schedule_type"]) -> MetaOapg.properties.pay_schedule_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["join_date"]) -> MetaOapg.properties.join_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["funding_type"]) -> MetaOapg.properties.funding_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locations"]) -> MetaOapg.properties.locations: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compensations"]) -> 'CompanyCompensations': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_signatory"]) -> 'CompanyPrimarySignatory': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_payroll_admin"]) -> 'CompanyPrimaryPayrollAdmin': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ein", "entity_type", "tier", "is_suspended", "company_status", "uuid", "name", "trade_name", "is_partner_managed", "pay_schedule_type", "join_date", "funding_type", "locations", "compensations", "primary_signatory", "primary_payroll_admin", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ein"]) -> typing.Union[MetaOapg.properties.ein, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entity_type"]) -> typing.Union[MetaOapg.properties.entity_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tier"]) -> typing.Union[MetaOapg.properties.tier, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_suspended"]) -> typing.Union[MetaOapg.properties.is_suspended, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_status"]) -> typing.Union[MetaOapg.properties.company_status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trade_name"]) -> typing.Union[MetaOapg.properties.trade_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_partner_managed"]) -> typing.Union[MetaOapg.properties.is_partner_managed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pay_schedule_type"]) -> typing.Union[MetaOapg.properties.pay_schedule_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["join_date"]) -> typing.Union[MetaOapg.properties.join_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["funding_type"]) -> typing.Union[MetaOapg.properties.funding_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locations"]) -> typing.Union[MetaOapg.properties.locations, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compensations"]) -> typing.Union['CompanyCompensations', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_signatory"]) -> typing.Union['CompanyPrimarySignatory', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_payroll_admin"]) -> typing.Union['CompanyPrimaryPayrollAdmin', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ein", "entity_type", "tier", "is_suspended", "company_status", "uuid", "name", "trade_name", "is_partner_managed", "pay_schedule_type", "join_date", "funding_type", "locations", "compensations", "primary_signatory", "primary_payroll_admin", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        ein: typing.Union[MetaOapg.properties.ein, str, schemas.Unset] = schemas.unset,
        entity_type: typing.Union[MetaOapg.properties.entity_type, str, schemas.Unset] = schemas.unset,
        tier: typing.Union[MetaOapg.properties.tier, None, str, schemas.Unset] = schemas.unset,
        is_suspended: typing.Union[MetaOapg.properties.is_suspended, bool, schemas.Unset] = schemas.unset,
        company_status: typing.Union[MetaOapg.properties.company_status, str, schemas.Unset] = schemas.unset,
        uuid: typing.Union[MetaOapg.properties.uuid, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        trade_name: typing.Union[MetaOapg.properties.trade_name, str, schemas.Unset] = schemas.unset,
        is_partner_managed: typing.Union[MetaOapg.properties.is_partner_managed, bool, schemas.Unset] = schemas.unset,
        pay_schedule_type: typing.Union[MetaOapg.properties.pay_schedule_type, str, schemas.Unset] = schemas.unset,
        join_date: typing.Union[MetaOapg.properties.join_date, str, schemas.Unset] = schemas.unset,
        funding_type: typing.Union[MetaOapg.properties.funding_type, str, schemas.Unset] = schemas.unset,
        locations: typing.Union[MetaOapg.properties.locations, list, tuple, schemas.Unset] = schemas.unset,
        compensations: typing.Union['CompanyCompensations', schemas.Unset] = schemas.unset,
        primary_signatory: typing.Union['CompanyPrimarySignatory', schemas.Unset] = schemas.unset,
        primary_payroll_admin: typing.Union['CompanyPrimaryPayrollAdmin', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Company':
        return super().__new__(
            cls,
            *args,
            ein=ein,
            entity_type=entity_type,
            tier=tier,
            is_suspended=is_suspended,
            company_status=company_status,
            uuid=uuid,
            name=name,
            trade_name=trade_name,
            is_partner_managed=is_partner_managed,
            pay_schedule_type=pay_schedule_type,
            join_date=join_date,
            funding_type=funding_type,
            locations=locations,
            compensations=compensations,
            primary_signatory=primary_signatory,
            primary_payroll_admin=primary_payroll_admin,
            _configuration=_configuration,
            **kwargs,
        )

from gusto_embedded_payroll_python_sdk.model.company_address import CompanyAddress
from gusto_embedded_payroll_python_sdk.model.company_compensations import CompanyCompensations
from gusto_embedded_payroll_python_sdk.model.company_primary_payroll_admin import CompanyPrimaryPayrollAdmin
from gusto_embedded_payroll_python_sdk.model.company_primary_signatory import CompanyPrimarySignatory
