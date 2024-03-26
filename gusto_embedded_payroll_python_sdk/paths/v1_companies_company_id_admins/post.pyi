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

from gusto_embedded_payroll_python_sdk.model.admin import Admin as AdminSchema
from gusto_embedded_payroll_python_sdk.model.companies_create_admin_request import CompaniesCreateAdminRequest as CompaniesCreateAdminRequestSchema
from gusto_embedded_payroll_python_sdk.model.unprocessable_entity_error_object import UnprocessableEntityErrorObject as UnprocessableEntityErrorObjectSchema

from gusto_embedded_payroll_python_sdk.type.unprocessable_entity_error_object import UnprocessableEntityErrorObject
from gusto_embedded_payroll_python_sdk.type.admin import Admin
from gusto_embedded_payroll_python_sdk.type.companies_create_admin_request import CompaniesCreateAdminRequest

from ...api_client import Dictionary
from gusto_embedded_payroll_python_sdk.pydantic.companies_create_admin_request import CompaniesCreateAdminRequest as CompaniesCreateAdminRequestPydantic
from gusto_embedded_payroll_python_sdk.pydantic.unprocessable_entity_error_object import UnprocessableEntityErrorObject as UnprocessableEntityErrorObjectPydantic
from gusto_embedded_payroll_python_sdk.pydantic.admin import Admin as AdminPydantic

# Header params


class XGustoAPIVersionSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
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
# body param
SchemaForRequestBodyApplicationJson = CompaniesCreateAdminRequestSchema


request_body_companies_create_admin_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = AdminSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Admin


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Admin


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
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
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_admin_mapped_args(
        self,
        first_name: str,
        last_name: str,
        email: str,
        company_id: str,
        x_gusto_api_version: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if first_name is not None:
            _body["first_name"] = first_name
        if last_name is not None:
            _body["last_name"] = last_name
        if email is not None:
            _body["email"] = email
        args.body = _body
        if x_gusto_api_version is not None:
            _header_params["X-Gusto-API-Version"] = x_gusto_api_version
        if company_id is not None:
            _path_params["company_id"] = company_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _acreate_admin_oapg(
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
        Create an admin for the company
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
            path_template='/v1/companies/{company_id}/admins',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_companies_create_admin_request.serialize(body, content_type)
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


    def _create_admin_oapg(
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
        Create an admin for the company
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
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
            path_template='/v1/companies/{company_id}/admins',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_companies_create_admin_request.serialize(body, content_type)
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


class CreateAdminRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_admin(
        self,
        first_name: str,
        last_name: str,
        email: str,
        company_id: str,
        x_gusto_api_version: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_admin_mapped_args(
            first_name=first_name,
            last_name=last_name,
            email=email,
            company_id=company_id,
            x_gusto_api_version=x_gusto_api_version,
        )
        return await self._acreate_admin_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def create_admin(
        self,
        first_name: str,
        last_name: str,
        email: str,
        company_id: str,
        x_gusto_api_version: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_admin_mapped_args(
            first_name=first_name,
            last_name=last_name,
            email=email,
            company_id=company_id,
            x_gusto_api_version=x_gusto_api_version,
        )
        return self._create_admin_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class CreateAdmin(BaseApi):

    async def acreate_admin(
        self,
        first_name: str,
        last_name: str,
        email: str,
        company_id: str,
        x_gusto_api_version: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> AdminPydantic:
        raw_response = await self.raw.acreate_admin(
            first_name=first_name,
            last_name=last_name,
            email=email,
            company_id=company_id,
            x_gusto_api_version=x_gusto_api_version,
            **kwargs,
        )
        if validate:
            return AdminPydantic(**raw_response.body)
        return api_client.construct_model_instance(AdminPydantic, raw_response.body)
    
    
    def create_admin(
        self,
        first_name: str,
        last_name: str,
        email: str,
        company_id: str,
        x_gusto_api_version: typing.Optional[str] = None,
        validate: bool = False,
    ) -> AdminPydantic:
        raw_response = self.raw.create_admin(
            first_name=first_name,
            last_name=last_name,
            email=email,
            company_id=company_id,
            x_gusto_api_version=x_gusto_api_version,
        )
        if validate:
            return AdminPydantic(**raw_response.body)
        return api_client.construct_model_instance(AdminPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        first_name: str,
        last_name: str,
        email: str,
        company_id: str,
        x_gusto_api_version: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_admin_mapped_args(
            first_name=first_name,
            last_name=last_name,
            email=email,
            company_id=company_id,
            x_gusto_api_version=x_gusto_api_version,
        )
        return await self._acreate_admin_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        first_name: str,
        last_name: str,
        email: str,
        company_id: str,
        x_gusto_api_version: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_admin_mapped_args(
            first_name=first_name,
            last_name=last_name,
            email=email,
            company_id=company_id,
            x_gusto_api_version=x_gusto_api_version,
        )
        return self._create_admin_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

