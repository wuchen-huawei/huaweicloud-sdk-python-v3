# coding: utf-8

import pprint
import re

import six





class ListStorageTypeRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'engine_name': 'str'
    }

    attribute_map = {
        'engine_name': 'engine_name'
    }

    def __init__(self, engine_name=None):
        """ListStorageTypeRequest - a model defined in huaweicloud sdk"""
        
        

        self._engine_name = None
        self.discriminator = None

        if engine_name is not None:
            self.engine_name = engine_name

    @property
    def engine_name(self):
        """Gets the engine_name of this ListStorageTypeRequest.

        数据库版本类型： - 取值为“DDS-Community”。

        :return: The engine_name of this ListStorageTypeRequest.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        """Sets the engine_name of this ListStorageTypeRequest.

        数据库版本类型： - 取值为“DDS-Community”。

        :param engine_name: The engine_name of this ListStorageTypeRequest.
        :type: str
        """
        self._engine_name = engine_name

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
        if not isinstance(other, ListStorageTypeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
