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
from gusto_embedded_payroll_python_sdk.paths.oauth_token import post
from gusto_embedded_payroll_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestOauthToken(ApiTestMixin, unittest.TestCase):
    """
    OauthToken unit test stubs
        Refresh access token
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
