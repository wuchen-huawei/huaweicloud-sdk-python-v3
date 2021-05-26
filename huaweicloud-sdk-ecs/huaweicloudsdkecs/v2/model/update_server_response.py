# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdateServerResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'server': 'UpdateServerResult'
    }

    attribute_map = {
        'server': 'server'
    }

    def __init__(self, server=None):
        """UpdateServerResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateServerResponse, self).__init__()

        self._server = None
        self.discriminator = None

        if server is not None:
            self.server = server

    @property
    def server(self):
        """Gets the server of this UpdateServerResponse.


        :return: The server of this UpdateServerResponse.
        :rtype: UpdateServerResult
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this UpdateServerResponse.


        :param server: The server of this UpdateServerResponse.
        :type: UpdateServerResult
        """
        self._server = server

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
        if not isinstance(other, UpdateServerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
