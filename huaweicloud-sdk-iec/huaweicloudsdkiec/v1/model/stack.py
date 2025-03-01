# coding: utf-8

import pprint
import re

import six





class Stack:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'resources': 'list[Resource]'
    }

    attribute_map = {
        'name': 'name',
        'resources': 'resources'
    }

    def __init__(self, name=None, resources=None):
        """Stack - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._resources = None
        self.discriminator = None

        self.name = name
        self.resources = resources

    @property
    def name(self):
        """Gets the name of this Stack.

        边缘资源组名称。 取值范围：只能由中文字符、大小写英文字母、数字及中划线、下划线组成，且长度为[1-48]个字符。

        :return: The name of this Stack.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Stack.

        边缘资源组名称。 取值范围：只能由中文字符、大小写英文字母、数字及中划线、下划线组成，且长度为[1-48]个字符。

        :param name: The name of this Stack.
        :type: str
        """
        self._name = name

    @property
    def resources(self):
        """Gets the resources of this Stack.

        边缘业务的堆栈，即为资源组。

        :return: The resources of this Stack.
        :rtype: list[Resource]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this Stack.

        边缘业务的堆栈，即为资源组。

        :param resources: The resources of this Stack.
        :type: list[Resource]
        """
        self._resources = resources

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
        if not isinstance(other, Stack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
