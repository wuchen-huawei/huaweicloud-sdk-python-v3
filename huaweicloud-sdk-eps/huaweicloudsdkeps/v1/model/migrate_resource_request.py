# coding: utf-8

import pprint
import re

import six





class MigrateResourceRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'body': 'MigrateResource'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, body=None):
        """MigrateResourceRequest - a model defined in huaweicloud sdk"""
        
        

        self._enterprise_project_id = None
        self._body = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this MigrateResourceRequest.

        目标企业项目ID，enterprise_project_id为0时表示迁移资源到默认资源组default。

        :return: The enterprise_project_id of this MigrateResourceRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this MigrateResourceRequest.

        目标企业项目ID，enterprise_project_id为0时表示迁移资源到默认资源组default。

        :param enterprise_project_id: The enterprise_project_id of this MigrateResourceRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def body(self):
        """Gets the body of this MigrateResourceRequest.


        :return: The body of this MigrateResourceRequest.
        :rtype: MigrateResource
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this MigrateResourceRequest.


        :param body: The body of this MigrateResourceRequest.
        :type: MigrateResource
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
        if not isinstance(other, MigrateResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
