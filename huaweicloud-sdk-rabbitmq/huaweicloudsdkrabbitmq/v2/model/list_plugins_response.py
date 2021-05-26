# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListPluginsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'plugins': 'list[ListPluginsRespPlugins]'
    }

    attribute_map = {
        'plugins': 'plugins'
    }

    def __init__(self, plugins=None):
        """ListPluginsResponse - a model defined in huaweicloud sdk"""
        
        super(ListPluginsResponse, self).__init__()

        self._plugins = None
        self.discriminator = None

        if plugins is not None:
            self.plugins = plugins

    @property
    def plugins(self):
        """Gets the plugins of this ListPluginsResponse.

        插件信息列表。

        :return: The plugins of this ListPluginsResponse.
        :rtype: list[ListPluginsRespPlugins]
        """
        return self._plugins

    @plugins.setter
    def plugins(self, plugins):
        """Sets the plugins of this ListPluginsResponse.

        插件信息列表。

        :param plugins: The plugins of this ListPluginsResponse.
        :type: list[ListPluginsRespPlugins]
        """
        self._plugins = plugins

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
        if not isinstance(other, ListPluginsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
