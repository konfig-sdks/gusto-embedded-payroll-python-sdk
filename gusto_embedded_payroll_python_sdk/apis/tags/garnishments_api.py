# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_id_garnishments.post import CreateGarnishment
from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_id_garnishments.get import GetEmployeeGarnishments
from gusto_embedded_payroll_python_sdk.paths.v1_garnishments_garnishment_id.get import GetGarnishment
from gusto_embedded_payroll_python_sdk.paths.v1_garnishments_garnishment_id.put import UpdateGarnishment
from gusto_embedded_payroll_python_sdk.apis.tags.garnishments_api_raw import GarnishmentsApiRaw


class GarnishmentsApi(
    CreateGarnishment,
    GetEmployeeGarnishments,
    GetGarnishment,
    UpdateGarnishment,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: GarnishmentsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = GarnishmentsApiRaw(api_client)
