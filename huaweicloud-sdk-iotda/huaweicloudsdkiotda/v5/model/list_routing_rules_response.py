# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListRoutingRulesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'rules': 'list[RoutingRule]',
        'count': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'rules': 'rules',
        'count': 'count',
        'marker': 'marker'
    }

    def __init__(self, rules=None, count=None, marker=None):
        """ListRoutingRulesResponse - a model defined in huaweicloud sdk"""
        
        super(ListRoutingRulesResponse, self).__init__()

        self._rules = None
        self._count = None
        self._marker = None
        self.discriminator = None

        if rules is not None:
            self.rules = rules
        if count is not None:
            self.count = count
        if marker is not None:
            self.marker = marker

    @property
    def rules(self):
        """Gets the rules of this ListRoutingRulesResponse.

        规则条件信息列表。

        :return: The rules of this ListRoutingRulesResponse.
        :rtype: list[RoutingRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this ListRoutingRulesResponse.

        规则条件信息列表。

        :param rules: The rules of this ListRoutingRulesResponse.
        :type: list[RoutingRule]
        """
        self._rules = rules

    @property
    def count(self):
        """Gets the count of this ListRoutingRulesResponse.

        满足查询条件的记录总数。

        :return: The count of this ListRoutingRulesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListRoutingRulesResponse.

        满足查询条件的记录总数。

        :param count: The count of this ListRoutingRulesResponse.
        :type: int
        """
        self._count = count

    @property
    def marker(self):
        """Gets the marker of this ListRoutingRulesResponse.

        本次分页查询结果中最后一条记录的ID，可在下一次分页查询时使用。

        :return: The marker of this ListRoutingRulesResponse.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListRoutingRulesResponse.

        本次分页查询结果中最后一条记录的ID，可在下一次分页查询时使用。

        :param marker: The marker of this ListRoutingRulesResponse.
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
        if not isinstance(other, ListRoutingRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
