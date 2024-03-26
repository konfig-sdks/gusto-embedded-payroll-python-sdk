# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from gusto_embedded_payroll_python_sdk.paths.v1_events.get import Get30DayEvents
from gusto_embedded_payroll_python_sdk.apis.tags.events_api_raw import EventsApiRaw


class EventsApi(
    Get30DayEvents,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EventsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EventsApiRaw(api_client)
