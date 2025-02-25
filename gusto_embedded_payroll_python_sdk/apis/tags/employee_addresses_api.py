# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_id_home_addresses.post import CreateHomeAddress
from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_id_work_addresses.post import CreateWorkAddress
from gusto_embedded_payroll_python_sdk.paths.v1_home_addresses_home_address_uuid.delete import DeleteHome
from gusto_embedded_payroll_python_sdk.paths.v1_work_addresses_work_address_uuid.delete import DeleteWorkAddress
from gusto_embedded_payroll_python_sdk.paths.v1_home_addresses_home_address_uuid.get import GetHomeAddress
from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_id_home_addresses.get import GetHomeAddresses
from gusto_embedded_payroll_python_sdk.paths.v1_work_addresses_work_address_uuid.get import GetWorkAddress
from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_id_work_addresses.get import ListWorkAddresses
from gusto_embedded_payroll_python_sdk.paths.v1_home_addresses_home_address_uuid.put import UpdateHomeAddress
from gusto_embedded_payroll_python_sdk.paths.v1_work_addresses_work_address_uuid.put import UpdateWorkAddress
from gusto_embedded_payroll_python_sdk.apis.tags.employee_addresses_api_raw import EmployeeAddressesApiRaw


class EmployeeAddressesApi(
    CreateHomeAddress,
    CreateWorkAddress,
    DeleteHome,
    DeleteWorkAddress,
    GetHomeAddress,
    GetHomeAddresses,
    GetWorkAddress,
    ListWorkAddresses,
    UpdateHomeAddress,
    UpdateWorkAddress,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EmployeeAddressesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EmployeeAddressesApiRaw(api_client)
