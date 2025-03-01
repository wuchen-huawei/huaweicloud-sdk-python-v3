# coding: utf-8

import pprint
import re

import six





class ShowAccessDomainRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'repository': 'str',
        'access_domain': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'repository': 'repository',
        'access_domain': 'access_domain'
    }

    def __init__(self, namespace=None, repository=None, access_domain=None):
        """ShowAccessDomainRequest - a model defined in huaweicloud sdk"""
        
        

        self._namespace = None
        self._repository = None
        self._access_domain = None
        self.discriminator = None

        self.namespace = namespace
        self.repository = repository
        self.access_domain = access_domain

    @property
    def namespace(self):
        """Gets the namespace of this ShowAccessDomainRequest.

        组织名称

        :return: The namespace of this ShowAccessDomainRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ShowAccessDomainRequest.

        组织名称

        :param namespace: The namespace of this ShowAccessDomainRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        """Gets the repository of this ShowAccessDomainRequest.

        镜像仓库名称

        :return: The repository of this ShowAccessDomainRequest.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this ShowAccessDomainRequest.

        镜像仓库名称

        :param repository: The repository of this ShowAccessDomainRequest.
        :type: str
        """
        self._repository = repository

    @property
    def access_domain(self):
        """Gets the access_domain of this ShowAccessDomainRequest.

        共享账号

        :return: The access_domain of this ShowAccessDomainRequest.
        :rtype: str
        """
        return self._access_domain

    @access_domain.setter
    def access_domain(self, access_domain):
        """Sets the access_domain of this ShowAccessDomainRequest.

        共享账号

        :param access_domain: The access_domain of this ShowAccessDomainRequest.
        :type: str
        """
        self._access_domain = access_domain

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
        if not isinstance(other, ShowAccessDomainRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
