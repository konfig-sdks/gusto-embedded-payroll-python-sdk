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

from gusto_embedded_payroll_python_sdk.pydantic.off_cycle_reason_type import OffCycleReasonType
from gusto_embedded_payroll_python_sdk.pydantic.payroll_company_taxes_type import PayrollCompanyTaxesType
from gusto_embedded_payroll_python_sdk.pydantic.payroll_employee_compensations_type import PayrollEmployeeCompensationsType
from gusto_embedded_payroll_python_sdk.pydantic.payroll_pay_period_type import PayrollPayPeriodType
from gusto_embedded_payroll_python_sdk.pydantic.payroll_payment_speed_changed_type import PayrollPaymentSpeedChangedType
from gusto_embedded_payroll_python_sdk.pydantic.payroll_payroll_status_meta_type import PayrollPayrollStatusMetaType
from gusto_embedded_payroll_python_sdk.pydantic.payroll_totals_type import PayrollTotalsType
from gusto_embedded_payroll_python_sdk.pydantic.payroll_withholding_pay_period_type import PayrollWithholdingPayPeriodType

class Payroll(BaseModel):
    # A timestamp that is the deadline for the payroll to be run in order for employees to be paid on time.
    payroll_deadline: typing.Optional[datetime] = Field(None, alias='payroll_deadline')

    # The date on which employees will be paid for the payroll.
    check_date: typing.Optional[str] = Field(None, alias='check_date')

    # Whether or not the payroll has been successfully processed. Note that processed payrolls cannot be updated. Additionally, a payroll is not guaranteed to be processed just because the payroll deadline has passed. Late payrolls are not uncommon. Conversely, users may choose to run payroll before the payroll deadline.
    processed: typing.Optional[bool] = Field(None, alias='processed')

    # The date at which the payroll was processed. Null if the payroll isn't processed yet.
    processed_date: typing.Optional[str] = Field(None, alias='processed_date')

    # A timestamp of the last valid payroll calculation. Null is there isn't a valid calculation.
    calculated_at: typing.Optional[str] = Field(None, alias='calculated_at')

    # The UUID of the payroll.
    payroll_uuid: typing.Optional[str] = Field(None, alias='payroll_uuid')

    # The UUID of the company for the payroll.
    company_uuid: typing.Optional[str] = Field(None, alias='company_uuid')

    # Indicates whether the payroll is an off-cycle payroll
    off_cycle: typing.Optional[bool] = Field(None, alias='off_cycle')

    off_cycle_reason: typing.Optional[OffCycleReasonType] = Field(None, alias='off_cycle_reason')

    # Indicates whether the payroll is an external payroll
    external: typing.Optional[bool] = Field(None, alias='external')

    # Indicates whether the payroll is the final payroll for a terminated employee. Only included for off-cycle payrolls.
    final_termination_payroll: typing.Optional[bool] = Field(None, alias='final_termination_payroll')

    withholding_pay_period: typing.Optional[PayrollWithholdingPayPeriodType] = Field(None, alias='withholding_pay_period')

    # Block regular deductions and contributions for this payroll.  Only included for off-cycle payrolls.
    skip_regular_deductions: typing.Optional[bool] = Field(None, alias='skip_regular_deductions')

    # Enable taxes to be withheld at the IRS's required rate of 22% for federal income taxes. State income taxes will be taxed at the state's supplemental tax rate. Otherwise, we'll sum the entirety of the employee's wages and withhold taxes on the entire amount at the rate for regular wages. Only included for off-cycle payrolls.
    fixed_withholding_rate: typing.Optional[bool] = Field(None, alias='fixed_withholding_rate')

    pay_period: typing.Optional[PayrollPayPeriodType] = Field(None, alias='pay_period')

    payroll_status_meta: typing.Optional[PayrollPayrollStatusMetaType] = Field(None, alias='payroll_status_meta')

    totals: typing.Optional[PayrollTotalsType] = Field(None, alias='totals')

    employee_compensations: typing.Optional[PayrollEmployeeCompensationsType] = Field(None, alias='employee_compensations')

    company_taxes: typing.Optional[PayrollCompanyTaxesType] = Field(None, alias='company_taxes')

    payment_speed_changed: typing.Optional[PayrollPaymentSpeedChangedType] = Field(None, alias='payment_speed_changed')

    # Datetime for when the resource was created.
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
