# coding: utf-8

import pprint
import re

import six





class Deployment:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'distribution': 'list[Distribution]',
        'edgecloud': 'DeploymentEdgecloud'
    }

    attribute_map = {
        'id': 'id',
        'distribution': 'distribution',
        'edgecloud': 'edgecloud'
    }

    def __init__(self, id=None, distribution=None, edgecloud=None):
        """Deployment - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._distribution = None
        self._edgecloud = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if distribution is not None:
            self.distribution = distribution
        if edgecloud is not None:
            self.edgecloud = edgecloud

    @property
    def id(self):
        """Gets the id of this Deployment.

        部署计划ID。

        :return: The id of this Deployment.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Deployment.

        部署计划ID。

        :param id: The id of this Deployment.
        :type: str
        """
        self._id = id

    @property
    def distribution(self):
        """Gets the distribution of this Deployment.

        部署位置信息列表

        :return: The distribution of this Deployment.
        :rtype: list[Distribution]
        """
        return self._distribution

    @distribution.setter
    def distribution(self, distribution):
        """Sets the distribution of this Deployment.

        部署位置信息列表

        :param distribution: The distribution of this Deployment.
        :type: list[Distribution]
        """
        self._distribution = distribution

    @property
    def edgecloud(self):
        """Gets the edgecloud of this Deployment.


        :return: The edgecloud of this Deployment.
        :rtype: DeploymentEdgecloud
        """
        return self._edgecloud

    @edgecloud.setter
    def edgecloud(self, edgecloud):
        """Sets the edgecloud of this Deployment.


        :param edgecloud: The edgecloud of this Deployment.
        :type: DeploymentEdgecloud
        """
        self._edgecloud = edgecloud

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
        if not isinstance(other, Deployment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
