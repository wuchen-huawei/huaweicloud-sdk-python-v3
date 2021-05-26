# coding: utf-8

import pprint
import re

import six





class ListTopicAttributesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'topic_urn': 'str',
        'name': 'str'
    }

    attribute_map = {
        'topic_urn': 'topic_urn',
        'name': 'name'
    }

    def __init__(self, topic_urn=None, name=None):
        """ListTopicAttributesRequest - a model defined in huaweicloud sdk"""
        
        

        self._topic_urn = None
        self._name = None
        self.discriminator = None

        self.topic_urn = topic_urn
        self.name = name

    @property
    def topic_urn(self):
        """Gets the topic_urn of this ListTopicAttributesRequest.

        Topic的唯一的资源标识，可通过[查询主题列表](https://support.huaweicloud.com/api-smn/smn_api_51004.html)获取该标识。

        :return: The topic_urn of this ListTopicAttributesRequest.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this ListTopicAttributesRequest.

        Topic的唯一的资源标识，可通过[查询主题列表](https://support.huaweicloud.com/api-smn/smn_api_51004.html)获取该标识。

        :param topic_urn: The topic_urn of this ListTopicAttributesRequest.
        :type: str
        """
        self._topic_urn = topic_urn

    @property
    def name(self):
        """Gets the name of this ListTopicAttributesRequest.

        主题策略名称。  只支持特定的策略名称，请参见[Topic属性表](https://support.huaweicloud.com/intl/zh-cn/api-smn/smn_api_a1000.html)。

        :return: The name of this ListTopicAttributesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListTopicAttributesRequest.

        主题策略名称。  只支持特定的策略名称，请参见[Topic属性表](https://support.huaweicloud.com/intl/zh-cn/api-smn/smn_api_a1000.html)。

        :param name: The name of this ListTopicAttributesRequest.
        :type: str
        """
        self._name = name

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
        if not isinstance(other, ListTopicAttributesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
