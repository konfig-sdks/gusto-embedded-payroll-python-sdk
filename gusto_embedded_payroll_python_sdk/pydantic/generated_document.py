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

from gusto_embedded_payroll_python_sdk.pydantic.generated_document_document_urls import GeneratedDocumentDocumentUrls

class GeneratedDocument(BaseModel):
    # A unique identifier of the Generated Document request
    request_uuid: typing.Optional[str] = Field(None, alias='request_uuid')

    # Current status of the Generated Document
    status: typing.Optional[str] = Field(None, alias='status')

    document_urls: typing.Optional[GeneratedDocumentDocumentUrls] = Field(None, alias='document_urls')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
