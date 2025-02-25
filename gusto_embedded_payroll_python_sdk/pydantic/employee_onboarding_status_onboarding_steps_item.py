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

from gusto_embedded_payroll_python_sdk.pydantic.employee_onboarding_status_onboarding_steps_item_requirements import EmployeeOnboardingStatusOnboardingStepsItemRequirements

class EmployeeOnboardingStatusOnboardingStepsItem(BaseModel):
    # User-friendly description of the onboarding step.
    title: typing.Optional[str] = Field(None, alias='title')

    # String identifier for the onboarding step.
    id: typing.Optional[str] = Field(None, alias='id')

    # When true, this step has been completed.
    required: typing.Optional[bool] = Field(None, alias='required')

    # When true, this step has been completed.
    completed: typing.Optional[bool] = Field(None, alias='completed')

    requirements: typing.Optional[EmployeeOnboardingStatusOnboardingStepsItemRequirements] = Field(None, alias='requirements')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
