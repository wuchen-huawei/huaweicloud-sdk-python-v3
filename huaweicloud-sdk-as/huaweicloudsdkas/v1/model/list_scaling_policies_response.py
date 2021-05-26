# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListScalingPoliciesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total_number': 'int',
        'start_number': 'int',
        'limit': 'int',
        'scaling_policies': 'list[ScalingV1PolicyDetail]'
    }

    attribute_map = {
        'total_number': 'total_number',
        'start_number': 'start_number',
        'limit': 'limit',
        'scaling_policies': 'scaling_policies'
    }

    def __init__(self, total_number=None, start_number=None, limit=None, scaling_policies=None):
        """ListScalingPoliciesResponse - a model defined in huaweicloud sdk"""
        
        super(ListScalingPoliciesResponse, self).__init__()

        self._total_number = None
        self._start_number = None
        self._limit = None
        self._scaling_policies = None
        self.discriminator = None

        if total_number is not None:
            self.total_number = total_number
        if start_number is not None:
            self.start_number = start_number
        if limit is not None:
            self.limit = limit
        if scaling_policies is not None:
            self.scaling_policies = scaling_policies

    @property
    def total_number(self):
        """Gets the total_number of this ListScalingPoliciesResponse.

        总记录数。

        :return: The total_number of this ListScalingPoliciesResponse.
        :rtype: int
        """
        return self._total_number

    @total_number.setter
    def total_number(self, total_number):
        """Sets the total_number of this ListScalingPoliciesResponse.

        总记录数。

        :param total_number: The total_number of this ListScalingPoliciesResponse.
        :type: int
        """
        self._total_number = total_number

    @property
    def start_number(self):
        """Gets the start_number of this ListScalingPoliciesResponse.

        查询的起始行号。

        :return: The start_number of this ListScalingPoliciesResponse.
        :rtype: int
        """
        return self._start_number

    @start_number.setter
    def start_number(self, start_number):
        """Sets the start_number of this ListScalingPoliciesResponse.

        查询的起始行号。

        :param start_number: The start_number of this ListScalingPoliciesResponse.
        :type: int
        """
        self._start_number = start_number

    @property
    def limit(self):
        """Gets the limit of this ListScalingPoliciesResponse.

        查询记录数。

        :return: The limit of this ListScalingPoliciesResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListScalingPoliciesResponse.

        查询记录数。

        :param limit: The limit of this ListScalingPoliciesResponse.
        :type: int
        """
        self._limit = limit

    @property
    def scaling_policies(self):
        """Gets the scaling_policies of this ListScalingPoliciesResponse.

        伸缩策略列表

        :return: The scaling_policies of this ListScalingPoliciesResponse.
        :rtype: list[ScalingV1PolicyDetail]
        """
        return self._scaling_policies

    @scaling_policies.setter
    def scaling_policies(self, scaling_policies):
        """Sets the scaling_policies of this ListScalingPoliciesResponse.

        伸缩策略列表

        :param scaling_policies: The scaling_policies of this ListScalingPoliciesResponse.
        :type: list[ScalingV1PolicyDetail]
        """
        self._scaling_policies = scaling_policies

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
        if not isinstance(other, ListScalingPoliciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
