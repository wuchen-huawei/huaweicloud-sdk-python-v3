# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListPostgresqlDbUserPaginatedResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'users': 'list[PostgresqlUserForList]',
        'total_count': 'int'
    }

    attribute_map = {
        'users': 'users',
        'total_count': 'total_count'
    }

    def __init__(self, users=None, total_count=None):
        """ListPostgresqlDbUserPaginatedResponse - a model defined in huaweicloud sdk"""
        
        super(ListPostgresqlDbUserPaginatedResponse, self).__init__()

        self._users = None
        self._total_count = None
        self.discriminator = None

        if users is not None:
            self.users = users
        if total_count is not None:
            self.total_count = total_count

    @property
    def users(self):
        """Gets the users of this ListPostgresqlDbUserPaginatedResponse.

        列表中每个元素表示一个数据库用户。

        :return: The users of this ListPostgresqlDbUserPaginatedResponse.
        :rtype: list[PostgresqlUserForList]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this ListPostgresqlDbUserPaginatedResponse.

        列表中每个元素表示一个数据库用户。

        :param users: The users of this ListPostgresqlDbUserPaginatedResponse.
        :type: list[PostgresqlUserForList]
        """
        self._users = users

    @property
    def total_count(self):
        """Gets the total_count of this ListPostgresqlDbUserPaginatedResponse.

        数据库用户总数。

        :return: The total_count of this ListPostgresqlDbUserPaginatedResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListPostgresqlDbUserPaginatedResponse.

        数据库用户总数。

        :param total_count: The total_count of this ListPostgresqlDbUserPaginatedResponse.
        :type: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListPostgresqlDbUserPaginatedResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
