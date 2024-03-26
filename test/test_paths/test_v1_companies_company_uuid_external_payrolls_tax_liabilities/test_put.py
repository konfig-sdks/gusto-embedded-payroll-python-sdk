# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import gusto_embedded_payroll_python_sdk
from gusto_embedded_payroll_python_sdk.paths.v1_companies_company_uuid_external_payrolls_tax_liabilities import put
from gusto_embedded_payroll_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1CompaniesCompanyUuidExternalPayrollsTaxLiabilities(ApiTestMixin, unittest.TestCase):
    """
    V1CompaniesCompanyUuidExternalPayrollsTaxLiabilities unit test stubs
        Update tax liabilities
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
