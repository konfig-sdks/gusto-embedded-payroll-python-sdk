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

from gusto_embedded_payroll_python_sdk.pydantic.industry_selection_update_company_industry_selection_request_sic_codes import IndustrySelectionUpdateCompanyIndustrySelectionRequestSicCodes

class IndustrySelectionUpdateCompanyIndustrySelectionRequest(BaseModel):
    # Industry title
    title: str = Field(alias='title')

    # North American Industry Classification System (NAICS) is used to classify businesses with a six digit number based on the primary type of work the business performs
    naics_code: str = Field(alias='naics_code')

    sic_codes: typing.Optional[IndustrySelectionUpdateCompanyIndustrySelectionRequestSicCodes] = Field(None, alias='sic_codes')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
