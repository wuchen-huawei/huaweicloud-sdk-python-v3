# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class OmsAsyncClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(OmsAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkoms.v2.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "OmsClient":
            raise TypeError("client type error, support client type is OmsClient")

        return ClientBuilder(clazz)

    def create_sync_events_async(self, request):
        """创建同步事件

        源端有对象需要进行同步时，调用该接口创建一个同步事件，系统将根据同步事件中包含的对象名称进行同步

        :param CreateSyncEventsRequest request
        :return: CreateSyncEventsResponse
        """
        return self.create_sync_events_with_http_info(request)

    def create_sync_events_with_http_info(self, request):
        """创建同步事件

        源端有对象需要进行同步时，调用该接口创建一个同步事件，系统将根据同步事件中包含的对象名称进行同步

        :param CreateSyncEventsRequest request
        :return: CreateSyncEventsResponse
        """

        all_params = ['sync_task_id', 'create_sync_events_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'sync_task_id' in local_var_params:
            path_params['sync_task_id'] = local_var_params['sync_task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/sync-tasks/{sync_task_id}/events',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSyncEventsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_task_async(self, request):
        """创建迁移任务

        创建迁移任务，创建成功后，任务会被自动启动，不需要额外调用启动任务命令。

        :param CreateTaskRequest request
        :return: CreateTaskResponse
        """
        return self.create_task_with_http_info(request)

    def create_task_with_http_info(self, request):
        """创建迁移任务

        创建迁移任务，创建成功后，任务会被自动启动，不需要额外调用启动任务命令。

        :param CreateTaskRequest request
        :return: CreateTaskResponse
        """

        all_params = ['create_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/tasks',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_task_async(self, request):
        """删除迁移任务

        调用该接口删除迁移任务。 正在运行的任务不允许删除，如果删除会返回失败；若要删除，请先行暂停任务。

        :param DeleteTaskRequest request
        :return: DeleteTaskResponse
        """
        return self.delete_task_with_http_info(request)

    def delete_task_with_http_info(self, request):
        """删除迁移任务

        调用该接口删除迁移任务。 正在运行的任务不允许删除，如果删除会返回失败；若要删除，请先行暂停任务。

        :param DeleteTaskRequest request
        :return: DeleteTaskResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_tasks_async(self, request):
        """查询迁移任务列表

        查询用户账户下的所有任务信息。

        :param ListTasksRequest request
        :return: ListTasksResponse
        """
        return self.list_tasks_with_http_info(request)

    def list_tasks_with_http_info(self, request):
        """查询迁移任务列表

        查询用户账户下的所有任务信息。

        :param ListTasksRequest request
        :return: ListTasksResponse
        """

        all_params = ['group_id', 'limit', 'offset', 'status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/tasks',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTasksResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_task_async(self, request):
        """查询指定ID的任务详情

        查询指定ID的任务详情。

        :param ShowTaskRequest request
        :return: ShowTaskResponse
        """
        return self.show_task_with_http_info(request)

    def show_task_with_http_info(self, request):
        """查询指定ID的任务详情

        查询指定ID的任务详情。

        :param ShowTaskRequest request
        :return: ShowTaskResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_task_async(self, request):
        """启动迁移任务

        迁移任务暂停或失败后，调用该接口以启动任务。

        :param StartTaskRequest request
        :return: StartTaskResponse
        """
        return self.start_task_with_http_info(request)

    def start_task_with_http_info(self, request):
        """启动迁移任务

        迁移任务暂停或失败后，调用该接口以启动任务。

        :param StartTaskRequest request
        :return: StartTaskResponse
        """

        all_params = ['task_id', 'start_task_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_task_async(self, request):
        """暂停迁移任务

        当迁移任务处于迁移中时，调用该接口停止任务。

        :param StopTaskRequest request
        :return: StopTaskResponse
        """
        return self.stop_task_with_http_info(request)

    def stop_task_with_http_info(self, request):
        """暂停迁移任务

        当迁移任务处于迁移中时，调用该接口停止任务。

        :param StopTaskRequest request
        :return: StopTaskResponse
        """

        all_params = ['task_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopTaskResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_bandwidth_policy_async(self, request):
        """更新任务带宽策略

        当迁移任务未执行完成时，修改迁移任务的流量控制策略。

        :param UpdateBandwidthPolicyRequest request
        :return: UpdateBandwidthPolicyResponse
        """
        return self.update_bandwidth_policy_with_http_info(request)

    def update_bandwidth_policy_with_http_info(self, request):
        """更新任务带宽策略

        当迁移任务未执行完成时，修改迁移任务的流量控制策略。

        :param UpdateBandwidthPolicyRequest request
        :return: UpdateBandwidthPolicyResponse
        """

        all_params = ['task_id', 'update_bandwidth_policy_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'task_id' in local_var_params:
            path_params['task_id'] = local_var_params['task_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json;charset=UTF-8'])

        auth_settings = []

        return self.call_api(
            resource_path='/v2/{project_id}/tasks/{task_id}/bandwidth-policy',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateBandwidthPolicyResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_api_versions_async(self, request):
        """查询API版本信息列表

        查询对象存储迁移服务的API版本信息。

        :param ListApiVersionsRequest request
        :return: ListApiVersionsResponse
        """
        return self.list_api_versions_with_http_info(request)

    def list_api_versions_with_http_info(self, request):
        """查询API版本信息列表

        查询对象存储迁移服务的API版本信息。

        :param ListApiVersionsRequest request
        :return: ListApiVersionsResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListApiVersionsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_api_info_async(self, request):
        """查询指定API版本信息

        查询对象存储迁移服务指定API版本信息。

        :param ShowApiInfoRequest request
        :return: ShowApiInfoResponse
        """
        return self.show_api_info_with_http_info(request)

    def show_api_info_with_http_info(self, request):
        """查询指定API版本信息

        查询对象存储迁移服务指定API版本信息。

        :param ShowApiInfoRequest request
        :return: ShowApiInfoResponse
        """

        all_params = ['version']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'version' in local_var_params:
            path_params['version'] = local_var_params['version']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/{version}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowApiInfoResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: Response data type.
        :param response_headers: Header should be added to response data.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param request_type: Request data type.
        :return:
            Return the response directly.
        """
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type,
	    async_request=True)
