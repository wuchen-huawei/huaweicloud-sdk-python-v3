# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListSecurityGroupsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'security_groups': 'list[SecurityGroup]',
        'count': 'int'
    }

    attribute_map = {
        'security_groups': 'security_groups',
        'count': 'count'
    }

    def __init__(self, security_groups=None, count=None):
        """ListSecurityGroupsResponse - a model defined in huaweicloud sdk"""
        
        super(ListSecurityGroupsResponse, self).__init__()

        self._security_groups = None
        self._count = None
        self.discriminator = None

        if security_groups is not None:
            self.security_groups = security_groups
        if count is not None:
            self.count = count

    @property
    def security_groups(self):
        """Gets the security_groups of this ListSecurityGroupsResponse.

        安全组列表对象。

        :return: The security_groups of this ListSecurityGroupsResponse.
        :rtype: list[SecurityGroup]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this ListSecurityGroupsResponse.

        安全组列表对象。

        :param security_groups: The security_groups of this ListSecurityGroupsResponse.
        :type: list[SecurityGroup]
        """
        self._security_groups = security_groups

    @property
    def count(self):
        """Gets the count of this ListSecurityGroupsResponse.

        安全组的列表总数。

        :return: The count of this ListSecurityGroupsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListSecurityGroupsResponse.

        安全组的列表总数。

        :param count: The count of this ListSecurityGroupsResponse.
        :type: int
        """
        self._count = count

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
        if not isinstance(other, ListSecurityGroupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
