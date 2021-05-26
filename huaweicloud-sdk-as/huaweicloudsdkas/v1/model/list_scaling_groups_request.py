# coding: utf-8

import pprint
import re

import six





class ListScalingGroupsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_group_name': 'str',
        'scaling_configuration_id': 'str',
        'scaling_group_status': 'str',
        'start_number': 'int',
        'limit': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'scaling_group_name': 'scaling_group_name',
        'scaling_configuration_id': 'scaling_configuration_id',
        'scaling_group_status': 'scaling_group_status',
        'start_number': 'start_number',
        'limit': 'limit',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, scaling_group_name=None, scaling_configuration_id=None, scaling_group_status=None, start_number=None, limit=None, enterprise_project_id=None):
        """ListScalingGroupsRequest - a model defined in huaweicloud sdk"""
        
        

        self._scaling_group_name = None
        self._scaling_configuration_id = None
        self._scaling_group_status = None
        self._start_number = None
        self._limit = None
        self._enterprise_project_id = None
        self.discriminator = None

        if scaling_group_name is not None:
            self.scaling_group_name = scaling_group_name
        if scaling_configuration_id is not None:
            self.scaling_configuration_id = scaling_configuration_id
        if scaling_group_status is not None:
            self.scaling_group_status = scaling_group_status
        if start_number is not None:
            self.start_number = start_number
        if limit is not None:
            self.limit = limit
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def scaling_group_name(self):
        """Gets the scaling_group_name of this ListScalingGroupsRequest.

        伸缩组名称

        :return: The scaling_group_name of this ListScalingGroupsRequest.
        :rtype: str
        """
        return self._scaling_group_name

    @scaling_group_name.setter
    def scaling_group_name(self, scaling_group_name):
        """Sets the scaling_group_name of this ListScalingGroupsRequest.

        伸缩组名称

        :param scaling_group_name: The scaling_group_name of this ListScalingGroupsRequest.
        :type: str
        """
        self._scaling_group_name = scaling_group_name

    @property
    def scaling_configuration_id(self):
        """Gets the scaling_configuration_id of this ListScalingGroupsRequest.

        伸缩配置ID，通过查询弹性伸缩配置列表接口获取，详见查询弹性伸缩配置列表。

        :return: The scaling_configuration_id of this ListScalingGroupsRequest.
        :rtype: str
        """
        return self._scaling_configuration_id

    @scaling_configuration_id.setter
    def scaling_configuration_id(self, scaling_configuration_id):
        """Sets the scaling_configuration_id of this ListScalingGroupsRequest.

        伸缩配置ID，通过查询弹性伸缩配置列表接口获取，详见查询弹性伸缩配置列表。

        :param scaling_configuration_id: The scaling_configuration_id of this ListScalingGroupsRequest.
        :type: str
        """
        self._scaling_configuration_id = scaling_configuration_id

    @property
    def scaling_group_status(self):
        """Gets the scaling_group_status of this ListScalingGroupsRequest.

        伸缩组状态，包括INSERVICE，PAUSED，ERROR，DELETING。

        :return: The scaling_group_status of this ListScalingGroupsRequest.
        :rtype: str
        """
        return self._scaling_group_status

    @scaling_group_status.setter
    def scaling_group_status(self, scaling_group_status):
        """Sets the scaling_group_status of this ListScalingGroupsRequest.

        伸缩组状态，包括INSERVICE，PAUSED，ERROR，DELETING。

        :param scaling_group_status: The scaling_group_status of this ListScalingGroupsRequest.
        :type: str
        """
        self._scaling_group_status = scaling_group_status

    @property
    def start_number(self):
        """Gets the start_number of this ListScalingGroupsRequest.

        查询的起始行号，默认为0。

        :return: The start_number of this ListScalingGroupsRequest.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        """Sets the start_number of this ListScalingGroupsRequest.

        查询的起始行号，默认为0。

        :param start_number: The start_number of this ListScalingGroupsRequest.
        :type: int
        """
        self._start_number = start_number

    @property
    def limit(self):
        """Gets the limit of this ListScalingGroupsRequest.

        查询的记录条数，默认为20。

        :return: The limit of this ListScalingGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListScalingGroupsRequest.

        查询的记录条数，默认为20。

        :param limit: The limit of this ListScalingGroupsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListScalingGroupsRequest.

        企业项目ID，当传入all_granted_eps时表示查询该用户所有授权的企业项目下的伸缩组列表

        :return: The enterprise_project_id of this ListScalingGroupsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListScalingGroupsRequest.

        企业项目ID，当传入all_granted_eps时表示查询该用户所有授权的企业项目下的伸缩组列表

        :param enterprise_project_id: The enterprise_project_id of this ListScalingGroupsRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListScalingGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
