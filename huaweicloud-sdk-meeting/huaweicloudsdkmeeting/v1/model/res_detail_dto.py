# coding: utf-8

import pprint
import re

import six





class ResDetailDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sum_count': 'int',
        'trial_count': 'int',
        'expired_count': 'int',
        'expiring_count': 'int',
        'used_count': 'int'
    }

    attribute_map = {
        'sum_count': 'sumCount',
        'trial_count': 'trialCount',
        'expired_count': 'expiredCount',
        'expiring_count': 'expiringCount',
        'used_count': 'usedCount'
    }

    def __init__(self, sum_count=None, trial_count=None, expired_count=None, expiring_count=None, used_count=None):
        """ResDetailDTO - a model defined in huaweicloud sdk"""
        
        

        self._sum_count = None
        self._trial_count = None
        self._expired_count = None
        self._expiring_count = None
        self._used_count = None
        self.discriminator = None

        if sum_count is not None:
            self.sum_count = sum_count
        if trial_count is not None:
            self.trial_count = trial_count
        if expired_count is not None:
            self.expired_count = expired_count
        if expiring_count is not None:
            self.expiring_count = expiring_count
        if used_count is not None:
            self.used_count = used_count

    @property
    def sum_count(self):
        """Gets the sum_count of this ResDetailDTO.

        总数

        :return: The sum_count of this ResDetailDTO.
        :rtype: int
        """
        return self._sum_count

    @sum_count.setter
    def sum_count(self, sum_count):
        """Sets the sum_count of this ResDetailDTO.

        总数

        :param sum_count: The sum_count of this ResDetailDTO.
        :type: int
        """
        self._sum_count = sum_count

    @property
    def trial_count(self):
        """Gets the trial_count of this ResDetailDTO.

        赠送数量

        :return: The trial_count of this ResDetailDTO.
        :rtype: int
        """
        return self._trial_count

    @trial_count.setter
    def trial_count(self, trial_count):
        """Sets the trial_count of this ResDetailDTO.

        赠送数量

        :param trial_count: The trial_count of this ResDetailDTO.
        :type: int
        """
        self._trial_count = trial_count

    @property
    def expired_count(self):
        """Gets the expired_count of this ResDetailDTO.

        到期数量

        :return: The expired_count of this ResDetailDTO.
        :rtype: int
        """
        return self._expired_count

    @expired_count.setter
    def expired_count(self, expired_count):
        """Sets the expired_count of this ResDetailDTO.

        到期数量

        :param expired_count: The expired_count of this ResDetailDTO.
        :type: int
        """
        self._expired_count = expired_count

    @property
    def expiring_count(self):
        """Gets the expiring_count of this ResDetailDTO.

        即将到期数量，到期时间在30天内

        :return: The expiring_count of this ResDetailDTO.
        :rtype: int
        """
        return self._expiring_count

    @expiring_count.setter
    def expiring_count(self, expiring_count):
        """Sets the expiring_count of this ResDetailDTO.

        即将到期数量，到期时间在30天内

        :param expiring_count: The expiring_count of this ResDetailDTO.
        :type: int
        """
        self._expiring_count = expiring_count

    @property
    def used_count(self):
        """Gets the used_count of this ResDetailDTO.

        已使用数（录播存储空间、会议并发、推流并发方数暂无法查询）。

        :return: The used_count of this ResDetailDTO.
        :rtype: int
        """
        return self._used_count

    @used_count.setter
    def used_count(self, used_count):
        """Sets the used_count of this ResDetailDTO.

        已使用数（录播存储空间、会议并发、推流并发方数暂无法查询）。

        :param used_count: The used_count of this ResDetailDTO.
        :type: int
        """
        self._used_count = used_count

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
        if not isinstance(other, ResDetailDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
