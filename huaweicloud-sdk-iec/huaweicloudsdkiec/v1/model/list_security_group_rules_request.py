# coding: utf-8

import pprint
import re

import six





class ListSecurityGroupRulesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'security_group_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'security_group_id': 'security_group_id'
    }

    def __init__(self, limit=None, offset=None, security_group_id=None):
        """ListSecurityGroupRulesRequest - a model defined in huaweicloud sdk"""
        
        

        self._limit = None
        self._offset = None
        self._security_group_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if security_group_id is not None:
            self.security_group_id = security_group_id

    @property
    def limit(self):
        """Gets the limit of this ListSecurityGroupRulesRequest.

        查询返回边缘安全组规则列表数量。取值范围：0~1000。

        :return: The limit of this ListSecurityGroupRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSecurityGroupRulesRequest.

        查询返回边缘安全组规则列表数量。取值范围：0~1000。

        :param limit: The limit of this ListSecurityGroupRulesRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListSecurityGroupRulesRequest.

        查询的偏移量。

        :return: The offset of this ListSecurityGroupRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSecurityGroupRulesRequest.

        查询的偏移量。

        :param offset: The offset of this ListSecurityGroupRulesRequest.
        :type: int
        """
        self._offset = offset

    @property
    def security_group_id(self):
        """Gets the security_group_id of this ListSecurityGroupRulesRequest.

        安全组ID。uuid

        :return: The security_group_id of this ListSecurityGroupRulesRequest.
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this ListSecurityGroupRulesRequest.

        安全组ID。uuid

        :param security_group_id: The security_group_id of this ListSecurityGroupRulesRequest.
        :type: str
        """
        self._security_group_id = security_group_id

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
        if not isinstance(other, ListSecurityGroupRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
