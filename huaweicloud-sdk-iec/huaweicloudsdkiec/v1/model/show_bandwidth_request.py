# coding: utf-8

import pprint
import re

import six





class ShowBandwidthRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bandwidth_id': 'str'
    }

    attribute_map = {
        'bandwidth_id': 'bandwidth_id'
    }

    def __init__(self, bandwidth_id=None):
        """ShowBandwidthRequest - a model defined in huaweicloud sdk"""
        
        

        self._bandwidth_id = None
        self.discriminator = None

        self.bandwidth_id = bandwidth_id

    @property
    def bandwidth_id(self):
        """Gets the bandwidth_id of this ShowBandwidthRequest.

        带宽ID。

        :return: The bandwidth_id of this ShowBandwidthRequest.
        :rtype: str
        """
        return self._bandwidth_id

    @bandwidth_id.setter
    def bandwidth_id(self, bandwidth_id):
        """Sets the bandwidth_id of this ShowBandwidthRequest.

        带宽ID。

        :param bandwidth_id: The bandwidth_id of this ShowBandwidthRequest.
        :type: str
        """
        self._bandwidth_id = bandwidth_id

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
        if not isinstance(other, ShowBandwidthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
