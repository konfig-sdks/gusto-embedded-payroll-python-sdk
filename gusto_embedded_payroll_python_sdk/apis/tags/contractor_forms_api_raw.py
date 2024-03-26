# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_embedded_payroll_python_sdk.paths.v1_sandbox_generate_1099.post import Create1099FormRaw
from gusto_embedded_payroll_python_sdk.paths.v1_contractors_contractor_uuid_forms_form_id.get import GetByIdFormRaw
from gusto_embedded_payroll_python_sdk.paths.v1_contractors_contractor_uuid_forms_form_id_pdf.get import GetPdfLinkRaw
from gusto_embedded_payroll_python_sdk.paths.v1_contractors_contractor_uuid_forms.get import ListAllRaw


class ContractorFormsApiRaw(
    Create1099FormRaw,
    GetByIdFormRaw,
    GetPdfLinkRaw,
    ListAllRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
