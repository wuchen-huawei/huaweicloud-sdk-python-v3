# coding: utf-8

import pprint
import re

import six





class ListSecretsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'str',
        'marker': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, limit=None, marker=None):
        """ListSecretsRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._marker = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def limit(self):
        """Gets the limit of this ListSecretsRequest.

        每页返回的个数。  默认值：50。 

        :return: The limit of this ListSecretsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSecretsRequest.

        每页返回的个数。  默认值：50。 

        :param limit: The limit of this ListSecretsRequest.
        :type: str
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListSecretsRequest.

        分页查询起始的资源id，为空时为查询第一页 

        :return: The marker of this ListSecretsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListSecretsRequest.

        分页查询起始的资源id，为空时为查询第一页 

        :param marker: The marker of this ListSecretsRequest.
        :type: str
        """
        self._marker = marker

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
        if not isinstance(other, ListSecretsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
