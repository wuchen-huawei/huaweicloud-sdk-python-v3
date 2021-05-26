# coding: utf-8

import pprint
import re

import six





class PersonalityResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'path': 'str',
        'content': 'str'
    }

    attribute_map = {
        'path': 'path',
        'content': 'content'
    }

    def __init__(self, path=None, content=None):
        """PersonalityResult - a model defined in huaweicloud sdk"""
        
        

        self._path = None
        self._content = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if content is not None:
            self.content = content

    @property
    def path(self):
        """Gets the path of this PersonalityResult.

        注入文件路径信息。

        :return: The path of this PersonalityResult.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PersonalityResult.

        注入文件路径信息。

        :param path: The path of this PersonalityResult.
        :type: str
        """
        self._path = path

    @property
    def content(self):
        """Gets the content of this PersonalityResult.

        注入文件内容，base64格式编码。

        :return: The content of this PersonalityResult.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this PersonalityResult.

        注入文件内容，base64格式编码。

        :param content: The content of this PersonalityResult.
        :type: str
        """
        self._content = content

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
        if not isinstance(other, PersonalityResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
