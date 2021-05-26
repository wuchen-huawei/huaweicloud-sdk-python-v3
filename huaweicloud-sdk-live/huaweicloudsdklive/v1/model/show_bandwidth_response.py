# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowBandwidthResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'bandwidth_info': 'list[BandwidthInfo]'
    }

    attribute_map = {
        'total': 'total',
        'bandwidth_info': 'bandwidth_info'
    }

    def __init__(self, total=None, bandwidth_info=None):
        """ShowBandwidthResponse - a model defined in huaweicloud sdk"""
        
        super(ShowBandwidthResponse, self).__init__()

        self._total = None
        self._bandwidth_info = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if bandwidth_info is not None:
            self.bandwidth_info = bandwidth_info

    @property
    def total(self):
        """Gets the total of this ShowBandwidthResponse.

        查询结果的总元素数量

        :return: The total of this ShowBandwidthResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowBandwidthResponse.

        查询结果的总元素数量

        :param total: The total of this ShowBandwidthResponse.
        :type: int
        """
        self._total = total

    @property
    def bandwidth_info(self):
        """Gets the bandwidth_info of this ShowBandwidthResponse.

        带宽信息

        :return: The bandwidth_info of this ShowBandwidthResponse.
        :rtype: list[BandwidthInfo]
        """
        return self._bandwidth_info

    @bandwidth_info.setter
    def bandwidth_info(self, bandwidth_info):
        """Sets the bandwidth_info of this ShowBandwidthResponse.

        带宽信息

        :param bandwidth_info: The bandwidth_info of this ShowBandwidthResponse.
        :type: list[BandwidthInfo]
        """
        self._bandwidth_info = bandwidth_info

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
        if not isinstance(other, ShowBandwidthResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
