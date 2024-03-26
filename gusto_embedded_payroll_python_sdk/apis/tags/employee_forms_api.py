# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_embedded_payroll_python_sdk.paths.v1_sandbox_generate_w2.post import GenerateW2Document
from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_id_forms.get import GetAllEmployeeForms
from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_id_forms_form_id.get import GetFormById
from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_id_forms_form_id_pdf.get import GetPdfLink
from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_id_forms_form_id_sign.put import SignForm
from gusto_embedded_payroll_python_sdk.apis.tags.employee_forms_api_raw import EmployeeFormsApiRaw


class EmployeeFormsApi(
    GenerateW2Document,
    GetAllEmployeeForms,
    GetFormById,
    GetPdfLink,
    SignForm,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EmployeeFormsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EmployeeFormsApiRaw(api_client)
