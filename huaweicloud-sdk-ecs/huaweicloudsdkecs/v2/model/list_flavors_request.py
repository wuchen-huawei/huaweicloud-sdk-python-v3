# coding: utf-8

import pprint
import re

import six





class ListFlavorsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'availability_zone': 'str'
    }

    attribute_map = {
        'availability_zone': 'availability_zone'
    }

    def __init__(self, availability_zone=None):
        """ListFlavorsRequest - a model defined in huaweicloud sdk"""
        
        

        self._availability_zone = None
        self.discriminator = None

        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ListFlavorsRequest.

        可用区，需要指定可用区（AZ）的名称或者ID或者code。

        :return: The availability_zone of this ListFlavorsRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ListFlavorsRequest.

        可用区，需要指定可用区（AZ）的名称或者ID或者code。

        :param availability_zone: The availability_zone of this ListFlavorsRequest.
        :type: str
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, ListFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
