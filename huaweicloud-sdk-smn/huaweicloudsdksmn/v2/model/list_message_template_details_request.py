# coding: utf-8

import pprint
import re

import six





class ListMessageTemplateDetailsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'message_template_id': 'str'
    }

    attribute_map = {
        'message_template_id': 'message_template_id'
    }

    def __init__(self, message_template_id=None):
        """ListMessageTemplateDetailsRequest - a model defined in huaweicloud sdk"""
        
        

        self._message_template_id = None
        self.discriminator = None

        self.message_template_id = message_template_id

    @property
    def message_template_id(self):
        """Gets the message_template_id of this ListMessageTemplateDetailsRequest.

        模板唯一的资源标识，可通过查询[消息模板列表](https://support.huaweicloud.com/api-smn/smn_api_53004.html)获取该标识。

        :return: The message_template_id of this ListMessageTemplateDetailsRequest.
        :rtype: str
        """
        return self._message_template_id

    @message_template_id.setter
    def message_template_id(self, message_template_id):
        """Sets the message_template_id of this ListMessageTemplateDetailsRequest.

        模板唯一的资源标识，可通过查询[消息模板列表](https://support.huaweicloud.com/api-smn/smn_api_53004.html)获取该标识。

        :param message_template_id: The message_template_id of this ListMessageTemplateDetailsRequest.
        :type: str
        """
        self._message_template_id = message_template_id

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
        if not isinstance(other, ListMessageTemplateDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
