# coding: utf-8

import pprint
import re

import six





class ListResourceTagsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'resource_id': 'str'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_id': 'resource_id'
    }

    def __init__(self, resource_type=None, resource_id=None):
        """ListResourceTagsRequest - a model defined in huaweicloud sdk"""
        
        

        self._resource_type = None
        self._resource_id = None
        self.discriminator = None

        self.resource_type = resource_type
        self.resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this ListResourceTagsRequest.

        资源类型 目前有: smn_topic，主题 smn_sms，短信 smn_application，移动推送

        :return: The resource_type of this ListResourceTagsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListResourceTagsRequest.

        资源类型 目前有: smn_topic，主题 smn_sms，短信 smn_application，移动推送

        :param resource_type: The resource_type of this ListResourceTagsRequest.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this ListResourceTagsRequest.

        资源ID。  获取resource_id的方法：  当resource_type为“smn_topic”时， 手动添加请求消息头“X-SMN-RESOURCEID-TYPE=name”，资源ID即为topic名称。 不添加请求消息头，通过“查询资源实例”，获取资源ID。 当resource_type为“smn_sms”时，resource_id为签名ID。您可在控制台获取。

        :return: The resource_id of this ListResourceTagsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListResourceTagsRequest.

        资源ID。  获取resource_id的方法：  当resource_type为“smn_topic”时， 手动添加请求消息头“X-SMN-RESOURCEID-TYPE=name”，资源ID即为topic名称。 不添加请求消息头，通过“查询资源实例”，获取资源ID。 当resource_type为“smn_sms”时，resource_id为签名ID。您可在控制台获取。

        :param resource_id: The resource_id of this ListResourceTagsRequest.
        :type: str
        """
        self._resource_id = resource_id

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
        if not isinstance(other, ListResourceTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
