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

from gusto_embedded_payroll_python_sdk.model.time_off_policies_calculate_accruing_time_off_hours_request import TimeOffPoliciesCalculateAccruingTimeOffHoursRequest as TimeOffPoliciesCalculateAccruingTimeOffHoursRequestSchema
from gusto_embedded_payroll_python_sdk.model.time_off_policies_calculate_accruing_time_off_hours_response import TimeOffPoliciesCalculateAccruingTimeOffHoursResponse as TimeOffPoliciesCalculateAccruingTimeOffHoursResponseSchema
from gusto_embedded_payroll_python_sdk.model.unprocessable_entity_error_object import UnprocessableEntityErrorObject as UnprocessableEntityErrorObjectSchema

from gusto_embedded_payroll_python_sdk.type.time_off_policies_calculate_accruing_time_off_hours_request import TimeOffPoliciesCalculateAccruingTimeOffHoursRequest
from gusto_embedded_payroll_python_sdk.type.time_off_policies_calculate_accruing_time_off_hours_response import TimeOffPoliciesCalculateAccruingTimeOffHoursResponse
from gusto_embedded_payroll_python_sdk.type.unprocessable_entity_error_object import UnprocessableEntityErrorObject

from ...api_client import Dictionary
from gusto_embedded_payroll_python_sdk.pydantic.time_off_policies_calculate_accruing_time_off_hours_response import TimeOffPoliciesCalculateAccruingTimeOffHoursResponse as TimeOffPoliciesCalculateAccruingTimeOffHoursResponsePydantic
from gusto_embedded_payroll_python_sdk.pydantic.time_off_policies_calculate_accruing_time_off_hours_request import TimeOffPoliciesCalculateAccruingTimeOffHoursRequest as TimeOffPoliciesCalculateAccruingTimeOffHoursRequestPydantic
from gusto_embedded_payroll_python_sdk.pydantic.unprocessable_entity_error_object import UnprocessableEntityErrorObject as UnprocessableEntityErrorObjectPydantic

from . import path

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
PayrollIdSchema = schemas.StrSchema
EmployeeIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'payroll_id': typing.Union[PayrollIdSchema, str, ],
        'employee_id': typing.Union[EmployeeIdSchema, str, ],
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


