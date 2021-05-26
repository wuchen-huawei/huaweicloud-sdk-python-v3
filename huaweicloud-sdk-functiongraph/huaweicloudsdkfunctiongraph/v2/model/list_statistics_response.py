# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListStatisticsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'list[MonthUsed]',
        'gbs': 'list[MonthUsed]',
        'statistics': 'ListFunctionStatisticsResponseBody'
    }

    attribute_map = {
        'count': 'count',
        'gbs': 'gbs',
        'statistics': 'statistics'
    }

    def __init__(self, count=None, gbs=None, statistics=None):
        """ListStatisticsResponse - a model defined in huaweicloud sdk"""
        
        super(ListStatisticsResponse, self).__init__()

        self._count = None
        self._gbs = None
        self._statistics = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if gbs is not None:
            self.gbs = gbs
        if statistics is not None:
            self.statistics = statistics

    @property
    def count(self):
        """Gets the count of this ListStatisticsResponse.

        月度调用次数

        :return: The count of this ListStatisticsResponse.
        :rtype: list[MonthUsed]
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListStatisticsResponse.

        月度调用次数

        :param count: The count of this ListStatisticsResponse.
        :type: list[MonthUsed]
        """
        self._count = count

    @property
    def gbs(self):
        """Gets the gbs of this ListStatisticsResponse.

        月度资源用量

        :return: The gbs of this ListStatisticsResponse.
        :rtype: list[MonthUsed]
        """
        return self._gbs

    @gbs.setter
    def gbs(self, gbs):
        """Sets the gbs of this ListStatisticsResponse.

        月度资源用量

        :param gbs: The gbs of this ListStatisticsResponse.
        :type: list[MonthUsed]
        """
        self._gbs = gbs

    @property
    def statistics(self):
        """Gets the statistics of this ListStatisticsResponse.


        :return: The statistics of this ListStatisticsResponse.
        :rtype: ListFunctionStatisticsResponseBody
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this ListStatisticsResponse.


        :param statistics: The statistics of this ListStatisticsResponse.
        :type: ListFunctionStatisticsResponseBody
        """
        self._statistics = statistics

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
        if not isinstance(other, ListStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
