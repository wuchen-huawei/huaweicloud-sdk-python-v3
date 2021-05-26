# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowScalingPolicyResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_policy': 'ScalingV1PolicyDetail'
    }

    attribute_map = {
        'scaling_policy': 'scaling_policy'
    }

    def __init__(self, scaling_policy=None):
        """ShowScalingPolicyResponse - a model defined in huaweicloud sdk"""
        
        super(ShowScalingPolicyResponse, self).__init__()

        self._scaling_policy = None
        self.discriminator = None

        if scaling_policy is not None:
            self.scaling_policy = scaling_policy

    @property
    def scaling_policy(self):
        """Gets the scaling_policy of this ShowScalingPolicyResponse.


        :return: The scaling_policy of this ShowScalingPolicyResponse.
        :rtype: ScalingV1PolicyDetail
        """
        return self._scaling_policy

    @scaling_policy.setter
    def scaling_policy(self, scaling_policy):
        """Sets the scaling_policy of this ShowScalingPolicyResponse.


        :param scaling_policy: The scaling_policy of this ShowScalingPolicyResponse.
        :type: ScalingV1PolicyDetail
        """
        self._scaling_policy = scaling_policy

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
        if not isinstance(other, ShowScalingPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
