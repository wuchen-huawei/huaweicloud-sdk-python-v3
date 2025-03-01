# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ResetVisionActiveCodeResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'active_code': 'str'
    }

    attribute_map = {
        'active_code': 'activeCode'
    }

    def __init__(self, active_code=None):
        """ResetVisionActiveCodeResponse - a model defined in huaweicloud sdk"""
        
        super(ResetVisionActiveCodeResponse, self).__init__()

        self._active_code = None
        self.discriminator = None

        if active_code is not None:
            self.active_code = active_code

    @property
    def active_code(self):
        """Gets the active_code of this ResetVisionActiveCodeResponse.

        激活码

        :return: The active_code of this ResetVisionActiveCodeResponse.
        :rtype: str
        """
        return self._active_code

    @active_code.setter
    def active_code(self, active_code):
        """Sets the active_code of this ResetVisionActiveCodeResponse.

        激活码

        :param active_code: The active_code of this ResetVisionActiveCodeResponse.
        :type: str
        """
        self._active_code = active_code

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
        if not isinstance(other, ResetVisionActiveCodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
