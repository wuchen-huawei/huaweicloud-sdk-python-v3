# coding: utf-8

import pprint
import re

import six





class QueryConnectionsResponse:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'client_ip': 'str',
        'count': 'int'
    }

    attribute_map = {
        'client_ip': 'client_ip',
        'count': 'count'
    }

    def __init__(self, client_ip=None, count=None):
        """QueryConnectionsResponse - a model defined in huaweicloud sdk"""
        
        

        self._client_ip = None
        self._count = None
        self.discriminator = None

        self.client_ip = client_ip
        self.count = count

    @property
    def client_ip(self):
        """Gets the client_ip of this QueryConnectionsResponse.

        连接到该实例或节点的客户端IP地址。

        :return: The client_ip of this QueryConnectionsResponse.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this QueryConnectionsResponse.

        连接到该实例或节点的客户端IP地址。

        :param client_ip: The client_ip of this QueryConnectionsResponse.
        :type: str
        """
        self._client_ip = client_ip

    @property
    def count(self):
        """Gets the count of this QueryConnectionsResponse.

        该IP对应的连接数。

        :return: The count of this QueryConnectionsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this QueryConnectionsResponse.

        该IP对应的连接数。

        :param count: The count of this QueryConnectionsResponse.
        :type: int
        """
        self._count = count

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
        if not isinstance(other, QueryConnectionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
