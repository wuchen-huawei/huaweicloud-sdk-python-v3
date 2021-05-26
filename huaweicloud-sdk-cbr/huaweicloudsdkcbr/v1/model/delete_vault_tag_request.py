# coding: utf-8

import pprint
import re

import six





class DeleteVaultTagRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'vault_id': 'str'
    }

    attribute_map = {
        'key': 'key',
        'vault_id': 'vault_id'
    }

    def __init__(self, key=None, vault_id=None):
        """DeleteVaultTagRequest - a model defined in huaweicloud sdk"""
        
        

        self._key = None
        self._vault_id = None
        self.discriminator = None

        self.key = key
        self.vault_id = vault_id

    @property
    def key(self):
        """Gets the key of this DeleteVaultTagRequest.

        不能为空或空字符串，不检查长度和字符集，去掉key前后的空格后检查，去掉key前后的空格后使用。 即使底层存在非法的tag也要能删。

        :return: The key of this DeleteVaultTagRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DeleteVaultTagRequest.

        不能为空或空字符串，不检查长度和字符集，去掉key前后的空格后检查，去掉key前后的空格后使用。 即使底层存在非法的tag也要能删。

        :param key: The key of this DeleteVaultTagRequest.
        :type: str
        """
        self._key = key

    @property
    def vault_id(self):
        """Gets the vault_id of this DeleteVaultTagRequest.

        资源id

        :return: The vault_id of this DeleteVaultTagRequest.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this DeleteVaultTagRequest.

        资源id

        :param vault_id: The vault_id of this DeleteVaultTagRequest.
        :type: str
        """
        self._vault_id = vault_id

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
        if not isinstance(other, DeleteVaultTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
