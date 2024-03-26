# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_embedded_payroll_python_sdk.paths.v1_generated_documents_document_type_request_uuid.get import GetDocumentByRequestUuid
from gusto_embedded_payroll_python_sdk.apis.tags.generated_documents_api_raw import GeneratedDocumentsApiRaw


class GeneratedDocumentsApi(
    GetDocumentByRequestUuid,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: GeneratedDocumentsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = GeneratedDocumentsApiRaw(api_client)
