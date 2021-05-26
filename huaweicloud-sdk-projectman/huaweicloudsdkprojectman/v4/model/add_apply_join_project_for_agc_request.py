# coding: utf-8

import pprint
import re

import six





class AddApplyJoinProjectForAgcRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'user_id': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'domain_id': 'Domain-Id',
        'user_id': 'User-Id',
        'project_id': 'project_id'
    }

    def __init__(self, domain_id=None, user_id=None, project_id=None):
        """AddApplyJoinProjectForAgcRequest - a model defined in huaweicloud sdk"""
        
        

        self._domain_id = None
        self._user_id = None
        self._project_id = None
        self.discriminator = None

        self.domain_id = domain_id
        self.user_id = user_id
        self.project_id = project_id

    @property
    def domain_id(self):
        """Gets the domain_id of this AddApplyJoinProjectForAgcRequest.

        租户id

        :return: The domain_id of this AddApplyJoinProjectForAgcRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this AddApplyJoinProjectForAgcRequest.

        租户id

        :param domain_id: The domain_id of this AddApplyJoinProjectForAgcRequest.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def user_id(self):
        """Gets the user_id of this AddApplyJoinProjectForAgcRequest.

        用户id

        :return: The user_id of this AddApplyJoinProjectForAgcRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AddApplyJoinProjectForAgcRequest.

        用户id

        :param user_id: The user_id of this AddApplyJoinProjectForAgcRequest.
        :type: str
        """
        self._user_id = user_id

    @property
    def project_id(self):
        """Gets the project_id of this AddApplyJoinProjectForAgcRequest.

        项目id

        :return: The project_id of this AddApplyJoinProjectForAgcRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AddApplyJoinProjectForAgcRequest.

        项目id

        :param project_id: The project_id of this AddApplyJoinProjectForAgcRequest.
        :type: str
        """
        self._project_id = project_id

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
        if not isinstance(other, AddApplyJoinProjectForAgcRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
