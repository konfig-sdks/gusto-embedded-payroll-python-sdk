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


class RequiredCompaniesMigrateToEmbeddedPayrollResponse(TypedDict):
    pass

class OptionalCompaniesMigrateToEmbeddedPayrollResponse(TypedDict, total=False):
    # The company UUID
    company_uuid: str

    # The migration status
    migration_status: str

class CompaniesMigrateToEmbeddedPayrollResponse(RequiredCompaniesMigrateToEmbeddedPayrollResponse, OptionalCompaniesMigrateToEmbeddedPayrollResponse):
    pass
