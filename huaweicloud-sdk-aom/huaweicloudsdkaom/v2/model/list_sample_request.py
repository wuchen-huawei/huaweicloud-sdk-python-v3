# coding: utf-8

import pprint
import re

import six





class ListSampleRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'fill_value': 'str',
        'body': 'QuerySampleParam'
    }

    attribute_map = {
        'fill_value': 'fill_value',
        'body': 'body'
    }

    def __init__(self, fill_value=None, body=None):
        """ListSampleRequest - a model defined in huaweicloud sdk"""
        
        

        self._fill_value = None
        self._body = None
        self.discriminator = None

        if fill_value is not None:
            self.fill_value = fill_value
        if body is not None:
            self.body = body

    @property
    def fill_value(self):
        """Gets the fill_value of this ListSampleRequest.

        用于对查询到的时序数据进行断点插值，默认值为-1。 -1：断点处使用-1进行表示。 0 ：断点处使用0进行表示。 null：断点处使用null进行表示。 average：断点处使用前后邻近的有效数据的平均值进行表示，如果不存在有效数据则使用null进行表示。 

        :return: The fill_value of this ListSampleRequest.
        :rtype: str
        """
        return self._fill_value

    @fill_value.setter
    def fill_value(self, fill_value):
        """Sets the fill_value of this ListSampleRequest.

        用于对查询到的时序数据进行断点插值，默认值为-1。 -1：断点处使用-1进行表示。 0 ：断点处使用0进行表示。 null：断点处使用null进行表示。 average：断点处使用前后邻近的有效数据的平均值进行表示，如果不存在有效数据则使用null进行表示。 

        :param fill_value: The fill_value of this ListSampleRequest.
        :type: str
        """
        self._fill_value = fill_value

    @property
    def body(self):
        """Gets the body of this ListSampleRequest.


        :return: The body of this ListSampleRequest.
        :rtype: QuerySampleParam
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListSampleRequest.


        :param body: The body of this ListSampleRequest.
        :type: QuerySampleParam
        """
        self._body = body

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
        if not isinstance(other, ListSampleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
