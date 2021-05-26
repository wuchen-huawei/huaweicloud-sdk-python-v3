# coding: utf-8

import pprint
import re

import six





class ListUsageTypesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'resource_type_code': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'resource_type_code': 'resource_type_code',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, resource_type_code=None, offset=None, limit=None):
        """ListUsageTypesRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._resource_type_code = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ListUsageTypesRequest.

        |忽略大小写，默认 zh_cn：中文 en_us：英文|

        :return: The x_language of this ListUsageTypesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListUsageTypesRequest.

        |忽略大小写，默认 zh_cn：中文 en_us：英文|

        :param x_language: The x_language of this ListUsageTypesRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this ListUsageTypesRequest.

        |参数名称：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。| |参数的约束及描述：|

        :return: The resource_type_code of this ListUsageTypesRequest.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this ListUsageTypesRequest.

        |参数名称：资源类型编码，例如ECS的VM为“hws.resource.type.vm”。具体请参见资源类型资源类型资源类型资源类型。| |参数的约束及描述：|

        :param resource_type_code: The resource_type_code of this ListUsageTypesRequest.
        :type: str
        """
        self._resource_type_code = resource_type_code

    @property
    def offset(self):
        """Gets the offset of this ListUsageTypesRequest.

        |参数名称：偏移量，从0开始。默认值为0。| |参数的约束及描述：偏移量，从0开始。默认值为0。|

        :return: The offset of this ListUsageTypesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListUsageTypesRequest.

        |参数名称：偏移量，从0开始。默认值为0。| |参数的约束及描述：偏移量，从0开始。默认值为0。|

        :param offset: The offset of this ListUsageTypesRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListUsageTypesRequest.

        |参数名称：每次查询的数量。默认值为10。| |参数的约束及描述：每次查询的数量。默认值为10。|

        :return: The limit of this ListUsageTypesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListUsageTypesRequest.

        |参数名称：每次查询的数量。默认值为10。| |参数的约束及描述：每次查询的数量。默认值为10。|

        :param limit: The limit of this ListUsageTypesRequest.
        :type: int
        """
        self._limit = limit

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
        if not isinstance(other, ListUsageTypesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
