# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListInstancesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'instances': 'list[InstanceListView]'
    }

    attribute_map = {
        'count': 'count',
        'instances': 'instances'
    }

    def __init__(self, count=None, instances=None):
        """ListInstancesResponse - a model defined in huaweicloud sdk"""
        
        super(ListInstancesResponse, self).__init__()

        self._count = None
        self._instances = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if instances is not None:
            self.instances = instances

    @property
    def count(self):
        """Gets the count of this ListInstancesResponse.

        实例总数。

        :return: The count of this ListInstancesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListInstancesResponse.

        实例总数。

        :param count: The count of this ListInstancesResponse.
        :type: int
        """
        self._count = count

    @property
    def instances(self):
        """Gets the instances of this ListInstancesResponse.

        实例列表。

        :return: The instances of this ListInstancesResponse.
        :rtype: list[InstanceListView]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ListInstancesResponse.

        实例列表。

        :param instances: The instances of this ListInstancesResponse.
        :type: list[InstanceListView]
        """
        self._instances = instances

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
        if not isinstance(other, ListInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
