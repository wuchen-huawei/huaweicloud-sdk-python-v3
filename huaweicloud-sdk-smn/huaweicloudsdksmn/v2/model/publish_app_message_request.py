# coding: utf-8

import pprint
import re

import six





class PublishAppMessageRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'endpoint_urn': 'str',
        'body': 'PublishAppMessageRequestBody'
    }

    attribute_map = {
        'endpoint_urn': 'endpoint_urn',
        'body': 'body'
    }

    def __init__(self, endpoint_urn=None, body=None):
        """PublishAppMessageRequest - a model defined in huaweicloud sdk"""
        
        

        self._endpoint_urn = None
        self._body = None
        self.discriminator = None

        self.endpoint_urn = endpoint_urn
        if body is not None:
            self.body = body

    @property
    def endpoint_urn(self):
        """Gets the endpoint_urn of this PublishAppMessageRequest.

        Endpoint的唯一资源标识，可通过[查询Application的Endpoint列表](https://support.huaweicloud.com/api-smn/smn_api_58004.html)获取该标识

        :return: The endpoint_urn of this PublishAppMessageRequest.
        :rtype: str
        """
        return self._endpoint_urn

    @endpoint_urn.setter
    def endpoint_urn(self, endpoint_urn):
        """Sets the endpoint_urn of this PublishAppMessageRequest.

        Endpoint的唯一资源标识，可通过[查询Application的Endpoint列表](https://support.huaweicloud.com/api-smn/smn_api_58004.html)获取该标识

        :param endpoint_urn: The endpoint_urn of this PublishAppMessageRequest.
        :type: str
        """
        self._endpoint_urn = endpoint_urn

    @property
    def body(self):
        """Gets the body of this PublishAppMessageRequest.


        :return: The body of this PublishAppMessageRequest.
        :rtype: PublishAppMessageRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this PublishAppMessageRequest.


        :param body: The body of this PublishAppMessageRequest.
        :type: PublishAppMessageRequestBody
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
        if not isinstance(other, PublishAppMessageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
