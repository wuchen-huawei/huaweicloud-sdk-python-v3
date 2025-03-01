# coding: utf-8

import pprint
import re

import six





class UpdateTopicAccessPolicyReqTopics:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'policies': 'list[UpdateTopicAccessPolicyReqPolicies]'
    }

    attribute_map = {
        'name': 'name',
        'policies': 'policies'
    }

    def __init__(self, name=None, policies=None):
        """UpdateTopicAccessPolicyReqTopics - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._policies = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if policies is not None:
            self.policies = policies

    @property
    def name(self):
        """Gets the name of this UpdateTopicAccessPolicyReqTopics.

        topic名称。

        :return: The name of this UpdateTopicAccessPolicyReqTopics.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateTopicAccessPolicyReqTopics.

        topic名称。

        :param name: The name of this UpdateTopicAccessPolicyReqTopics.
        :type: str
        """
        self._name = name

    @property
    def policies(self):
        """Gets the policies of this UpdateTopicAccessPolicyReqTopics.

        权限列表。

        :return: The policies of this UpdateTopicAccessPolicyReqTopics.
        :rtype: list[UpdateTopicAccessPolicyReqPolicies]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this UpdateTopicAccessPolicyReqTopics.

        权限列表。

        :param policies: The policies of this UpdateTopicAccessPolicyReqTopics.
        :type: list[UpdateTopicAccessPolicyReqPolicies]
        """
        self._policies = policies

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
        if not isinstance(other, UpdateTopicAccessPolicyReqTopics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
