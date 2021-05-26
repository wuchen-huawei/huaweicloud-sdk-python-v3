# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowReplicationCapabilitiesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'regions': 'list[ProtectableReplicationCapabilitiesRespRegion]'
    }

    attribute_map = {
        'regions': 'regions'
    }

    def __init__(self, regions=None):
        """ShowReplicationCapabilitiesResponse - a model defined in huaweicloud sdk"""
        
        super(ShowReplicationCapabilitiesResponse, self).__init__()

        self._regions = None
        self.discriminator = None

        if regions is not None:
            self.regions = regions

    @property
    def regions(self):
        """Gets the regions of this ShowReplicationCapabilitiesResponse.

        支持复制的区域列表

        :return: The regions of this ShowReplicationCapabilitiesResponse.
        :rtype: list[ProtectableReplicationCapabilitiesRespRegion]
        """
        return self._regions

    @regions.setter
    def regions(self, regions):
        """Sets the regions of this ShowReplicationCapabilitiesResponse.

        支持复制的区域列表

        :param regions: The regions of this ShowReplicationCapabilitiesResponse.
        :type: list[ProtectableReplicationCapabilitiesRespRegion]
        """
        self._regions = regions

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
        if not isinstance(other, ShowReplicationCapabilitiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
