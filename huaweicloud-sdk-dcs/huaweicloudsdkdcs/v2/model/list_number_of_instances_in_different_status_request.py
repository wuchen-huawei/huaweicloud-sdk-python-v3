# coding: utf-8

import pprint
import re

import six





class ListNumberOfInstancesInDifferentStatusRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'include_failure': 'str'
    }

    attribute_map = {
        'include_failure': 'include_failure'
    }

    def __init__(self, include_failure=None):
        """ListNumberOfInstancesInDifferentStatusRequest - a model defined in huaweicloud sdk"""
        
        

        self._include_failure = None
        self.discriminator = None

        if include_failure is not None:
            self.include_failure = include_failure

    @property
    def include_failure(self):
        """Gets the include_failure of this ListNumberOfInstancesInDifferentStatusRequest.

        是否返回创建失败的实例数。   - 当参数值为“true”时，返回的统计包括创建失败的实例数。   - 参数值为“false”或者其他值，返回的统计不包括创建失败的实例数。 

        :return: The include_failure of this ListNumberOfInstancesInDifferentStatusRequest.
        :rtype: str
        """
        return self._include_failure

    @include_failure.setter
    def include_failure(self, include_failure):
        """Sets the include_failure of this ListNumberOfInstancesInDifferentStatusRequest.

        是否返回创建失败的实例数。   - 当参数值为“true”时，返回的统计包括创建失败的实例数。   - 参数值为“false”或者其他值，返回的统计不包括创建失败的实例数。 

        :param include_failure: The include_failure of this ListNumberOfInstancesInDifferentStatusRequest.
        :type: str
        """
        self._include_failure = include_failure

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
        if not isinstance(other, ListNumberOfInstancesInDifferentStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
