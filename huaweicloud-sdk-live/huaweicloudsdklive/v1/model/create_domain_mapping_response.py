# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateDomainMappingResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pull_domain': 'str',
        'push_domain': 'str'
    }

    attribute_map = {
        'pull_domain': 'pull_domain',
        'push_domain': 'push_domain'
    }

    def __init__(self, pull_domain=None, push_domain=None):
        """CreateDomainMappingResponse - a model defined in huaweicloud sdk"""
        
        super(CreateDomainMappingResponse, self).__init__()

        self._pull_domain = None
        self._push_domain = None
        self.discriminator = None

        if pull_domain is not None:
            self.pull_domain = pull_domain
        if push_domain is not None:
            self.push_domain = push_domain

    @property
    def pull_domain(self):
        """Gets the pull_domain of this CreateDomainMappingResponse.

        直播播放域名

        :return: The pull_domain of this CreateDomainMappingResponse.
        :rtype: str
        """
        return self._pull_domain

    @pull_domain.setter
    def pull_domain(self, pull_domain):
        """Sets the pull_domain of this CreateDomainMappingResponse.

        直播播放域名

        :param pull_domain: The pull_domain of this CreateDomainMappingResponse.
        :type: str
        """
        self._pull_domain = pull_domain

    @property
    def push_domain(self):
        """Gets the push_domain of this CreateDomainMappingResponse.

        直播播放域名关联的推流域名

        :return: The push_domain of this CreateDomainMappingResponse.
        :rtype: str
        """
        return self._push_domain

    @push_domain.setter
    def push_domain(self, push_domain):
        """Sets the push_domain of this CreateDomainMappingResponse.

        直播播放域名关联的推流域名

        :param push_domain: The push_domain of this CreateDomainMappingResponse.
        :type: str
        """
        self._push_domain = push_domain

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
        if not isinstance(other, CreateDomainMappingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
