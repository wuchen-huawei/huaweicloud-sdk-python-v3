# coding: utf-8

import pprint
import re

import six





class DeploymentEdgecloud:


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
        'name': 'str',
        'stacks': 'Stack',
        'description': 'str',
        'coverage': 'Coverage'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'stacks': 'stacks',
        'description': 'description',
        'coverage': 'coverage'
    }

    def __init__(self, id=None, name=None, stacks=None, description=None, coverage=None):
        """DeploymentEdgecloud - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._stacks = None
        self._description = None
        self._coverage = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if stacks is not None:
            self.stacks = stacks
        if description is not None:
            self.description = description
        if coverage is not None:
            self.coverage = coverage

    @property
    def id(self):
        """Gets the id of this DeploymentEdgecloud.

        边缘业务ID。

        :return: The id of this DeploymentEdgecloud.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeploymentEdgecloud.

        边缘业务ID。

        :param id: The id of this DeploymentEdgecloud.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this DeploymentEdgecloud.

        边缘业务名称。

        :return: The name of this DeploymentEdgecloud.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeploymentEdgecloud.

        边缘业务名称。

        :param name: The name of this DeploymentEdgecloud.
        :type: str
        """
        self._name = name

    @property
    def stacks(self):
        """Gets the stacks of this DeploymentEdgecloud.


        :return: The stacks of this DeploymentEdgecloud.
        :rtype: Stack
        """
        return self._stacks

    @stacks.setter
    def stacks(self, stacks):
        """Sets the stacks of this DeploymentEdgecloud.


        :param stacks: The stacks of this DeploymentEdgecloud.
        :type: Stack
        """
        self._stacks = stacks

    @property
    def description(self):
        """Gets the description of this DeploymentEdgecloud.

        边缘业务描述，最大支持255字节。

        :return: The description of this DeploymentEdgecloud.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeploymentEdgecloud.

        边缘业务描述，最大支持255字节。

        :param description: The description of this DeploymentEdgecloud.
        :type: str
        """
        self._description = description

    @property
    def coverage(self):
        """Gets the coverage of this DeploymentEdgecloud.


        :return: The coverage of this DeploymentEdgecloud.
        :rtype: Coverage
        """
        return self._coverage

    @coverage.setter
    def coverage(self, coverage):
        """Sets the coverage of this DeploymentEdgecloud.


        :param coverage: The coverage of this DeploymentEdgecloud.
        :type: Coverage
        """
        self._coverage = coverage

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
        if not isinstance(other, DeploymentEdgecloud):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
