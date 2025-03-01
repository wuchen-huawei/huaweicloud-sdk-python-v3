# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListNamespacesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'namespaces': 'list[ShowNamespace]'
    }

    attribute_map = {
        'namespaces': 'namespaces'
    }

    def __init__(self, namespaces=None):
        """ListNamespacesResponse - a model defined in huaweicloud sdk"""
        
        super(ListNamespacesResponse, self).__init__()

        self._namespaces = None
        self.discriminator = None

        if namespaces is not None:
            self.namespaces = namespaces

    @property
    def namespaces(self):
        """Gets the namespaces of this ListNamespacesResponse.

        组织列表

        :return: The namespaces of this ListNamespacesResponse.
        :rtype: list[ShowNamespace]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this ListNamespacesResponse.

        组织列表

        :param namespaces: The namespaces of this ListNamespacesResponse.
        :type: list[ShowNamespace]
        """
        self._namespaces = namespaces

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
        if not isinstance(other, ListNamespacesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
