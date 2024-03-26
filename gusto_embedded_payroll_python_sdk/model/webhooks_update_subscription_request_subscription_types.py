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


class WebhooksUpdateSubscriptionRequestSubscriptionTypes(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "BankAccount": "BANK_ACCOUNT",
                    "Company": "COMPANY",
                    "CompanyBenefit": "COMPANY_BENEFIT",
                    "Contractor": "CONTRACTOR",
                    "ContractorPayment": "CONTRACTOR_PAYMENT",
                    "Employee": "EMPLOYEE",
                    "EmployeeBenefit": "EMPLOYEE_BENEFIT",
                    "EmployeeJobCompensation": "EMPLOYEE_JOB_COMPENSATION",
                    "ExternalPayroll": "EXTERNAL_PAYROLL",
                    "Form": "FORM",
                    "Location": "LOCATION",
                    "Notification": "NOTIFICATION",
                    "Payroll": "PAYROLL",
                    "PaySchedule": "PAY_SCHEDULE",
                    "Signatory": "SIGNATORY",
                }
            
            @schemas.classproperty
            def BANK_ACCOUNT(cls):
                return cls("BankAccount")
            
            @schemas.classproperty
            def COMPANY(cls):
                return cls("Company")
            
            @schemas.classproperty
            def COMPANY_BENEFIT(cls):
                return cls("CompanyBenefit")
            
            @schemas.classproperty
            def CONTRACTOR(cls):
                return cls("Contractor")
            
            @schemas.classproperty
            def CONTRACTOR_PAYMENT(cls):
                return cls("ContractorPayment")
            
            @schemas.classproperty
            def EMPLOYEE(cls):
                return cls("Employee")
            
            @schemas.classproperty
            def EMPLOYEE_BENEFIT(cls):
                return cls("EmployeeBenefit")
            
            @schemas.classproperty
            def EMPLOYEE_JOB_COMPENSATION(cls):
                return cls("EmployeeJobCompensation")
            
            @schemas.classproperty
            def EXTERNAL_PAYROLL(cls):
                return cls("ExternalPayroll")
            
            @schemas.classproperty
            def FORM(cls):
                return cls("Form")
            
            @schemas.classproperty
            def LOCATION(cls):
                return cls("Location")
            
            @schemas.classproperty
            def NOTIFICATION(cls):
                return cls("Notification")
            
            @schemas.classproperty
            def PAYROLL(cls):
                return cls("Payroll")
            
            @schemas.classproperty
            def PAY_SCHEDULE(cls):
                return cls("PaySchedule")
            
            @schemas.classproperty
            def SIGNATORY(cls):
                return cls("Signatory")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'WebhooksUpdateSubscriptionRequestSubscriptionTypes':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
