# coding: utf-8

import pprint
import re

import six





class ListCustomLineRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'line_id': 'str',
        'name': 'str',
        'limit': 'int',
        'offset': 'int',
        'show_detail': 'bool'
    }

    attribute_map = {
        'line_id': 'line_id',
        'name': 'name',
        'limit': 'limit',
        'offset': 'offset',
        'show_detail': 'show_detail'
    }

    def __init__(self, line_id=None, name=None, limit=None, offset=None, show_detail=None):
        """ListCustomLineRequest - a model defined in huaweicloud sdk"""
        
        

        self._line_id = None
        self._name = None
        self._limit = None
        self._offset = None
        self._show_detail = None
        self.discriminator = None

        if line_id is not None:
            self.line_id = line_id
        if name is not None:
            self.name = name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if show_detail is not None:
            self.show_detail = show_detail

    @property
    def line_id(self):
        """Gets the line_id of this ListCustomLineRequest.

        解析线路ID。

        :return: The line_id of this ListCustomLineRequest.
        :rtype: str
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        """Sets the line_id of this ListCustomLineRequest.

        解析线路ID。

        :param line_id: The line_id of this ListCustomLineRequest.
        :type: str
        """
        self._line_id = line_id

    @property
    def name(self):
        """Gets the name of this ListCustomLineRequest.

        解析线路名称。

        :return: The name of this ListCustomLineRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListCustomLineRequest.

        解析线路名称。

        :param name: The name of this ListCustomLineRequest.
        :type: str
        """
        self._name = name

    @property
    def limit(self):
        """Gets the limit of this ListCustomLineRequest.

        每页返回的资源个数。取值范围为0~100。

        :return: The limit of this ListCustomLineRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCustomLineRequest.

        每页返回的资源个数。取值范围为0~100。

        :param limit: The limit of this ListCustomLineRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListCustomLineRequest.

        分页查询起始偏移量，表示从偏移量的下一个资源开始查询。

        :return: The offset of this ListCustomLineRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCustomLineRequest.

        分页查询起始偏移量，表示从偏移量的下一个资源开始查询。

        :param offset: The offset of this ListCustomLineRequest.
        :type: int
        """
        self._offset = offset

    @property
    def show_detail(self):
        """Gets the show_detail of this ListCustomLineRequest.

        是否查询详细信息。  取值范围：  true：是，查询详细信息。 false：否，不查询详细信息。 默认为true。

        :return: The show_detail of this ListCustomLineRequest.
        :rtype: bool
        """
        return self._show_detail

    @show_detail.setter
    def show_detail(self, show_detail):
        """Sets the show_detail of this ListCustomLineRequest.

        是否查询详细信息。  取值范围：  true：是，查询详细信息。 false：否，不查询详细信息。 默认为true。

        :param show_detail: The show_detail of this ListCustomLineRequest.
        :type: bool
        """
        self._show_detail = show_detail

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
        if not isinstance(other, ListCustomLineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
