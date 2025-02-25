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
from pydantic import BaseModel, Field, RootModel, ConfigDict


class CompaniesCreateAdminRequest(BaseModel):
    # The first name of the admin.
    first_name: str = Field(alias='first_name')

    # The last name of the admin.
    last_name: str = Field(alias='last_name')

    # The email of the admin for Gusto's system. If the email matches an existing user, this will create an admin account for them.
    email: str = Field(alias='email')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
