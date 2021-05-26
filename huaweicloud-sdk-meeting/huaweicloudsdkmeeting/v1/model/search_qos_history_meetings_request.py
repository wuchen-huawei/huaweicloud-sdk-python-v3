# coding: utf-8

import pprint
import re

import six





class SearchQosHistoryMeetingsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'start_date': 'int',
        'end_date': 'int',
        'offset': 'int',
        'limit': 'int',
        'search_key': 'str'
    }

    attribute_map = {
        'start_date': 'startDate',
        'end_date': 'endDate',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'searchKey'
    }

    def __init__(self, start_date=None, end_date=None, offset=None, limit=None, search_key=None):
        """SearchQosHistoryMeetingsRequest - a model defined in huaweicloud sdk"""
        
        

        self._start_date = None
        self._end_date = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self.discriminator = None

        self.start_date = start_date
        self.end_date = end_date
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search_key is not None:
            self.search_key = search_key

    @property
    def start_date(self):
        """Gets the start_date of this SearchQosHistoryMeetingsRequest.

        查询的起始日期，Unix时间戳（单位毫秒）。

        :return: The start_date of this SearchQosHistoryMeetingsRequest.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this SearchQosHistoryMeetingsRequest.

        查询的起始日期，Unix时间戳（单位毫秒）。

        :param start_date: The start_date of this SearchQosHistoryMeetingsRequest.
        :type: int
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this SearchQosHistoryMeetingsRequest.

        查询的截止日期，Unix时间戳（单位毫秒）。

        :return: The end_date of this SearchQosHistoryMeetingsRequest.
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this SearchQosHistoryMeetingsRequest.

        查询的截止日期，Unix时间戳（单位毫秒）。

        :param end_date: The end_date of this SearchQosHistoryMeetingsRequest.
        :type: int
        """
        self._end_date = end_date

    @property
    def offset(self):
        """Gets the offset of this SearchQosHistoryMeetingsRequest.

        查询偏移量。 * 取值：大于等于0，默认值为0。 * 小于最小值0时，系统设置为0。 * 大于等于最大条目数量，则返回最后一页的数据。

        :return: The offset of this SearchQosHistoryMeetingsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this SearchQosHistoryMeetingsRequest.

        查询偏移量。 * 取值：大于等于0，默认值为0。 * 小于最小值0时，系统设置为0。 * 大于等于最大条目数量，则返回最后一页的数据。

        :param offset: The offset of this SearchQosHistoryMeetingsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this SearchQosHistoryMeetingsRequest.

        查询的条目数量。 * 取值：1-500，默认值为20。 * 小于最小值1时，系统设置为1。 * 大于最大值500时，系统设置为500。

        :return: The limit of this SearchQosHistoryMeetingsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this SearchQosHistoryMeetingsRequest.

        查询的条目数量。 * 取值：1-500，默认值为20。 * 小于最小值1时，系统设置为1。 * 大于最大值500时，系统设置为500。

        :param limit: The limit of this SearchQosHistoryMeetingsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this SearchQosHistoryMeetingsRequest.

        根据会议主题,预定人和会议id作为关键词，模糊查询会议列表。最大不超过512个字节。

        :return: The search_key of this SearchQosHistoryMeetingsRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this SearchQosHistoryMeetingsRequest.

        根据会议主题,预定人和会议id作为关键词，模糊查询会议列表。最大不超过512个字节。

        :param search_key: The search_key of this SearchQosHistoryMeetingsRequest.
        :type: str
        """
        self._search_key = search_key

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
        if not isinstance(other, SearchQosHistoryMeetingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
