# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_id_home_addresses.post import CreateHomeAddressRaw
from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_id_work_addresses.post import CreateWorkAddressRaw
from gusto_embedded_payroll_python_sdk.paths.v1_home_addresses_home_address_uuid.delete import DeleteHomeRaw
from gusto_embedded_payroll_python_sdk.paths.v1_work_addresses_work_address_uuid.delete import DeleteWorkAddressRaw
from gusto_embedded_payroll_python_sdk.paths.v1_home_addresses_home_address_uuid.get import GetHomeAddressRaw
from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_id_home_addresses.get import GetHomeAddressesRaw
from gusto_embedded_payroll_python_sdk.paths.v1_work_addresses_work_address_uuid.get import GetWorkAddressRaw
from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_id_work_addresses.get import ListWorkAddressesRaw
from gusto_embedded_payroll_python_sdk.paths.v1_home_addresses_home_address_uuid.put import UpdateHomeAddressRaw
from gusto_embedded_payroll_python_sdk.paths.v1_work_addresses_work_address_uuid.put import UpdateWorkAddressRaw


class EmployeeAddressesApiRaw(
    CreateHomeAddressRaw,
    CreateWorkAddressRaw,
    DeleteHomeRaw,
    DeleteWorkAddressRaw,
    GetHomeAddressRaw,
    GetHomeAddressesRaw,
    GetWorkAddressRaw,
    ListWorkAddressesRaw,
    UpdateHomeAddressRaw,
    UpdateWorkAddressRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
