# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_id_payroll_reversals.get import ApprovedReversalsRaw
from gusto_embedded_payroll_python_sdk.paths.v1_payrolls_payroll_uuid_gross_up.post import CalculateGrossUpRaw
from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_id_payrolls_payroll_id_calculate.put import CalculateGrossUp0Raw
from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_id_payrolls_payroll_id_cancel.put import CancelPayrollTransitionRaw
from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_id_payrolls.post import CreateOffCyclePayrollRaw
from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_id_payrolls_payroll_id.delete import DeleteUnprocessedPayrollRaw
from gusto_embedded_payroll_python_sdk.paths.v1_payrolls_payroll_id_generated_documents_printable_payroll_checks.post import GeneratePrintableChecksRaw
from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_uuid_payrolls_blockers.get import GetAllPayrollBlockersRaw
from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_id_payrolls.get import GetCompanyPayrollsRaw
from gusto_embedded_payroll_python_sdk.paths.v1_payrolls_payroll_id_employees_employee_id_pay_stub.get import GetEmployeePayStubRaw
from gusto_embedded_payroll_python_sdk.paths.v1_employees_employee_id_pay_stubs.get import GetEmployeePayStubsRaw
from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_id_payrolls_payroll_id.get import GetSinglePayrollRaw
from gusto_embedded_payroll_python_sdk.paths.v1_payrolls_payroll_uuid_receipt.get import GetSingleReceiptRaw
from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_id_payrolls_payroll_id_prepare.put import PrepareForUpdateRaw
from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_uuid_payrolls_skip.post import SkipPayrollRaw
from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_id_payrolls_payroll_id_submit.put import SubmitPayrollRaw
from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_id_payrolls_payroll_id.put import UpdatePayrollByIdRaw


class PayrollsApiRaw(
    ApprovedReversalsRaw,
    CalculateGrossUpRaw,
    CalculateGrossUp0Raw,
    CancelPayrollTransitionRaw,
    CreateOffCyclePayrollRaw,
    DeleteUnprocessedPayrollRaw,
    GeneratePrintableChecksRaw,
    GetAllPayrollBlockersRaw,
    GetCompanyPayrollsRaw,
    GetEmployeePayStubRaw,
    GetEmployeePayStubsRaw,
    GetSinglePayrollRaw,
    GetSingleReceiptRaw,
    PrepareForUpdateRaw,
    SkipPayrollRaw,
    SubmitPayrollRaw,
    UpdatePayrollByIdRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
