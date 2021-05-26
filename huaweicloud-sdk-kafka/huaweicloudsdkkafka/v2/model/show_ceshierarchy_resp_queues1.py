# coding: utf-8

import pprint
import re

import six





class ShowCeshierarchyRespQueues1:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'partitions': 'list[ShowCeshierarchyRespPartitions]'
    }

    attribute_map = {
        'name': 'name',
        'partitions': 'partitions'
    }

    def __init__(self, name=None, partitions=None):
        """ShowCeshierarchyRespQueues1 - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._partitions = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if partitions is not None:
            self.partitions = partitions

    @property
    def name(self):
        """Gets the name of this ShowCeshierarchyRespQueues1.

        topic名称。

        :return: The name of this ShowCeshierarchyRespQueues1.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowCeshierarchyRespQueues1.

        topic名称。

        :param name: The name of this ShowCeshierarchyRespQueues1.
        :type: str
        """
        self._name = name

    @property
    def partitions(self):
        """Gets the partitions of this ShowCeshierarchyRespQueues1.

        分区信息。

        :return: The partitions of this ShowCeshierarchyRespQueues1.
        :rtype: list[ShowCeshierarchyRespPartitions]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """Sets the partitions of this ShowCeshierarchyRespQueues1.

        分区信息。

        :param partitions: The partitions of this ShowCeshierarchyRespQueues1.
        :type: list[ShowCeshierarchyRespPartitions]
        """
        self._partitions = partitions

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
        if not isinstance(other, ShowCeshierarchyRespQueues1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
