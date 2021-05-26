# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowJobInfosResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'entities': 'Entities',
        'job_id': 'str',
        'job_type': 'str',
        'begin_time': 'datetime',
        'end_time': 'datetime',
        'error_code': 'str',
        'fail_reason': 'str',
        'message': 'str',
        'code': 'str'
    }

    attribute_map = {
        'status': 'status',
        'entities': 'entities',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'error_code': 'error_code',
        'fail_reason': 'fail_reason',
        'message': 'message',
        'code': 'code'
    }

    def __init__(self, status=None, entities=None, job_id=None, job_type=None, begin_time=None, end_time=None, error_code=None, fail_reason=None, message=None, code=None):
        """ShowJobInfosResponse - a model defined in huaweicloud sdk"""
        
        super(ShowJobInfosResponse, self).__init__()

        self._status = None
        self._entities = None
        self._job_id = None
        self._job_type = None
        self._begin_time = None
        self._end_time = None
        self._error_code = None
        self._fail_reason = None
        self._message = None
        self._code = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if entities is not None:
            self.entities = entities
        if job_id is not None:
            self.job_id = job_id
        if job_type is not None:
            self.job_type = job_type
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if error_code is not None:
            self.error_code = error_code
        if fail_reason is not None:
            self.fail_reason = fail_reason
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    @property
    def status(self):
        """Gets the status of this ShowJobInfosResponse.

        Job的状态。SUCCESS：成功RUNNING：运行中FAIL：失败INIT：正在初始化

        :return: The status of this ShowJobInfosResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowJobInfosResponse.

        Job的状态。SUCCESS：成功RUNNING：运行中FAIL：失败INIT：正在初始化

        :param status: The status of this ShowJobInfosResponse.
        :type: str
        """
        self._status = status

    @property
    def entities(self):
        """Gets the entities of this ShowJobInfosResponse.


        :return: The entities of this ShowJobInfosResponse.
        :rtype: Entities
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this ShowJobInfosResponse.


        :param entities: The entities of this ShowJobInfosResponse.
        :type: Entities
        """
        self._entities = entities

    @property
    def job_id(self):
        """Gets the job_id of this ShowJobInfosResponse.

        Job ID

        :return: The job_id of this ShowJobInfosResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowJobInfosResponse.

        Job ID

        :param job_id: The job_id of this ShowJobInfosResponse.
        :type: str
        """
        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this ShowJobInfosResponse.

        Job的类型，包含以下类型：baremetalBatchCreate：批量创建裸金属服务器baremetalBatchOperate：批量修改裸金属服务器电源状态baremetalBatchCreate：批量创建裸金属服务器baremetalChangeOsVolumeBoot：切换快速发放裸金属服务器操作系统baremetalChangeOsLocalDisk：切换本地盘裸金属服务器操作系统baremetalVolumeBootReinstallOs：重装快速发放裸金属服务器操作系统baremetalReinstallOs：重装本地盘裸金属服务器操作系统baremetalAttachVolume：挂载单个磁盘baremetalDetachVolume：卸载单个磁盘baremetalBatchAttachVolume：裸金属服务器批量挂载共享磁盘

        :return: The job_type of this ShowJobInfosResponse.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this ShowJobInfosResponse.

        Job的类型，包含以下类型：baremetalBatchCreate：批量创建裸金属服务器baremetalBatchOperate：批量修改裸金属服务器电源状态baremetalBatchCreate：批量创建裸金属服务器baremetalChangeOsVolumeBoot：切换快速发放裸金属服务器操作系统baremetalChangeOsLocalDisk：切换本地盘裸金属服务器操作系统baremetalVolumeBootReinstallOs：重装快速发放裸金属服务器操作系统baremetalReinstallOs：重装本地盘裸金属服务器操作系统baremetalAttachVolume：挂载单个磁盘baremetalDetachVolume：卸载单个磁盘baremetalBatchAttachVolume：裸金属服务器批量挂载共享磁盘

        :param job_type: The job_type of this ShowJobInfosResponse.
        :type: str
        """
        self._job_type = job_type

    @property
    def begin_time(self):
        """Gets the begin_time of this ShowJobInfosResponse.

        开始时间。时间戳格式为ISO 8601，例如：2019-04-25T20:04:47.591Z

        :return: The begin_time of this ShowJobInfosResponse.
        :rtype: datetime
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ShowJobInfosResponse.

        开始时间。时间戳格式为ISO 8601，例如：2019-04-25T20:04:47.591Z

        :param begin_time: The begin_time of this ShowJobInfosResponse.
        :type: datetime
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ShowJobInfosResponse.

        结束时间。时间戳格式为ISO 8601，例如：2019-04-26T20:04:47.591Z

        :return: The end_time of this ShowJobInfosResponse.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ShowJobInfosResponse.

        结束时间。时间戳格式为ISO 8601，例如：2019-04-26T20:04:47.591Z

        :param end_time: The end_time of this ShowJobInfosResponse.
        :type: datetime
        """
        self._end_time = end_time

    @property
    def error_code(self):
        """Gets the error_code of this ShowJobInfosResponse.

        Job执行失败时的错误码

        :return: The error_code of this ShowJobInfosResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ShowJobInfosResponse.

        Job执行失败时的错误码

        :param error_code: The error_code of this ShowJobInfosResponse.
        :type: str
        """
        self._error_code = error_code

    @property
    def fail_reason(self):
        """Gets the fail_reason of this ShowJobInfosResponse.

        Job执行失败时的错误原因

        :return: The fail_reason of this ShowJobInfosResponse.
        :rtype: str
        """
        return self._fail_reason

    @fail_reason.setter
    def fail_reason(self, fail_reason):
        """Sets the fail_reason of this ShowJobInfosResponse.

        Job执行失败时的错误原因

        :param fail_reason: The fail_reason of this ShowJobInfosResponse.
        :type: str
        """
        self._fail_reason = fail_reason

    @property
    def message(self):
        """Gets the message of this ShowJobInfosResponse.

        出现错误时，返回的错误消息

        :return: The message of this ShowJobInfosResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowJobInfosResponse.

        出现错误时，返回的错误消息

        :param message: The message of this ShowJobInfosResponse.
        :type: str
        """
        self._message = message

    @property
    def code(self):
        """Gets the code of this ShowJobInfosResponse.

        出现错误时，返回的错误码。错误码和其对应的含义请参考8.1-状态码。

        :return: The code of this ShowJobInfosResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ShowJobInfosResponse.

        出现错误时，返回的错误码。错误码和其对应的含义请参考8.1-状态码。

        :param code: The code of this ShowJobInfosResponse.
        :type: str
        """
        self._code = code

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
        if not isinstance(other, ShowJobInfosResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
