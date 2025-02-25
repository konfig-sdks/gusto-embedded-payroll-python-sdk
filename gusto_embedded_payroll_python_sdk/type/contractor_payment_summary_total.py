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


class RequiredContractorPaymentSummaryTotal(TypedDict):
    pass

class OptionalContractorPaymentSummaryTotal(TypedDict, total=False):
    # The total reimbursements for contractor payments within a given time period.
    reimbursements: str

    # The total wages for contractor payments within a given time period.
    wages: str

class ContractorPaymentSummaryTotal(RequiredContractorPaymentSummaryTotal, OptionalContractorPaymentSummaryTotal):
    pass
