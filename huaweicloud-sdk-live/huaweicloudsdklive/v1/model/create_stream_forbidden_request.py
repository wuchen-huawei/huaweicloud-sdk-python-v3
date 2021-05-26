# coding: utf-8

import pprint
import re

import six





class CreateStreamForbiddenRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'specify_project': 'str',
        'body': 'StreamForbiddenSetting'
    }

    attribute_map = {
        'specify_project': 'specify_project',
        'body': 'body'
    }

    def __init__(self, specify_project=None, body=None):
        """CreateStreamForbiddenRequest - a model defined in huaweicloud sdk"""
        
        

        self._specify_project = None
        self._body = None
        self.discriminator = None

        if specify_project is not None:
            self.specify_project = specify_project
        if body is not None:
            self.body = body

    @property
    def specify_project(self):
        """Gets the specify_project of this CreateStreamForbiddenRequest.

        op账号需要携带的特定project_id，当使用op账号时该值为所操作租户的project_id

        :return: The specify_project of this CreateStreamForbiddenRequest.
        :rtype: str
        """
        return self._specify_project

    @specify_project.setter
    def specify_project(self, specify_project):
        """Sets the specify_project of this CreateStreamForbiddenRequest.

        op账号需要携带的特定project_id，当使用op账号时该值为所操作租户的project_id

        :param specify_project: The specify_project of this CreateStreamForbiddenRequest.
        :type: str
        """
        self._specify_project = specify_project

    @property
    def body(self):
        """Gets the body of this CreateStreamForbiddenRequest.


        :return: The body of this CreateStreamForbiddenRequest.
        :rtype: StreamForbiddenSetting
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateStreamForbiddenRequest.


        :param body: The body of this CreateStreamForbiddenRequest.
        :type: StreamForbiddenSetting
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
        if not isinstance(other, CreateStreamForbiddenRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
