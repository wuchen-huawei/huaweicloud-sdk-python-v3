# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListApisBindedToAppV2Response(SdkResponse):


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
        'size': 'int',
        'auths': 'list[AppAuthBindedApiResp]'
    }

    attribute_map = {
        'total': 'total',
        'size': 'size',
        'auths': 'auths'
    }

    def __init__(self, total=None, size=None, auths=None):
        """ListApisBindedToAppV2Response - a model defined in huaweicloud sdk"""
        
        super(ListApisBindedToAppV2Response, self).__init__()

        self._total = None
        self._size = None
        self._auths = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if auths is not None:
            self.auths = auths

    @property
    def total(self):
        """Gets the total of this ListApisBindedToAppV2Response.

        符合条件的API总数

        :return: The total of this ListApisBindedToAppV2Response.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListApisBindedToAppV2Response.

        符合条件的API总数

        :param total: The total of this ListApisBindedToAppV2Response.
        :type: int
        """
        self._total = total

    @property
    def size(self):
        """Gets the size of this ListApisBindedToAppV2Response.

        本次返回的列表长度

        :return: The size of this ListApisBindedToAppV2Response.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListApisBindedToAppV2Response.

        本次返回的列表长度

        :param size: The size of this ListApisBindedToAppV2Response.
        :type: int
        """
        self._size = size

    @property
    def auths(self):
        """Gets the auths of this ListApisBindedToAppV2Response.

        本次返回的API列表

        :return: The auths of this ListApisBindedToAppV2Response.
        :rtype: list[AppAuthBindedApiResp]
        """
        return self._auths

    @auths.setter
    def auths(self, auths):
        """Sets the auths of this ListApisBindedToAppV2Response.

        本次返回的API列表

        :param auths: The auths of this ListApisBindedToAppV2Response.
        :type: list[AppAuthBindedApiResp]
        """
        self._auths = auths

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
        if not isinstance(other, ListApisBindedToAppV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
