# coding: utf-8

"""
    Gusto API

    Welcome to Gusto's Embedded Payroll API documentation!

    The version of the OpenAPI document: 2024-03-01
    Contact: developer@gusto.com
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from gusto_embedded_payroll_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from gusto_embedded_payroll_python_sdk.api_response import AsyncGeneratorResponse
from gusto_embedded_payroll_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from gusto_embedded_payroll_python_sdk import schemas  # noqa: F401

from gusto_embedded_payroll_python_sdk.model.pay_schedules_preview_pay_schedule_dates_response import PaySchedulesPreviewPayScheduleDatesResponse as PaySchedulesPreviewPayScheduleDatesResponseSchema

from gusto_embedded_payroll_python_sdk.type.pay_schedules_preview_pay_schedule_dates_response import PaySchedulesPreviewPayScheduleDatesResponse

from ...api_client import Dictionary
from gusto_embedded_payroll_python_sdk.pydantic.pay_schedules_preview_pay_schedule_dates_response import PaySchedulesPreviewPayScheduleDatesResponse as PaySchedulesPreviewPayScheduleDatesResponsePydantic

from . import path

# Query params


class FrequencySchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "Every week": "EVERY_WEEK",
            "Every other week": "EVERY_OTHER_WEEK",
            "Twice per month": "TWICE_PER_MONTH",
            "Monthly": "MONTHLY",
        }
    
    @schemas.classproperty
    def EVERY_WEEK(cls):
        return cls("Every week")
    
    @schemas.classproperty
    def EVERY_OTHER_WEEK(cls):
        return cls("Every other week")
    
    @schemas.classproperty
    def TWICE_PER_MONTH(cls):
        return cls("Twice per month")
    
    @schemas.classproperty
    def MONTHLY(cls):
        return cls("Monthly")
AnchorPayDateSchema = schemas.StrSchema
AnchorEndOfPayPeriodSchema = schemas.StrSchema
Day1Schema = schemas.IntSchema
Day2Schema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'frequency': typing.Union[FrequencySchema, str, ],
        'anchor_pay_date': typing.Union[AnchorPayDateSchema, str, ],
        'anchor_end_of_pay_period': typing.Union[AnchorEndOfPayPeriodSchema, str, ],
        'day_1': typing.Union[Day1Schema, decimal.Decimal, int, ],
        'day_2': typing.Union[Day2Schema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_frequency = api_client.QueryParameter(
    name="frequency",
    style=api_client.ParameterStyle.FORM,
    schema=FrequencySchema,
    explode=True,
)
request_query_anchor_pay_date = api_client.QueryParameter(
    name="anchor_pay_date",
    style=api_client.ParameterStyle.FORM,
    schema=AnchorPayDateSchema,
    explode=True,
)
request_query_anchor_end_of_pay_period = api_client.QueryParameter(
    name="anchor_end_of_pay_period",
    style=api_client.ParameterStyle.FORM,
    schema=AnchorEndOfPayPeriodSchema,
    explode=True,
)
request_query_day_1 = api_client.QueryParameter(
    name="day_1",
    style=api_client.ParameterStyle.FORM,
    schema=Day1Schema,
    explode=True,
)
request_query_day_2 = api_client.QueryParameter(
    name="day_2",
    style=api_client.ParameterStyle.FORM,
    schema=Day2Schema,
    explode=True,
)
# Header params


class XGustoAPIVersionSchema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg:
        enum_value_to_name = {
            "2024-03-01": "_20240301",
        }
    
    @schemas.classproperty
    def _20240301(cls):
        return cls("2024-03-01")
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'X-Gusto-API-Version': typing.Union[XGustoAPIVersionSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_x_gusto_api_version = api_client.HeaderParameter(
    name="X-Gusto-API-Version",
    style=api_client.ParameterStyle.SIMPLE,
    schema=XGustoAPIVersionSchema,
)
# Path params
CompanyIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'company_id': typing.Union[CompanyIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_company_id = api_client.PathParameter(
    name="company_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CompanyIdSchema,
    required=True,
)
_auth = [
    'Authorization',
]
SchemaFor200ResponseBodyApplicationJson = PaySchedulesPreviewPayScheduleDatesResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PaySchedulesPreviewPayScheduleDatesResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PaySchedulesPreviewPayScheduleDatesResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _preview_pay_schedule_dates_mapped_args(
        self,
        company_id: str,
        frequency: typing.Optional[str] = None,
        anchor_pay_date: typing.Optional[str] = None,
        anchor_end_of_pay_period: typing.Optional[str] = None,
        day_1: typing.Optional[int] = None,
        day_2: typing.Optional[int] = None,
        x_gusto_api_version: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _header_params = {}
        _path_params = {}
        if frequency is not None:
            _query_params["frequency"] = frequency
        if anchor_pay_date is not None:
            _query_params["anchor_pay_date"] = anchor_pay_date
        if anchor_end_of_pay_period is not None:
            _query_params["anchor_end_of_pay_period"] = anchor_end_of_pay_period
        if day_1 is not None:
            _query_params["day_1"] = day_1
        if day_2 is not None:
            _query_params["day_2"] = day_2
        if x_gusto_api_version is not None:
            _header_params["X-Gusto-API-Version"] = x_gusto_api_version
        if company_id is not None:
            _path_params["company_id"] = company_id
        args.query = _query_params
        args.header = _header_params
        args.path = _path_params
        return args

    async def _apreview_pay_schedule_dates_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Preview pay schedule dates
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_frequency,
            request_query_anchor_pay_date,
            request_query_anchor_end_of_pay_period,
            request_query_day_1,
            request_query_day_2,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_gusto_api_version,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/companies/{company_id}/pay_schedules/preview',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _preview_pay_schedule_dates_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Preview pay schedule dates
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_company_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_frequency,
            request_query_anchor_pay_date,
            request_query_anchor_end_of_pay_period,
            request_query_day_1,
            request_query_day_2,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_x_gusto_api_version,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/companies/{company_id}/pay_schedules/preview',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class PreviewPayScheduleDatesRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def apreview_pay_schedule_dates(
        self,
        company_id: str,
        frequency: typing.Optional[str] = None,
        anchor_pay_date: typing.Optional[str] = None,
        anchor_end_of_pay_period: typing.Optional[str] = None,
        day_1: typing.Optional[int] = None,
        day_2: typing.Optional[int] = None,
        x_gusto_api_version: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._preview_pay_schedule_dates_mapped_args(
            company_id=company_id,
            frequency=frequency,
            anchor_pay_date=anchor_pay_date,
            anchor_end_of_pay_period=anchor_end_of_pay_period,
            day_1=day_1,
            day_2=day_2,
            x_gusto_api_version=x_gusto_api_version,
        )
        return await self._apreview_pay_schedule_dates_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def preview_pay_schedule_dates(
        self,
        company_id: str,
        frequency: typing.Optional[str] = None,
        anchor_pay_date: typing.Optional[str] = None,
        anchor_end_of_pay_period: typing.Optional[str] = None,
        day_1: typing.Optional[int] = None,
        day_2: typing.Optional[int] = None,
        x_gusto_api_version: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._preview_pay_schedule_dates_mapped_args(
            company_id=company_id,
            frequency=frequency,
            anchor_pay_date=anchor_pay_date,
            anchor_end_of_pay_period=anchor_end_of_pay_period,
            day_1=day_1,
            day_2=day_2,
            x_gusto_api_version=x_gusto_api_version,
        )
        return self._preview_pay_schedule_dates_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

class PreviewPayScheduleDates(BaseApi):

    async def apreview_pay_schedule_dates(
        self,
        company_id: str,
        frequency: typing.Optional[str] = None,
        anchor_pay_date: typing.Optional[str] = None,
        anchor_end_of_pay_period: typing.Optional[str] = None,
        day_1: typing.Optional[int] = None,
        day_2: typing.Optional[int] = None,
        x_gusto_api_version: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PaySchedulesPreviewPayScheduleDatesResponsePydantic:
        raw_response = await self.raw.apreview_pay_schedule_dates(
            company_id=company_id,
            frequency=frequency,
            anchor_pay_date=anchor_pay_date,
            anchor_end_of_pay_period=anchor_end_of_pay_period,
            day_1=day_1,
            day_2=day_2,
            x_gusto_api_version=x_gusto_api_version,
            **kwargs,
        )
        if validate:
            return PaySchedulesPreviewPayScheduleDatesResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PaySchedulesPreviewPayScheduleDatesResponsePydantic, raw_response.body)
    
    
    def preview_pay_schedule_dates(
        self,
        company_id: str,
        frequency: typing.Optional[str] = None,
        anchor_pay_date: typing.Optional[str] = None,
        anchor_end_of_pay_period: typing.Optional[str] = None,
        day_1: typing.Optional[int] = None,
        day_2: typing.Optional[int] = None,
        x_gusto_api_version: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PaySchedulesPreviewPayScheduleDatesResponsePydantic:
        raw_response = self.raw.preview_pay_schedule_dates(
            company_id=company_id,
            frequency=frequency,
            anchor_pay_date=anchor_pay_date,
            anchor_end_of_pay_period=anchor_end_of_pay_period,
            day_1=day_1,
            day_2=day_2,
            x_gusto_api_version=x_gusto_api_version,
        )
        if validate:
            return PaySchedulesPreviewPayScheduleDatesResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PaySchedulesPreviewPayScheduleDatesResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        company_id: str,
        frequency: typing.Optional[str] = None,
        anchor_pay_date: typing.Optional[str] = None,
        anchor_end_of_pay_period: typing.Optional[str] = None,
        day_1: typing.Optional[int] = None,
        day_2: typing.Optional[int] = None,
        x_gusto_api_version: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._preview_pay_schedule_dates_mapped_args(
            company_id=company_id,
            frequency=frequency,
            anchor_pay_date=anchor_pay_date,
            anchor_end_of_pay_period=anchor_end_of_pay_period,
            day_1=day_1,
            day_2=day_2,
            x_gusto_api_version=x_gusto_api_version,
        )
        return await self._apreview_pay_schedule_dates_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        company_id: str,
        frequency: typing.Optional[str] = None,
        anchor_pay_date: typing.Optional[str] = None,
        anchor_end_of_pay_period: typing.Optional[str] = None,
        day_1: typing.Optional[int] = None,
        day_2: typing.Optional[int] = None,
        x_gusto_api_version: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._preview_pay_schedule_dates_mapped_args(
            company_id=company_id,
            frequency=frequency,
            anchor_pay_date=anchor_pay_date,
            anchor_end_of_pay_period=anchor_end_of_pay_period,
            day_1=day_1,
            day_2=day_2,
            x_gusto_api_version=x_gusto_api_version,
        )
        return self._preview_pay_schedule_dates_oapg(
            query_params=args.query,
            header_params=args.header,
            path_params=args.path,
        )

