# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowNamespaceAuthResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'creator_name': 'str',
        'self_auth': 'UserAuth',
        'others_auths': 'list[UserAuth]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'creator_name': 'creator_name',
        'self_auth': 'self_auth',
        'others_auths': 'others_auths'
    }

    def __init__(self, id=None, name=None, creator_name=None, self_auth=None, others_auths=None):
        """ShowNamespaceAuthResponse - a model defined in huaweicloud sdk"""
        
        super(ShowNamespaceAuthResponse, self).__init__()

        self._id = None
        self._name = None
        self._creator_name = None
        self._self_auth = None
        self._others_auths = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if creator_name is not None:
            self.creator_name = creator_name
        if self_auth is not None:
            self.self_auth = self_auth
        if others_auths is not None:
            self.others_auths = others_auths

    @property
    def id(self):
        """Gets the id of this ShowNamespaceAuthResponse.

        id

        :return: The id of this ShowNamespaceAuthResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowNamespaceAuthResponse.

        id

        :param id: The id of this ShowNamespaceAuthResponse.
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowNamespaceAuthResponse.

        组织名称

        :return: The name of this ShowNamespaceAuthResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowNamespaceAuthResponse.

        组织名称

        :param name: The name of this ShowNamespaceAuthResponse.
        :type: str
        """
        self._name = name

    @property
    def creator_name(self):
        """Gets the creator_name of this ShowNamespaceAuthResponse.

        组织创建者

        :return: The creator_name of this ShowNamespaceAuthResponse.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this ShowNamespaceAuthResponse.

        组织创建者

        :param creator_name: The creator_name of this ShowNamespaceAuthResponse.
        :type: str
        """
        self._creator_name = creator_name

    @property
    def self_auth(self):
        """Gets the self_auth of this ShowNamespaceAuthResponse.


        :return: The self_auth of this ShowNamespaceAuthResponse.
        :rtype: UserAuth
        """
        return self._self_auth

    @self_auth.setter
    def self_auth(self, self_auth):
        """Sets the self_auth of this ShowNamespaceAuthResponse.


        :param self_auth: The self_auth of this ShowNamespaceAuthResponse.
        :type: UserAuth
        """
        self._self_auth = self_auth

    @property
    def others_auths(self):
        """Gets the others_auths of this ShowNamespaceAuthResponse.

        其他用户的权限

        :return: The others_auths of this ShowNamespaceAuthResponse.
        :rtype: list[UserAuth]
        """
        return self._others_auths

    @others_auths.setter
    def others_auths(self, others_auths):
        """Sets the others_auths of this ShowNamespaceAuthResponse.

        其他用户的权限

        :param others_auths: The others_auths of this ShowNamespaceAuthResponse.
        :type: list[UserAuth]
        """
        self._others_auths = others_auths

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
        if not isinstance(other, ShowNamespaceAuthResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
