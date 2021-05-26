# coding: utf-8

import pprint
import re

import six





class QosCpuInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'client_cpu_max': 'list[QosDataElement]',
        'system_cpu_max': 'list[QosDataElement]'
    }

    attribute_map = {
        'client_cpu_max': 'client_cpu_max',
        'system_cpu_max': 'system_cpu_max'
    }

    def __init__(self, client_cpu_max=None, system_cpu_max=None):
        """QosCpuInfo - a model defined in huaweicloud sdk"""
        
        

        self._client_cpu_max = None
        self._system_cpu_max = None
        self.discriminator = None

        if client_cpu_max is not None:
            self.client_cpu_max = client_cpu_max
        if system_cpu_max is not None:
            self.system_cpu_max = system_cpu_max

    @property
    def client_cpu_max(self):
        """Gets the client_cpu_max of this QosCpuInfo.

        华为云会议最大CPU使用率。

        :return: The client_cpu_max of this QosCpuInfo.
        :rtype: list[QosDataElement]
        """
        return self._client_cpu_max

    @client_cpu_max.setter
    def client_cpu_max(self, client_cpu_max):
        """Sets the client_cpu_max of this QosCpuInfo.

        华为云会议最大CPU使用率。

        :param client_cpu_max: The client_cpu_max of this QosCpuInfo.
        :type: list[QosDataElement]
        """
        self._client_cpu_max = client_cpu_max

    @property
    def system_cpu_max(self):
        """Gets the system_cpu_max of this QosCpuInfo.

        系统最大CPU使用率。

        :return: The system_cpu_max of this QosCpuInfo.
        :rtype: list[QosDataElement]
        """
        return self._system_cpu_max

    @system_cpu_max.setter
    def system_cpu_max(self, system_cpu_max):
        """Sets the system_cpu_max of this QosCpuInfo.

        系统最大CPU使用率。

        :param system_cpu_max: The system_cpu_max of this QosCpuInfo.
        :type: list[QosDataElement]
        """
        self._system_cpu_max = system_cpu_max

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
        if not isinstance(other, QosCpuInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
