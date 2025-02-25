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

from gusto_embedded_payroll_python_sdk.type.payroll_receipt_employee_compensations import PayrollReceiptEmployeeCompensations
from gusto_embedded_payroll_python_sdk.type.payroll_receipt_licensee import PayrollReceiptLicensee
from gusto_embedded_payroll_python_sdk.type.payroll_receipt_taxes import PayrollReceiptTaxes
from gusto_embedded_payroll_python_sdk.type.payroll_receipt_totals import PayrollReceiptTotals

class RequiredPayrollReceipt(TypedDict):
    pass

class OptionalPayrollReceipt(TypedDict, total=False):
    # A unique identifier of the payroll receipt.
    payroll_uuid: str

    # A unique identifier of the company for the payroll.
    company_uuid: str

    # The name of the company by whom the payroll was paid
    name_of_sender: str

    # Always the fixed string \"Payroll Recipients\"
    name_of_recipient: str

    # Always the fixed string \"Payroll recipients include the employees listed below plus the tax agencies for the taxes listed below.\"
    recipient_notice: str

    # The debit or funding date for the payroll
    debit_date: str

    # Always the fixed string \"ZenPayroll, Inc., dba Gusto is a licensed money transmitter. For more about Gusto’s licenses and your state-specific rights to request information, submit complaints, dispute errors, or cancel transactions, visit our license page.\"
    license: str

    # URL for the license information for the licensed payroll processor. Always the fixed string \"https://gusto.com/about/licenses\"
    license_uri: str

    right_to_refund: str

    liability_of_licensee: str

    totals: PayrollReceiptTotals

    taxes: PayrollReceiptTaxes

    employee_compensations: PayrollReceiptEmployeeCompensations

    licensee: PayrollReceiptLicensee

class PayrollReceipt(RequiredPayrollReceipt, OptionalPayrollReceipt):
    pass
