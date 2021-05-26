# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListSecretsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'secrets': 'list[Secret]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'secrets': 'secrets',
        'page_info': 'page_info'
    }

    def __init__(self, secrets=None, page_info=None):
        """ListSecretsResponse - a model defined in huaweicloud sdk"""
        
        super(ListSecretsResponse, self).__init__()

        self._secrets = None
        self._page_info = None
        self.discriminator = None

        if secrets is not None:
            self.secrets = secrets
        if page_info is not None:
            self.page_info = page_info

    @property
    def secrets(self):
        """Gets the secrets of this ListSecretsResponse.

        凭据详情列表。

        :return: The secrets of this ListSecretsResponse.
        :rtype: list[Secret]
        """
        return self._secrets

    @secrets.setter
    def secrets(self, secrets):
        """Sets the secrets of this ListSecretsResponse.

        凭据详情列表。

        :param secrets: The secrets of this ListSecretsResponse.
        :type: list[Secret]
        """
        self._secrets = secrets

    @property
    def page_info(self):
        """Gets the page_info of this ListSecretsResponse.


        :return: The page_info of this ListSecretsResponse.
        :rtype: PageInfo
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListSecretsResponse.


        :param page_info: The page_info of this ListSecretsResponse.
        :type: PageInfo
        """
        self._page_info = page_info

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
        if not isinstance(other, ListSecretsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
