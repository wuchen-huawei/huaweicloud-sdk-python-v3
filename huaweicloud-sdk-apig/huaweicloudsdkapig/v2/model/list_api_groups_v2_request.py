# coding: utf-8

import pprint
import re

import six





class ListApiGroupsV2Request:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'id': 'str',
        'name': 'str',
        'offset': 'int',
        'limit': 'int',
        'precise_search': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'id': 'id',
        'name': 'name',
        'offset': 'offset',
        'limit': 'limit',
        'precise_search': 'precise_search'
    }

    def __init__(self, instance_id=None, id=None, name=None, offset=None, limit=None, precise_search=None):
        """ListApiGroupsV2Request - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._id = None
        self._name = None
        self._offset = None
        self._limit = None
        self._precise_search = None
        self.discriminator = None

        self.instance_id = instance_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if precise_search is not None:
            self.precise_search = precise_search

    @property
    def instance_id(self):
        """Gets the instance_id of this ListApiGroupsV2Request.

        实例编号

        :return: The instance_id of this ListApiGroupsV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListApiGroupsV2Request.

        实例编号

        :param instance_id: The instance_id of this ListApiGroupsV2Request.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def id(self):
        """Gets the id of this ListApiGroupsV2Request.

        API分组编号

        :return: The id of this ListApiGroupsV2Request.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListApiGroupsV2Request.

        API分组编号

        :param id: The id of this ListApiGroupsV2Request.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListApiGroupsV2Request.

        API分组名称

        :return: The name of this ListApiGroupsV2Request.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListApiGroupsV2Request.

        API分组名称

        :param name: The name of this ListApiGroupsV2Request.
        :type: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListApiGroupsV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListApiGroupsV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListApiGroupsV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListApiGroupsV2Request.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListApiGroupsV2Request.

        每页显示的条目数量

        :return: The limit of this ListApiGroupsV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListApiGroupsV2Request.

        每页显示的条目数量

        :param limit: The limit of this ListApiGroupsV2Request.
        :type: int
        """
        self._limit = limit

    @property
    def precise_search(self):
        """Gets the precise_search of this ListApiGroupsV2Request.

        指定需要精确匹配查找的参数名称，目前仅支持API分组名称

        :return: The precise_search of this ListApiGroupsV2Request.
        :rtype: str
        """
        return self._precise_search

    @precise_search.setter
    def precise_search(self, precise_search):
        """Sets the precise_search of this ListApiGroupsV2Request.

        指定需要精确匹配查找的参数名称，目前仅支持API分组名称

        :param precise_search: The precise_search of this ListApiGroupsV2Request.
        :type: str
        """
        self._precise_search = precise_search

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
        if not isinstance(other, ListApiGroupsV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
