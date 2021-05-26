# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateBatchTaskResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'task_name': 'str',
        'task_type': 'str',
        'targets': 'list[str]',
        'targets_filter': 'dict(str, object)',
        'document': 'object',
        'task_policy': 'TaskPolicy',
        'status': 'str',
        'status_desc': 'str',
        'task_progress': 'TaskProgress',
        'create_time': 'str'
    }

    attribute_map = {
        'task_id': 'task_id',
        'task_name': 'task_name',
        'task_type': 'task_type',
        'targets': 'targets',
        'targets_filter': 'targets_filter',
        'document': 'document',
        'task_policy': 'task_policy',
        'status': 'status',
        'status_desc': 'status_desc',
        'task_progress': 'task_progress',
        'create_time': 'create_time'
    }

    def __init__(self, task_id=None, task_name=None, task_type=None, targets=None, targets_filter=None, document=None, task_policy=None, status=None, status_desc=None, task_progress=None, create_time=None):
        """CreateBatchTaskResponse - a model defined in huaweicloud sdk"""
        
        super(CreateBatchTaskResponse, self).__init__()

        self._task_id = None
        self._task_name = None
        self._task_type = None
        self._targets = None
        self._targets_filter = None
        self._document = None
        self._task_policy = None
        self._status = None
        self._status_desc = None
        self._task_progress = None
        self._create_time = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if task_name is not None:
            self.task_name = task_name
        if task_type is not None:
            self.task_type = task_type
        if targets is not None:
            self.targets = targets
        if targets_filter is not None:
            self.targets_filter = targets_filter
        if document is not None:
            self.document = document
        if task_policy is not None:
            self.task_policy = task_policy
        if status is not None:
            self.status = status
        if status_desc is not None:
            self.status_desc = status_desc
        if task_progress is not None:
            self.task_progress = task_progress
        if create_time is not None:
            self.create_time = create_time

    @property
    def task_id(self):
        """Gets the task_id of this CreateBatchTaskResponse.

        批量任务ID，创建批量任务时由物联网平台分配获得。

        :return: The task_id of this CreateBatchTaskResponse.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this CreateBatchTaskResponse.

        批量任务ID，创建批量任务时由物联网平台分配获得。

        :param task_id: The task_id of this CreateBatchTaskResponse.
        :type: str
        """
        self._task_id = task_id

    @property
    def task_name(self):
        """Gets the task_name of this CreateBatchTaskResponse.

        批量任务名称。

        :return: The task_name of this CreateBatchTaskResponse.
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this CreateBatchTaskResponse.

        批量任务名称。

        :param task_name: The task_name of this CreateBatchTaskResponse.
        :type: str
        """
        self._task_name = task_name

    @property
    def task_type(self):
        """Gets the task_type of this CreateBatchTaskResponse.

        批量任务类型，取值范围：firmwareUpgrade，softwareUpgrade，createDevices，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands。 - softwareUpgrade: 软件升级任务 - firmwareUpgrade: 固件升级任务 - createDevices: 批量创建设备任务 - deleteDevices: 批量删除设备任务 - freezeDevices: 批量冻结设备任务 - unfreezeDevices: 批量解冻设备任务 - createCommands: 批量创建同步命令任务 - createAsyncCommands: 批量创建异步命令任务 

        :return: The task_type of this CreateBatchTaskResponse.
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this CreateBatchTaskResponse.

        批量任务类型，取值范围：firmwareUpgrade，softwareUpgrade，createDevices，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands。 - softwareUpgrade: 软件升级任务 - firmwareUpgrade: 固件升级任务 - createDevices: 批量创建设备任务 - deleteDevices: 批量删除设备任务 - freezeDevices: 批量冻结设备任务 - unfreezeDevices: 批量解冻设备任务 - createCommands: 批量创建同步命令任务 - createAsyncCommands: 批量创建异步命令任务 

        :param task_type: The task_type of this CreateBatchTaskResponse.
        :type: str
        """
        self._task_type = task_type

    @property
    def targets(self):
        """Gets the targets of this CreateBatchTaskResponse.

        执行批量任务的目标，当task_type为firmwareUpgrade，softwareUpgrade，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，此处填写device_id列表。

        :return: The targets of this CreateBatchTaskResponse.
        :rtype: list[str]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this CreateBatchTaskResponse.

        执行批量任务的目标，当task_type为firmwareUpgrade，softwareUpgrade，deleteDevices，freezeDevices，unfreezeDevices，createCommands，createAsyncCommands，此处填写device_id列表。

        :param targets: The targets of this CreateBatchTaskResponse.
        :type: list[str]
        """
        self._targets = targets

    @property
    def targets_filter(self):
        """Gets the targets_filter of this CreateBatchTaskResponse.

        任务目标筛选参数。Json格式，里面是一个个键值对，（K,V）格式标识筛选targets需要的参数，目前支持的K有group_ids（V填写group_id数组，eg:[\"e495cf17-ff79-4294-8f64-4d367919d665\"]，任务则会筛选出来符合该群组条件的设备作为目标）

        :return: The targets_filter of this CreateBatchTaskResponse.
        :rtype: dict(str, object)
        """
        return self._targets_filter

    @targets_filter.setter
    def targets_filter(self, targets_filter):
        """Sets the targets_filter of this CreateBatchTaskResponse.

        任务目标筛选参数。Json格式，里面是一个个键值对，（K,V）格式标识筛选targets需要的参数，目前支持的K有group_ids（V填写group_id数组，eg:[\"e495cf17-ff79-4294-8f64-4d367919d665\"]，任务则会筛选出来符合该群组条件的设备作为目标）

        :param targets_filter: The targets_filter of this CreateBatchTaskResponse.
        :type: dict(str, object)
        """
        self._targets_filter = targets_filter

    @property
    def document(self):
        """Gets the document of this CreateBatchTaskResponse.

        执行任务数据文档，Json格式。(当task_type为softwareUpgrade|firmwareUpgrade，也就是软固件升级任务时，Json里面是(K,V)键值对，需要填写key为package_id，value为在平台上传的软固件附件id，id由portal软件库包管理上传并查询获得。当task_type为createCommands，也就是批量创建同步命令任务时，Json里面是命令相关参数，eg：“{\"service_id\":\"water\",\"command_name\":\"ON_OFF\",\"paras\":{\"value\":\"ON\"}}”,参考[设备同步命令](https://support.huaweicloud.com/api-iothub/iot_06_v5_0038.html))。当task_type为createAsyncCommands，也就是批量创建异步命令任务时，Json里面是命令相关参数，eg：“{\"service_id\":\"water\",\"command_name\":\"ON_OFF\",\"paras\":{\"value\":\"ON\"},\"expire_time\":0,\"send_strategy\":\"immediately\"}”,参考[设备异步命令](https://support.huaweicloud.com/api-iothub/iot_06_v5_0040.html))。

        :return: The document of this CreateBatchTaskResponse.
        :rtype: object
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this CreateBatchTaskResponse.

        执行任务数据文档，Json格式。(当task_type为softwareUpgrade|firmwareUpgrade，也就是软固件升级任务时，Json里面是(K,V)键值对，需要填写key为package_id，value为在平台上传的软固件附件id，id由portal软件库包管理上传并查询获得。当task_type为createCommands，也就是批量创建同步命令任务时，Json里面是命令相关参数，eg：“{\"service_id\":\"water\",\"command_name\":\"ON_OFF\",\"paras\":{\"value\":\"ON\"}}”,参考[设备同步命令](https://support.huaweicloud.com/api-iothub/iot_06_v5_0038.html))。当task_type为createAsyncCommands，也就是批量创建异步命令任务时，Json里面是命令相关参数，eg：“{\"service_id\":\"water\",\"command_name\":\"ON_OFF\",\"paras\":{\"value\":\"ON\"},\"expire_time\":0,\"send_strategy\":\"immediately\"}”,参考[设备异步命令](https://support.huaweicloud.com/api-iothub/iot_06_v5_0040.html))。

        :param document: The document of this CreateBatchTaskResponse.
        :type: object
        """
        self._document = document

    @property
    def task_policy(self):
        """Gets the task_policy of this CreateBatchTaskResponse.


        :return: The task_policy of this CreateBatchTaskResponse.
        :rtype: TaskPolicy
        """
        return self._task_policy

    @task_policy.setter
    def task_policy(self, task_policy):
        """Sets the task_policy of this CreateBatchTaskResponse.


        :param task_policy: The task_policy of this CreateBatchTaskResponse.
        :type: TaskPolicy
        """
        self._task_policy = task_policy

    @property
    def status(self):
        """Gets the status of this CreateBatchTaskResponse.

        批量任务的状态，可选参数，取值范围：Success|Fail|Processing|PartialSuccess|Stopped|Waitting|Initializing。 - Initializing: 初始化中。 - Waitting: 等待中。 - Processing: 执行中。 - Success: 成功。 - Fail: 失败。 - PartialSuccess: 部分成功。 - Stopped: 停止。 

        :return: The status of this CreateBatchTaskResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateBatchTaskResponse.

        批量任务的状态，可选参数，取值范围：Success|Fail|Processing|PartialSuccess|Stopped|Waitting|Initializing。 - Initializing: 初始化中。 - Waitting: 等待中。 - Processing: 执行中。 - Success: 成功。 - Fail: 失败。 - PartialSuccess: 部分成功。 - Stopped: 停止。 

        :param status: The status of this CreateBatchTaskResponse.
        :type: str
        """
        self._status = status

    @property
    def status_desc(self):
        """Gets the status_desc of this CreateBatchTaskResponse.

        批量任务状态描述(包含主任务失败错误信息)

        :return: The status_desc of this CreateBatchTaskResponse.
        :rtype: str
        """
        return self._status_desc

    @status_desc.setter
    def status_desc(self, status_desc):
        """Sets the status_desc of this CreateBatchTaskResponse.

        批量任务状态描述(包含主任务失败错误信息)

        :param status_desc: The status_desc of this CreateBatchTaskResponse.
        :type: str
        """
        self._status_desc = status_desc

    @property
    def task_progress(self):
        """Gets the task_progress of this CreateBatchTaskResponse.


        :return: The task_progress of this CreateBatchTaskResponse.
        :rtype: TaskProgress
        """
        return self._task_progress

    @task_progress.setter
    def task_progress(self, task_progress):
        """Sets the task_progress of this CreateBatchTaskResponse.


        :param task_progress: The task_progress of this CreateBatchTaskResponse.
        :type: TaskProgress
        """
        self._task_progress = task_progress

    @property
    def create_time(self):
        """Gets the create_time of this CreateBatchTaskResponse.

        批量任务的创建时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The create_time of this CreateBatchTaskResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateBatchTaskResponse.

        批量任务的创建时间。格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param create_time: The create_time of this CreateBatchTaskResponse.
        :type: str
        """
        self._create_time = create_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateBatchTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
