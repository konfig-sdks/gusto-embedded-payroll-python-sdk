# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_uuid_federal_taxes.get import GetFederalTaxesById
from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_uuid_state_taxes.get import GetStateTaxes
from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_uuid_federal_taxes.put import UpdateFederalTaxes
from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_uuid_state_taxes.put import UpdateStateTaxes
from gusto_embedded_payroll_python_sdk.apis.tags.employee_tax_setup_api_raw import EmployeeTaxSetupApiRaw


class EmployeeTaxSetupApi(
    GetFederalTaxesById,
    GetStateTaxes,
    UpdateFederalTaxes,
    UpdateStateTaxes,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EmployeeTaxSetupApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EmployeeTaxSetupApiRaw(api_client)
