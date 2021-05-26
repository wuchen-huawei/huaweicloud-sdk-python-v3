# coding: utf-8

import pprint
import re

import six





class BandwidthPolicyDto:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'end': 'str',
        'max_bandwidth': 'int',
        'start': 'str'
    }

    attribute_map = {
        'end': 'end',
        'max_bandwidth': 'max_bandwidth',
        'start': 'start'
    }

    def __init__(self, end=None, max_bandwidth=None, start=None):
        """BandwidthPolicyDto - a model defined in huaweicloud sdk"""
        
        

        self._end = None
        self._max_bandwidth = None
        self._start = None
        self.discriminator = None

        self.end = end
        self.max_bandwidth = max_bandwidth
        self.start = start

    @property
    def end(self):
        """Gets the end of this BandwidthPolicyDto.

        流量控制开始时间（包含），格式为“hh:mm”。例如“12:03”表示12时03分。

        :return: The end of this BandwidthPolicyDto.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this BandwidthPolicyDto.

        流量控制开始时间（包含），格式为“hh:mm”。例如“12:03”表示12时03分。

        :param end: The end of this BandwidthPolicyDto.
        :type: str
        """
        self._end = end

    @property
    def max_bandwidth(self):
        """Gets the max_bandwidth of this BandwidthPolicyDto.

        时段内允许的最大流量带宽，单位Byte/s，取值范围为>= 1048576Byte/s（相当于1MB/s）且<=209715200Byte/s（相当于200MB/s）。

        :return: The max_bandwidth of this BandwidthPolicyDto.
        :rtype: int
        """
        return self._max_bandwidth

    @max_bandwidth.setter
    def max_bandwidth(self, max_bandwidth):
        """Sets the max_bandwidth of this BandwidthPolicyDto.

        时段内允许的最大流量带宽，单位Byte/s，取值范围为>= 1048576Byte/s（相当于1MB/s）且<=209715200Byte/s（相当于200MB/s）。

        :param max_bandwidth: The max_bandwidth of this BandwidthPolicyDto.
        :type: int
        """
        self._max_bandwidth = max_bandwidth

    @property
    def start(self):
        """Gets the start of this BandwidthPolicyDto.

        流量控制开始时间（包含），格式为“hh:mm”。例如“12:03”表示12时03分。

        :return: The start of this BandwidthPolicyDto.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this BandwidthPolicyDto.

        流量控制开始时间（包含），格式为“hh:mm”。例如“12:03”表示12时03分。

        :param start: The start of this BandwidthPolicyDto.
        :type: str
        """
        self._start = start

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
        if not isinstance(other, BandwidthPolicyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
