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

from gusto_embedded_payroll_python_sdk.pydantic.contractor_payment_summary_contractor_payments import ContractorPaymentSummaryContractorPayments
from gusto_embedded_payroll_python_sdk.pydantic.contractor_payment_summary_total import ContractorPaymentSummaryTotal

class ContractorPaymentSummary(BaseModel):
    total: typing.Optional[ContractorPaymentSummaryTotal] = Field(None, alias='total')

    contractor_payments: typing.Optional[ContractorPaymentSummaryContractorPayments] = Field(None, alias='contractor_payments')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
