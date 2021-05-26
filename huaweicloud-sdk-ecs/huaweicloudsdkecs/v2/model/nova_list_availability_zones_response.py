# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class NovaListAvailabilityZonesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'availability_zone_info': 'list[NovaAvailabilityZone]'
    }

    attribute_map = {
        'availability_zone_info': 'availabilityZoneInfo'
    }

    def __init__(self, availability_zone_info=None):
        """NovaListAvailabilityZonesResponse - a model defined in huaweicloud sdk"""
        
        super(NovaListAvailabilityZonesResponse, self).__init__()

        self._availability_zone_info = None
        self.discriminator = None

        if availability_zone_info is not None:
            self.availability_zone_info = availability_zone_info

    @property
    def availability_zone_info(self):
        """Gets the availability_zone_info of this NovaListAvailabilityZonesResponse.

        可用域信息。

        :return: The availability_zone_info of this NovaListAvailabilityZonesResponse.
        :rtype: list[NovaAvailabilityZone]
        """
        return self._availability_zone_info

    @availability_zone_info.setter
    def availability_zone_info(self, availability_zone_info):
        """Sets the availability_zone_info of this NovaListAvailabilityZonesResponse.

        可用域信息。

        :param availability_zone_info: The availability_zone_info of this NovaListAvailabilityZonesResponse.
        :type: list[NovaAvailabilityZone]
        """
        self._availability_zone_info = availability_zone_info

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
        if not isinstance(other, NovaListAvailabilityZonesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
