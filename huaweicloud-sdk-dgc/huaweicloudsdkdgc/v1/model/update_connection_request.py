# coding: utf-8

import pprint
import re

import six





class UpdateConnectionRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'connection_name': 'str',
        'body': 'ConnectionInfo'
    }

    attribute_map = {
        'connection_name': 'connection_name',
        'body': 'body'
    }

    def __init__(self, connection_name=None, body=None):
        """UpdateConnectionRequest - a model defined in huaweicloud sdk"""
        
        

        self._connection_name = None
        self._body = None
        self.discriminator = None

        self.connection_name = connection_name
        if body is not None:
            self.body = body

    @property
    def connection_name(self):
        """Gets the connection_name of this UpdateConnectionRequest.

        连接名称.

        :return: The connection_name of this UpdateConnectionRequest.
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        """Sets the connection_name of this UpdateConnectionRequest.

        连接名称.

        :param connection_name: The connection_name of this UpdateConnectionRequest.
        :type: str
        """
        self._connection_name = connection_name

    @property
    def body(self):
        """Gets the body of this UpdateConnectionRequest.


        :return: The body of this UpdateConnectionRequest.
        :rtype: ConnectionInfo
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateConnectionRequest.


        :param body: The body of this UpdateConnectionRequest.
        :type: ConnectionInfo
        """
        self._body = body

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
        if not isinstance(other, UpdateConnectionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