request_path_payroll_id = api_client.PathParameter(
    name="payroll_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PayrollIdSchema,
    required=True,
)
request_path_employee_id = api_client.PathParameter(
    name="employee_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=EmployeeIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = TimeOffPoliciesCalculateAccruingTimeOffHoursRequestSchema


request_body_time_off_policies_calculate_accruing_time_off_hours_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'Authorization',
]
SchemaFor200ResponseBodyApplicationJson = TimeOffPoliciesCalculateAccruingTimeOffHoursResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TimeOffPoliciesCalculateAccruingTimeOffHoursResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TimeOffPoliciesCalculateAccruingTimeOffHoursResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = UnprocessableEntityErrorObjectSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: UnprocessableEntityErrorObject


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: UnprocessableEntityErrorObject


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _calculate_accruing_time_off_hours_mapped_args(
        self,
        payroll_id: str,
        employee_id: str,
        regular_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        overtime_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        double_overtime_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        pto_hours_used: typing.Optional[typing.Union[int, float]] = None,
        sick_hours_used: typing.Optional[typing.Union[int, float]] = None,
        x_gusto_api_version: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if regular_hours_worked is not None:
            _body["regular_hours_worked"] = regular_hours_worked
        if overtime_hours_worked is not None:
            _body["overtime_hours_worked"] = overtime_hours_worked
        if double_overtime_hours_worked is not None:
            _body["double_overtime_hours_worked"] = double_overtime_hours_worked
        if pto_hours_used is not None:
            _body["pto_hours_used"] = pto_hours_used
        if sick_hours_used is not None:
            _body["sick_hours_used"] = sick_hours_used
        args.body = _body
        if x_gusto_api_version is not None:
            _header_params["X-Gusto-API-Version"] = x_gusto_api_version
        if payroll_id is not None:
            _path_params["payroll_id"] = payroll_id
        if employee_id is not None:
            _path_params["employee_id"] = employee_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _acalculate_accruing_time_off_hours_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Calculate accruing time off hours
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_payroll_id,
            request_path_employee_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/payrolls/{payroll_id}/employees/{employee_id}/calculate_accruing_time_off_hours',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_time_off_policies_calculate_accruing_time_off_hours_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _calculate_accruing_time_off_hours_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Calculate accruing time off hours
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_payroll_id,
            request_path_employee_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/payrolls/{payroll_id}/employees/{employee_id}/calculate_accruing_time_off_hours',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_time_off_policies_calculate_accruing_time_off_hours_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class CalculateAccruingTimeOffHoursRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acalculate_accruing_time_off_hours(
        self,
        payroll_id: str,
        employee_id: str,
        regular_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        overtime_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        double_overtime_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        pto_hours_used: typing.Optional[typing.Union[int, float]] = None,
        sick_hours_used: typing.Optional[typing.Union[int, float]] = None,
        x_gusto_api_version: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._calculate_accruing_time_off_hours_mapped_args(
            payroll_id=payroll_id,
            employee_id=employee_id,
            regular_hours_worked=regular_hours_worked,
            overtime_hours_worked=overtime_hours_worked,
            double_overtime_hours_worked=double_overtime_hours_worked,
            pto_hours_used=pto_hours_used,
            sick_hours_used=sick_hours_used,
            x_gusto_api_version=x_gusto_api_version,
        )
        return await self._acalculate_accruing_time_off_hours_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def calculate_accruing_time_off_hours(
        self,
        payroll_id: str,
        employee_id: str,
        regular_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        overtime_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        double_overtime_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        pto_hours_used: typing.Optional[typing.Union[int, float]] = None,
        sick_hours_used: typing.Optional[typing.Union[int, float]] = None,
        x_gusto_api_version: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._calculate_accruing_time_off_hours_mapped_args(
            payroll_id=payroll_id,
            employee_id=employee_id,
            regular_hours_worked=regular_hours_worked,
            overtime_hours_worked=overtime_hours_worked,
            double_overtime_hours_worked=double_overtime_hours_worked,
            pto_hours_used=pto_hours_used,
            sick_hours_used=sick_hours_used,
            x_gusto_api_version=x_gusto_api_version,
        )
        return self._calculate_accruing_time_off_hours_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class CalculateAccruingTimeOffHours(BaseApi):

    async def acalculate_accruing_time_off_hours(
        self,
        payroll_id: str,
        employee_id: str,
        regular_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        overtime_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        double_overtime_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        pto_hours_used: typing.Optional[typing.Union[int, float]] = None,
        sick_hours_used: typing.Optional[typing.Union[int, float]] = None,
        x_gusto_api_version: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> TimeOffPoliciesCalculateAccruingTimeOffHoursResponsePydantic:
        raw_response = await self.raw.acalculate_accruing_time_off_hours(
            payroll_id=payroll_id,
            employee_id=employee_id,
            regular_hours_worked=regular_hours_worked,
            overtime_hours_worked=overtime_hours_worked,
            double_overtime_hours_worked=double_overtime_hours_worked,
            pto_hours_used=pto_hours_used,
            sick_hours_used=sick_hours_used,
            x_gusto_api_version=x_gusto_api_version,
            **kwargs,
        )
        if validate:
            return RootModel[TimeOffPoliciesCalculateAccruingTimeOffHoursResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(TimeOffPoliciesCalculateAccruingTimeOffHoursResponsePydantic, raw_response.body)
    
    
    def calculate_accruing_time_off_hours(
        self,
        payroll_id: str,
        employee_id: str,
        regular_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        overtime_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        double_overtime_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        pto_hours_used: typing.Optional[typing.Union[int, float]] = None,
        sick_hours_used: typing.Optional[typing.Union[int, float]] = None,
        x_gusto_api_version: typing.Optional[str] = None,
        validate: bool = False,
    ) -> TimeOffPoliciesCalculateAccruingTimeOffHoursResponsePydantic:
        raw_response = self.raw.calculate_accruing_time_off_hours(
            payroll_id=payroll_id,
            employee_id=employee_id,
            regular_hours_worked=regular_hours_worked,
            overtime_hours_worked=overtime_hours_worked,
            double_overtime_hours_worked=double_overtime_hours_worked,
            pto_hours_used=pto_hours_used,
            sick_hours_used=sick_hours_used,
            x_gusto_api_version=x_gusto_api_version,
        )
        if validate:
            return RootModel[TimeOffPoliciesCalculateAccruingTimeOffHoursResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(TimeOffPoliciesCalculateAccruingTimeOffHoursResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        payroll_id: str,
        employee_id: str,
        regular_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        overtime_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        double_overtime_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        pto_hours_used: typing.Optional[typing.Union[int, float]] = None,
        sick_hours_used: typing.Optional[typing.Union[int, float]] = None,
        x_gusto_api_version: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._calculate_accruing_time_off_hours_mapped_args(
            payroll_id=payroll_id,
            employee_id=employee_id,
            regular_hours_worked=regular_hours_worked,
            overtime_hours_worked=overtime_hours_worked,
            double_overtime_hours_worked=double_overtime_hours_worked,
            pto_hours_used=pto_hours_used,
            sick_hours_used=sick_hours_used,
            x_gusto_api_version=x_gusto_api_version,
        )
        return await self._acalculate_accruing_time_off_hours_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        payroll_id: str,
        employee_id: str,
        regular_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        overtime_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        double_overtime_hours_worked: typing.Optional[typing.Union[int, float]] = None,
        pto_hours_used: typing.Optional[typing.Union[int, float]] = None,
        sick_hours_used: typing.Optional[typing.Union[int, float]] = None,
        x_gusto_api_version: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._calculate_accruing_time_off_hours_mapped_args(
            payroll_id=payroll_id,
            employee_id=employee_id,
            regular_hours_worked=regular_hours_worked,
            overtime_hours_worked=overtime_hours_worked,
            double_overtime_hours_worked=double_overtime_hours_worked,
            pto_hours_used=pto_hours_used,
            sick_hours_used=sick_hours_used,
            x_gusto_api_version=x_gusto_api_version,
        )
        return self._calculate_accruing_time_off_hours_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

