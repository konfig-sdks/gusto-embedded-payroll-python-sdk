# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_id_contractor_payments_contractor_payment_id.delete import CancelPayment
from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_id_contractor_payments.post import CreatePayment
from gusto_embedded_payroll_python_sdk.paths.v1_contractor_payments_contractor_payment_uuid_fund.put import FundContractorPayment
from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_id_contractor_payments_contractor_payment_id.get import GetSinglePayment
from gusto_embedded_payroll_python_sdk.paths.v1_contractor_payments_contractor_payment_uuid_receipt.get import GetSingleReceipt
from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_id_contractor_payments.get import GetWithinTimePeriodTotals
from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_uuid_contractor_payments_preview.get import PreviewDebitDate
from gusto_embedded_payroll_python_sdk.apis.tags.contractor_payments_api_raw import ContractorPaymentsApiRaw


class ContractorPaymentsApi(
    CancelPayment,
    CreatePayment,
    FundContractorPayment,
    GetSinglePayment,
    GetSingleReceipt,
    GetWithinTimePeriodTotals,
    PreviewDebitDate,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ContractorPaymentsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ContractorPaymentsApiRaw(api_client)
