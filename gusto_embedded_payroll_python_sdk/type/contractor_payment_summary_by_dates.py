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

from gusto_embedded_payroll_python_sdk.type.contractor_payment_summary_by_dates_contractor_payments import ContractorPaymentSummaryByDatesContractorPayments
from gusto_embedded_payroll_python_sdk.type.contractor_payment_summary_by_dates_total import ContractorPaymentSummaryByDatesTotal

class RequiredContractorPaymentSummaryByDates(TypedDict):
    pass

class OptionalContractorPaymentSummaryByDates(TypedDict, total=False):
    total: ContractorPaymentSummaryByDatesTotal

    contractor_payments: ContractorPaymentSummaryByDatesContractorPayments

class ContractorPaymentSummaryByDates(RequiredContractorPaymentSummaryByDates, OptionalContractorPaymentSummaryByDates):
    pass
