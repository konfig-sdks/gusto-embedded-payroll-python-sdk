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

from gusto_embedded_payroll_python_sdk.type.contractor_payments_preview_debit_date422_response_errors_base import ContractorPaymentsPreviewDebitDate422ResponseErrorsBase
from gusto_embedded_payroll_python_sdk.type.contractor_payments_preview_debit_date422_response_errors_check_date import ContractorPaymentsPreviewDebitDate422ResponseErrorsCheckDate

class RequiredContractorPaymentsPreviewDebitDate422ResponseErrors(TypedDict):
    pass

class OptionalContractorPaymentsPreviewDebitDate422ResponseErrors(TypedDict, total=False):
    base: ContractorPaymentsPreviewDebitDate422ResponseErrorsBase

    check_date: ContractorPaymentsPreviewDebitDate422ResponseErrorsCheckDate

class ContractorPaymentsPreviewDebitDate422ResponseErrors(RequiredContractorPaymentsPreviewDebitDate422ResponseErrors, OptionalContractorPaymentsPreviewDebitDate422ResponseErrors):
    pass
