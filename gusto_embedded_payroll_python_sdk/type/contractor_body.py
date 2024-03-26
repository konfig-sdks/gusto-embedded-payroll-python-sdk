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


class RequiredContractorBody(TypedDict):
    pass

class OptionalContractorBody(TypedDict, total=False):
    # The contractor type.
    type: str

    # The contractor’s wage type. 
    wage_type: str

    # The day when the contractor will start working for the company. 
    start_date: str

    # The contractor’s hourly rate. This attribute is required if the wage_type is `Hourly`.
    hourly_rate: str

    # Whether the contractor or the payroll admin will complete onboarding in Gusto. Self-onboarding is recommended so that contractors receive Gusto accounts. If self_onboarding is true, then email is required.
    self_onboarding: bool

    # The contractor’s email address.
    email: str

    # The contractor’s first name. This attribute is required for `Individual` contractors and will be ignored for `Business` contractors.
    first_name: str

    # The contractor’s last name. This attribute is required for `Individual` contractors and will be ignored for `Business` contractors.
    last_name: str

    # The contractor’s middle initial. This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors.
    middle_initial: str

    # The boolean flag indicating whether Gusto will file a new hire report for the contractor. This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors.
    file_new_hire_report: bool

    # State where the contractor will be conducting the majority of their work for the company. This value is used when generating the new hire report. This attribute is required for `Individual` contractors if `file_new_hire_report` is true and will be ignored for `Business` contractors.
    work_state: typing.Optional[str]

    # This attribute is optional for `Individual` contractors and will be ignored for `Business` contractors. Social security number is needed to file the annual 1099 tax form.
    ssn: str

    # The name of the contractor business. This attribute is required for `Business` contractors and will be ignored for `Individual` contractors.
    business_name: str

    # The employer identification number of the contractor business. This attribute is optional for `Business` contractors and will be ignored for `Individual` contractors.
    ein: str

    # The status of the contractor.
    is_active: bool

class ContractorBody(RequiredContractorBody, OptionalContractorBody):
    pass
