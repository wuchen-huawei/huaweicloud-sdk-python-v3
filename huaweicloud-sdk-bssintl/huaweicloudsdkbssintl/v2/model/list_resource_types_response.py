# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListResourceTypesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_types': 'list[ResourceType]'
    }

    attribute_map = {
        'resource_types': 'resource_types'
    }

    def __init__(self, resource_types=None):
        """ListResourceTypesResponse - a model defined in huaweicloud sdk"""
        
        super(ListResourceTypesResponse, self).__init__()

        self._resource_types = None
        self.discriminator = None

        if resource_types is not None:
            self.resource_types = resource_types

    @property
    def resource_types(self):
        """Gets the resource_types of this ListResourceTypesResponse.

        |参数名称：返回数据| |参数约束以及描述：返回数据|

        :return: The resource_types of this ListResourceTypesResponse.
        :rtype: list[ResourceType]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        """Sets the resource_types of this ListResourceTypesResponse.

        |参数名称：返回数据| |参数约束以及描述：返回数据|

        :param resource_types: The resource_types of this ListResourceTypesResponse.
        :type: list[ResourceType]
        """
        self._resource_types = resource_types

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
        if not isinstance(other, ListResourceTypesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
