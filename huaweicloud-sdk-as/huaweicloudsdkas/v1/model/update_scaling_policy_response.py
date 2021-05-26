# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdateScalingPolicyResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_policy_id': 'str'
    }

    attribute_map = {
        'scaling_policy_id': 'scaling_policy_id'
    }

    def __init__(self, scaling_policy_id=None):
        """UpdateScalingPolicyResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateScalingPolicyResponse, self).__init__()

        self._scaling_policy_id = None
        self.discriminator = None

        if scaling_policy_id is not None:
            self.scaling_policy_id = scaling_policy_id

    @property
    def scaling_policy_id(self):
        """Gets the scaling_policy_id of this UpdateScalingPolicyResponse.

        伸缩策略ID。

        :return: The scaling_policy_id of this UpdateScalingPolicyResponse.
        :rtype: str
        """
        return self._scaling_policy_id

    @scaling_policy_id.setter
    def scaling_policy_id(self, scaling_policy_id):
        """Sets the scaling_policy_id of this UpdateScalingPolicyResponse.

        伸缩策略ID。

        :param scaling_policy_id: The scaling_policy_id of this UpdateScalingPolicyResponse.
        :type: str
        """
        self._scaling_policy_id = scaling_policy_id

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
        if not isinstance(other, UpdateScalingPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
