# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class KeystoneListProjectsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'links': 'Links',
        'projects': 'list[ProjectResult]'
    }

    attribute_map = {
        'links': 'links',
        'projects': 'projects'
    }

    def __init__(self, links=None, projects=None):
        """KeystoneListProjectsResponse - a model defined in huaweicloud sdk"""
        
        super(KeystoneListProjectsResponse, self).__init__()

        self._links = None
        self._projects = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if projects is not None:
            self.projects = projects

    @property
    def links(self):
        """Gets the links of this KeystoneListProjectsResponse.


        :return: The links of this KeystoneListProjectsResponse.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this KeystoneListProjectsResponse.


        :param links: The links of this KeystoneListProjectsResponse.
        :type: Links
        """
        self._links = links

    @property
    def projects(self):
        """Gets the projects of this KeystoneListProjectsResponse.

        项目信息列表。

        :return: The projects of this KeystoneListProjectsResponse.
        :rtype: list[ProjectResult]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this KeystoneListProjectsResponse.

        项目信息列表。

        :param projects: The projects of this KeystoneListProjectsResponse.
        :type: list[ProjectResult]
        """
        self._projects = projects

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
        if not isinstance(other, KeystoneListProjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
