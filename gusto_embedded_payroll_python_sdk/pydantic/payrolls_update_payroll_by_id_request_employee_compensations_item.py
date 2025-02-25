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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from gusto_embedded_payroll_python_sdk.pydantic.payrolls_update_payroll_by_id_request_employee_compensations_item_fixed_compensations import PayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemFixedCompensations
from gusto_embedded_payroll_python_sdk.pydantic.payrolls_update_payroll_by_id_request_employee_compensations_item_hourly_compensations import PayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemHourlyCompensations
from gusto_embedded_payroll_python_sdk.pydantic.payrolls_update_payroll_by_id_request_employee_compensations_item_paid_time_off import PayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemPaidTimeOff

class PayrollsUpdatePayrollByIdRequestEmployeeCompensationsItem(BaseModel):
    # The current version of this employee compensation from the prepared payroll. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field.
    version: typing.Optional[str] = Field(None, alias='version')

    # The UUID of the employee.
    employee_uuid: typing.Optional[str] = Field(None, alias='employee_uuid')

    # This employee will be excluded from payroll calculation and will not be paid for the payroll.
    excluded: typing.Optional[bool] = Field(None, alias='excluded')

    # The employee's compensation payment method. Invalid values will be ignored.
    payment_method: typing.Optional[Literal["Direct Deposit", "Check"]] = Field(None, alias='payment_method')

    # Custom text that will be printed as a personal note to the employee on a paystub.
    memo: typing.Optional[str] = Field(None, alias='memo')

    fixed_compensations: typing.Optional[PayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemFixedCompensations] = Field(None, alias='fixed_compensations')

    hourly_compensations: typing.Optional[PayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemHourlyCompensations] = Field(None, alias='hourly_compensations')

    paid_time_off: typing.Optional[PayrollsUpdatePayrollByIdRequestEmployeeCompensationsItemPaidTimeOff] = Field(None, alias='paid_time_off')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
