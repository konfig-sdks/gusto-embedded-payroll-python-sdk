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


class SignatoriesCreateInviteRequest(BaseModel):
    email: str = Field(alias='email')

    title: typing.Optional[str] = Field(None, alias='title')

    first_name: typing.Optional[str] = Field(None, alias='first_name')

    last_name: typing.Optional[str] = Field(None, alias='last_name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
