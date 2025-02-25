# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from gusto_embedded_payroll_python_sdk.type.payrolls_update_payroll_by_id_request_employee_compensations_item_fixed_compensations import PayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemFixedCompensations
from gusto_embedded_payroll_python_sdk.type.payrolls_update_payroll_by_id_request_employee_compensations_item_hourly_compensations import PayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemHourlyCompensations
from gusto_embedded_payroll_python_sdk.type.payrolls_update_payroll_by_id_request_employee_compensations_item_paid_time_off import PayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemPaidTimeOff

class RequiredPayrollsUpdatePayrollByIdRequestEmployeeCompensationsItem(TypedDict):
    pass

class OptionalPayrollsUpdatePayrollByIdRequestEmployeeCompensationsItem(TypedDict, total=False):
    # The current version of this employee compensation from the prepared payroll. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.
    version: str

    # The UUID of the employee.
    employee_uuid: str

    # This employee will be excluded from payroll calculation and will not be paid for the payroll.
    excluded: bool

    # The employee's compensation payment method. Invalid values will be ignored.
    payment_method: str

    # Custom text that will be printed as a personal note to the employee on a paystub.
    memo: str

    fixed_compensations: PayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemFixedCompensations

    hourly_compensations: PayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemHourlyCompensations

    paid_time_off: PayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemPaidTimeOff

class PayrollsUpdatePayrollByIdRequestEmployeeCompensationsItem(RequiredPayrollsUpdatePayrollByIdRequestEmployeeCompensationsItem, OptionalPayrollsUpdatePayrollByIdRequestEmployeeCompensationsItem):
    pass
