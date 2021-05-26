# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListFlavorsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'flavors': 'list[Flavor]'
    }

    attribute_map = {
        'count': 'count',
        'flavors': 'flavors'
    }

    def __init__(self, count=None, flavors=None):
        """ListFlavorsResponse - a model defined in huaweicloud sdk"""
        
        super(ListFlavorsResponse, self).__init__()

        self._count = None
        self._flavors = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if flavors is not None:
            self.flavors = flavors

    @property
    def count(self):
        """Gets the count of this ListFlavorsResponse.

        边缘实例规格数量。

        :return: The count of this ListFlavorsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListFlavorsResponse.

        边缘实例规格数量。

        :param count: The count of this ListFlavorsResponse.
        :type: int
        """
        self._count = count

    @property
    def flavors(self):
        """Gets the flavors of this ListFlavorsResponse.

        规格列表。

        :return: The flavors of this ListFlavorsResponse.
        :rtype: list[Flavor]
        """
        return self._flavors

    @flavors.setter
    def flavors(self, flavors):
        """Sets the flavors of this ListFlavorsResponse.

        规格列表。

        :param flavors: The flavors of this ListFlavorsResponse.
        :type: list[Flavor]
        """
        self._flavors = flavors

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
        if not isinstance(other, ListFlavorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
