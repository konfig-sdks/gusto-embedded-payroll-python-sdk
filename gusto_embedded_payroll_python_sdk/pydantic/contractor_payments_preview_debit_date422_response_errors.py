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

from gusto_embedded_payroll_python_sdk.pydantic.contractor_payments_preview_debit_date422_response_errors_base import ContractorPaymentsPreviewDebitDate422ResponseErrorsBase
from gusto_embedded_payroll_python_sdk.pydantic.contractor_payments_preview_debit_date422_response_errors_check_date import ContractorPaymentsPreviewDebitDate422ResponseErrorsCheckDate

class ContractorPaymentsPreviewDebitDate422ResponseErrors(BaseModel):
    base: typing.Optional[ContractorPaymentsPreviewDebitDate422ResponseErrorsBase] = Field(None, alias='base')

    check_date: typing.Optional[ContractorPaymentsPreviewDebitDate422ResponseErrorsCheckDate] = Field(None, alias='check_date')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
