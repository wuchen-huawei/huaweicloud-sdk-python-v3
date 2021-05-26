# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdateNatGatewaySnatRuleResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'snat_rule': 'NatGatewaySnatRuleResponseBody'
    }

    attribute_map = {
        'snat_rule': 'snat_rule'
    }

    def __init__(self, snat_rule=None):
        """UpdateNatGatewaySnatRuleResponse - a model defined in huaweicloud sdk"""
        
        super(UpdateNatGatewaySnatRuleResponse, self).__init__()

        self._snat_rule = None
        self.discriminator = None

        if snat_rule is not None:
            self.snat_rule = snat_rule

    @property
    def snat_rule(self):
        """Gets the snat_rule of this UpdateNatGatewaySnatRuleResponse.


        :return: The snat_rule of this UpdateNatGatewaySnatRuleResponse.
        :rtype: NatGatewaySnatRuleResponseBody
        """
        return self._snat_rule

    @snat_rule.setter
    def snat_rule(self, snat_rule):
        """Sets the snat_rule of this UpdateNatGatewaySnatRuleResponse.


        :param snat_rule: The snat_rule of this UpdateNatGatewaySnatRuleResponse.
        :type: NatGatewaySnatRuleResponseBody
        """
        self._snat_rule = snat_rule

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
        if not isinstance(other, UpdateNatGatewaySnatRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
