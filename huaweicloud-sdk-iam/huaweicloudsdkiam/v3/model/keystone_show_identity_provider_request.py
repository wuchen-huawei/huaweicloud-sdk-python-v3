# coding: utf-8

import pprint
import re

import six





class KeystoneShowIdentityProviderRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str'
    }

    attribute_map = {
        'id': 'id'
    }

    def __init__(self, id=None):
        """KeystoneShowIdentityProviderRequest - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self.discriminator = None

        self.id = id

    @property
    def id(self):
        """Gets the id of this KeystoneShowIdentityProviderRequest.

        待查询的身份提供商ID。

        :return: The id of this KeystoneShowIdentityProviderRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KeystoneShowIdentityProviderRequest.

        待查询的身份提供商ID。

        :param id: The id of this KeystoneShowIdentityProviderRequest.
        :type: str
        """
        self._id = id

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
        if not isinstance(other, KeystoneShowIdentityProviderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
