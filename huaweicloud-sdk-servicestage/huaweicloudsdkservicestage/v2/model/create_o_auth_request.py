# coding: utf-8

import pprint
import re

import six





class CreateOAuthRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'repo_type': 'str',
        'tag': 'str',
        'body': 'OAuth'
    }

    attribute_map = {
        'repo_type': 'repo_type',
        'tag': 'tag',
        'body': 'body'
    }

    def __init__(self, repo_type=None, tag=None, body=None):
        """CreateOAuthRequest - a model defined in huaweicloud sdk"""
        
        

        self._repo_type = None
        self._tag = None
        self._body = None
        self.discriminator = None

        self.repo_type = repo_type
        if tag is not None:
            self.tag = tag
        if body is not None:
            self.body = body

    @property
    def repo_type(self):
        """Gets the repo_type of this CreateOAuthRequest.

        仓库类型。 支持OAuth授权的仓库类型有：github、gitlab、gitee、bitbucket。

        :return: The repo_type of this CreateOAuthRequest.
        :rtype: str
        """
        return self._repo_type

    @repo_type.setter
    def repo_type(self, repo_type):
        """Sets the repo_type of this CreateOAuthRequest.

        仓库类型。 支持OAuth授权的仓库类型有：github、gitlab、gitee、bitbucket。

        :param repo_type: The repo_type of this CreateOAuthRequest.
        :type: str
        """
        self._repo_type = repo_type

    @property
    def tag(self):
        """Gets the tag of this CreateOAuthRequest.

        站点标签。 比如国际站的，?tag=intl。 默认为空。

        :return: The tag of this CreateOAuthRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this CreateOAuthRequest.

        站点标签。 比如国际站的，?tag=intl。 默认为空。

        :param tag: The tag of this CreateOAuthRequest.
        :type: str
        """
        self._tag = tag

    @property
    def body(self):
        """Gets the body of this CreateOAuthRequest.


        :return: The body of this CreateOAuthRequest.
        :rtype: OAuth
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateOAuthRequest.


        :param body: The body of this CreateOAuthRequest.
        :type: OAuth
        """
        self._body = body

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
        if not isinstance(other, CreateOAuthRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
