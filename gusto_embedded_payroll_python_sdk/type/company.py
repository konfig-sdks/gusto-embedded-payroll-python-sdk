# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from gusto_embedded_payroll_python_sdk.type.company_address import CompanyAddress
from gusto_embedded_payroll_python_sdk.type.company_compensations import CompanyCompensations
from gusto_embedded_payroll_python_sdk.type.company_primary_payroll_admin import CompanyPrimaryPayrollAdmin
from gusto_embedded_payroll_python_sdk.type.company_primary_signatory import CompanyPrimarySignatory

class RequiredCompany(TypedDict):
    pass

class OptionalCompany(TypedDict, total=False):
    # The Federal Employer Identification Number of the company.
    ein: str

    # The tax payer type of the company.
    entity_type: str

    # The Gusto product tier of the company (not applicable to Embedded partner managed companies).
    tier: typing.Optional[str]

    # Whether or not the company is suspended in Gusto. Suspended companies may not run payroll.
    is_suspended: bool

    # The status of the company in Gusto. \"Approved\" companies may run payroll with Gusto. \"Not Approved\" companies may not yet run payroll with Gusto. In order to run payroll, the company may need to complete onboarding or contact support. \"Suspended\" companies may not run payroll with Gusto. In order to unsuspend their account, the company must contact support.
    company_status: str

    # A unique identifier of the company in Gusto.
    uuid: str

    # The name of the company.
    name: str

    # The trade name of the company.
    trade_name: str

    # Whether the company is fully managed by a partner via the API
    is_partner_managed: bool

    # The pay schedule assignment type.
    pay_schedule_type: str

    # Company's first invoiceable event date
    join_date: str

    # Company's default funding type
    funding_type: str

    # The locations of the company.
    locations: typing.List[CompanyAddress]

    compensations: CompanyCompensations

    primary_signatory: CompanyPrimarySignatory

    primary_payroll_admin: CompanyPrimaryPayrollAdmin

class Company(RequiredCompany, OptionalCompany):
    pass
