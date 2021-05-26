# coding: utf-8

import pprint
import re

import six





class UpdateFunctionAsyncInvokeConfigRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'function_urn': 'str',
        'body': 'UpdateFunctionAsyncInvokeConfigRequestBody'
    }

    attribute_map = {
        'function_urn': 'function_urn',
        'body': 'body'
    }

    def __init__(self, function_urn=None, body=None):
        """UpdateFunctionAsyncInvokeConfigRequest - a model defined in huaweicloud sdk"""
        
        

        self._function_urn = None
        self._body = None
        self.discriminator = None

        self.function_urn = function_urn
        if body is not None:
            self.body = body

    @property
    def function_urn(self):
        """Gets the function_urn of this UpdateFunctionAsyncInvokeConfigRequest.

        函数的URN（Uniform Resource Name），唯一标识函数。

        :return: The function_urn of this UpdateFunctionAsyncInvokeConfigRequest.
        :rtype: str
        """
        return self._function_urn

    @function_urn.setter
    def function_urn(self, function_urn):
        """Sets the function_urn of this UpdateFunctionAsyncInvokeConfigRequest.

        函数的URN（Uniform Resource Name），唯一标识函数。

        :param function_urn: The function_urn of this UpdateFunctionAsyncInvokeConfigRequest.
        :type: str
        """
        self._function_urn = function_urn

    @property
    def body(self):
        """Gets the body of this UpdateFunctionAsyncInvokeConfigRequest.


        :return: The body of this UpdateFunctionAsyncInvokeConfigRequest.
        :rtype: UpdateFunctionAsyncInvokeConfigRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateFunctionAsyncInvokeConfigRequest.


        :param body: The body of this UpdateFunctionAsyncInvokeConfigRequest.
        :type: UpdateFunctionAsyncInvokeConfigRequestBody
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
        if not isinstance(other, UpdateFunctionAsyncInvokeConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
