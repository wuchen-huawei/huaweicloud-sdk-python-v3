# coding: utf-8

import pprint
import re

import six





class DeleteListenerTagsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'listener_id': 'str',
        'key': 'str'
    }

    attribute_map = {
        'listener_id': 'listener_id',
        'key': 'key'
    }

    def __init__(self, listener_id=None, key=None):
        """DeleteListenerTagsRequest - a model defined in huaweicloud sdk"""
        
        

        self._listener_id = None
        self._key = None
        self.discriminator = None

        self.listener_id = listener_id
        self.key = key

    @property
    def listener_id(self):
        """Gets the listener_id of this DeleteListenerTagsRequest.

        监听器ID

        :return: The listener_id of this DeleteListenerTagsRequest.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this DeleteListenerTagsRequest.

        监听器ID

        :param listener_id: The listener_id of this DeleteListenerTagsRequest.
        :type: str
        """
        self._listener_id = listener_id

    @property
    def key(self):
        """Gets the key of this DeleteListenerTagsRequest.

        待删除标签的key值。

        :return: The key of this DeleteListenerTagsRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DeleteListenerTagsRequest.

        待删除标签的key值。

        :param key: The key of this DeleteListenerTagsRequest.
        :type: str
        """
        self._key = key

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
        if not isinstance(other, DeleteListenerTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
