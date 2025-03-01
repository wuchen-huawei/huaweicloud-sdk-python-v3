# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UnfreezeSubCustomersResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'error_details': 'list[CustomerErrorDetail]'
    }

    attribute_map = {
        'error_details': 'error_details'
    }

    def __init__(self, error_details=None):
        """UnfreezeSubCustomersResponse - a model defined in huaweicloud sdk"""
        
        super(UnfreezeSubCustomersResponse, self).__init__()

        self._error_details = None
        self.discriminator = None

        if error_details is not None:
            self.error_details = error_details

    @property
    def error_details(self):
        """Gets the error_details of this UnfreezeSubCustomersResponse.

        |参数名称：错误原因，部分成功部分失败的时候会返回失败的客户列表和错误原因。注意这个结构体在HTTP 200的时候返回| |参数约束以及描述：错误原因，部分成功部分失败的时候会返回失败的客户列表和错误原因。注意这个结构体在HTTP 200的时候返回|

        :return: The error_details of this UnfreezeSubCustomersResponse.
        :rtype: list[CustomerErrorDetail]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this UnfreezeSubCustomersResponse.

        |参数名称：错误原因，部分成功部分失败的时候会返回失败的客户列表和错误原因。注意这个结构体在HTTP 200的时候返回| |参数约束以及描述：错误原因，部分成功部分失败的时候会返回失败的客户列表和错误原因。注意这个结构体在HTTP 200的时候返回|

        :param error_details: The error_details of this UnfreezeSubCustomersResponse.
        :type: list[CustomerErrorDetail]
        """
        self._error_details = error_details

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
        if not isinstance(other, UnfreezeSubCustomersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
