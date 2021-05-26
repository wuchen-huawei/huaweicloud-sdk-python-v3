# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ExpandEdgecloudResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'deployment_id': 'str',
        'status': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'deployment_id': 'deployment_id',
        'status': 'status',
        'job_id': 'job_id'
    }

    def __init__(self, id=None, name=None, deployment_id=None, status=None, job_id=None):
        """ExpandEdgecloudResponse - a model defined in huaweicloud sdk"""
        
        super(ExpandEdgecloudResponse, self).__init__()

        self._id = None
        self._name = None
        self._deployment_id = None
        self._status = None
        self._job_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if deployment_id is not None:
            self.deployment_id = deployment_id
        if status is not None:
            self.status = status
        if job_id is not None:
            self.job_id = job_id

    @property
    def id(self):
        """Gets the id of this ExpandEdgecloudResponse.

        边缘业务ID。

        :return: The id of this ExpandEdgecloudResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExpandEdgecloudResponse.

        边缘业务ID。

        :param id: The id of this ExpandEdgecloudResponse.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ExpandEdgecloudResponse.

        部署计划名称。

        :return: The name of this ExpandEdgecloudResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExpandEdgecloudResponse.

        部署计划名称。

        :param name: The name of this ExpandEdgecloudResponse.
        :type: str
        """
        self._name = name

    @property
    def deployment_id(self):
        """Gets the deployment_id of this ExpandEdgecloudResponse.

        部署计划ID。

        :return: The deployment_id of this ExpandEdgecloudResponse.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this ExpandEdgecloudResponse.

        部署计划ID。

        :param deployment_id: The deployment_id of this ExpandEdgecloudResponse.
        :type: str
        """
        self._deployment_id = deployment_id

    @property
    def status(self):
        """Gets the status of this ExpandEdgecloudResponse.

        边缘业务状态，现存状态有： - creating/scheduling/updating：部署中 - inService：运行中 - failed：创建失败 - deleting：删除中 - delFailed：删除失败

        :return: The status of this ExpandEdgecloudResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExpandEdgecloudResponse.

        边缘业务状态，现存状态有： - creating/scheduling/updating：部署中 - inService：运行中 - failed：创建失败 - deleting：删除中 - delFailed：删除失败

        :param status: The status of this ExpandEdgecloudResponse.
        :type: str
        """
        self._status = status

    @property
    def job_id(self):
        """Gets the job_id of this ExpandEdgecloudResponse.

        任务ID。

        :return: The job_id of this ExpandEdgecloudResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ExpandEdgecloudResponse.

        任务ID。

        :param job_id: The job_id of this ExpandEdgecloudResponse.
        :type: str
        """
        self._job_id = job_id

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
        if not isinstance(other, ExpandEdgecloudResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
