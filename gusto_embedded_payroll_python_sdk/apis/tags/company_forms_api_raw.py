# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_id_forms.get import GetAllFormsRaw
from gusto_embedded_payroll_python_sdk.paths.v1_forms_form_id.get import GetFormByIdRaw
from gusto_embedded_payroll_python_sdk.paths.v1_forms_form_id_pdf.get import GetPdfLinkRaw
from gusto_embedded_payroll_python_sdk.paths.v1_forms_form_id_sign.put import SignFormRaw


class CompanyFormsApiRaw(
    GetAllFormsRaw,
    GetFormByIdRaw,
    GetPdfLinkRaw,
    SignFormRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
