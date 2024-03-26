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

from gusto_embedded_payroll_python_sdk.pydantic.rehire_body import RehireBody
from gusto_embedded_payroll_python_sdk.pydantic.versionable_required import VersionableRequired

EmployeeEmploymentsUpdateRehireRequest = typing.Union[VersionableRequired,RehireBody]
