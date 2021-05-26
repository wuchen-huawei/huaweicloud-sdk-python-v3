# coding: utf-8

import pprint
import re

import six





class ListNamespacesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_repo_auth': 'str'
    }

    attribute_map = {
        'x_repo_auth': 'X-Repo-Auth'
    }

    def __init__(self, x_repo_auth=None):
        """ListNamespacesRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_repo_auth = None
        self.discriminator = None

        self.x_repo_auth = x_repo_auth

    @property
    def x_repo_auth(self):
        """Gets the x_repo_auth of this ListNamespacesRequest.

        授权名称。

        :return: The x_repo_auth of this ListNamespacesRequest.
        :rtype: str
        """
        return self._x_repo_auth

    @x_repo_auth.setter
    def x_repo_auth(self, x_repo_auth):
        """Sets the x_repo_auth of this ListNamespacesRequest.

        授权名称。

        :param x_repo_auth: The x_repo_auth of this ListNamespacesRequest.
        :type: str
        """
        self._x_repo_auth = x_repo_auth

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
        if not isinstance(other, ListNamespacesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
