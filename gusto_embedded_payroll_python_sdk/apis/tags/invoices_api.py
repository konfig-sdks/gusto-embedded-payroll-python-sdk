# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_embedded_payroll_python_sdk.paths.v1_invoices_invoice_period.get import GetInvoicingDataForCompanies
from gusto_embedded_payroll_python_sdk.apis.tags.invoices_api_raw import InvoicesApiRaw


class InvoicesApi(
    GetInvoicingDataForCompanies,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: InvoicesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = InvoicesApiRaw(api_client)
