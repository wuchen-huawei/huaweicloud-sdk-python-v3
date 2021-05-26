# coding: utf-8

import pprint
import re

import six





class ShowTopicAccessPolicyRespPolicies:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'owner': 'bool',
        'user_name': 'str',
        'access_policy': 'str'
    }

    attribute_map = {
        'owner': 'owner',
        'user_name': 'user_name',
        'access_policy': 'access_policy'
    }

    def __init__(self, owner=None, user_name=None, access_policy=None):
        """ShowTopicAccessPolicyRespPolicies - a model defined in huaweicloud sdk"""
        
        

        self._owner = None
        self._user_name = None
        self._access_policy = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if user_name is not None:
            self.user_name = user_name
        if access_policy is not None:
            self.access_policy = access_policy

    @property
    def owner(self):
        """Gets the owner of this ShowTopicAccessPolicyRespPolicies.

        是否为创建topic时所选择的用户。

        :return: The owner of this ShowTopicAccessPolicyRespPolicies.
        :rtype: bool
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ShowTopicAccessPolicyRespPolicies.

        是否为创建topic时所选择的用户。

        :param owner: The owner of this ShowTopicAccessPolicyRespPolicies.
        :type: bool
        """
        self._owner = owner

    @property
    def user_name(self):
        """Gets the user_name of this ShowTopicAccessPolicyRespPolicies.

        用户名。

        :return: The user_name of this ShowTopicAccessPolicyRespPolicies.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ShowTopicAccessPolicyRespPolicies.

        用户名。

        :param user_name: The user_name of this ShowTopicAccessPolicyRespPolicies.
        :type: str
        """
        self._user_name = user_name

    @property
    def access_policy(self):
        """Gets the access_policy of this ShowTopicAccessPolicyRespPolicies.

        权限类型。 - all：拥有发布、订阅权限; - pub：拥有发布权限; - sub：拥有订阅权限。

        :return: The access_policy of this ShowTopicAccessPolicyRespPolicies.
        :rtype: str
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        """Sets the access_policy of this ShowTopicAccessPolicyRespPolicies.

        权限类型。 - all：拥有发布、订阅权限; - pub：拥有发布权限; - sub：拥有订阅权限。

        :param access_policy: The access_policy of this ShowTopicAccessPolicyRespPolicies.
        :type: str
        """
        self._access_policy = access_policy

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
        if not isinstance(other, ShowTopicAccessPolicyRespPolicies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
