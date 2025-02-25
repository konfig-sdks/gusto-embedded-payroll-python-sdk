# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_embedded_payroll_python_sdk.paths.v1_contractors_contractor_uuid_bank_accounts.post import CreateBankAccountRaw
from gusto_embedded_payroll_python_sdk.paths.v1_contractors_contractor_uuid_payment_method.get import GetContractorPaymentMethodRaw
from gusto_embedded_payroll_python_sdk.paths.v1_contractors_contractor_uuid_bank_accounts.get import ListBankAccountsRaw
from gusto_embedded_payroll_python_sdk.paths.v1_contractors_contractor_uuid_payment_method.put import UpdateBankAccountRaw


class ContractorPaymentMethodApiRaw(
    CreateBankAccountRaw,
    GetContractorPaymentMethodRaw,
    ListBankAccountsRaw,
    UpdateBankAccountRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
