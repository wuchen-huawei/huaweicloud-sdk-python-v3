# coding: utf-8

import pprint
import re

import six





class MetaData:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'offset': 'int',
        'total': 'int',
        'next_token': 'int'
    }

    attribute_map = {
        'count': 'count',
        'offset': 'offset',
        'total': 'total',
        'next_token': 'nextToken'
    }

    def __init__(self, count=None, offset=None, total=None, next_token=None):
        """MetaData - a model defined in huaweicloud sdk"""
        
        

        self._count = None
        self._offset = None
        self._total = None
        self._next_token = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if offset is not None:
            self.offset = offset
        if total is not None:
            self.total = total
        if next_token is not None:
            self.next_token = next_token

    @property
    def count(self):
        """Gets the count of this MetaData.

        当前返回结果条数。

        :return: The count of this MetaData.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this MetaData.

        当前返回结果条数。

        :param count: The count of this MetaData.
        :type: int
        """
        self._count = count

    @property
    def offset(self):
        """Gets the offset of this MetaData.

        下一个开始的标记，用于分页，null表示无更多数据。

        :return: The offset of this MetaData.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this MetaData.

        下一个开始的标记，用于分页，null表示无更多数据。

        :param offset: The offset of this MetaData.
        :type: int
        """
        self._offset = offset

    @property
    def total(self):
        """Gets the total of this MetaData.

        总条数。

        :return: The total of this MetaData.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this MetaData.

        总条数。

        :param total: The total of this MetaData.
        :type: int
        """
        self._total = total

    @property
    def next_token(self):
        """Gets the next_token of this MetaData.

        偏移量。

        :return: The next_token of this MetaData.
        :rtype: int
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this MetaData.

        偏移量。

        :param next_token: The next_token of this MetaData.
        :type: int
        """
        self._next_token = next_token

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
        if not isinstance(other, MetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
