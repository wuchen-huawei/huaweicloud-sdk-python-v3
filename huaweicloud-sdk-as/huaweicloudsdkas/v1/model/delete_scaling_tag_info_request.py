# coding: utf-8

import pprint
import re

import six





class DeleteScalingTagInfoRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'resource_id': 'str',
        'body': 'DeleteTagsOption'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'body': 'body'
    }

    def __init__(self, resource_type=None, resource_id=None, body=None):
        """DeleteScalingTagInfoRequest - a model defined in huaweicloud sdk"""
        
        

        self._resource_type = None
        self._resource_id = None
        self._body = None
        self.discriminator = None

        self.resource_type = resource_type
        self.resource_id = resource_id
        if body is not None:
            self.body = body

    @property
    def resource_type(self):
        """Gets the resource_type of this DeleteScalingTagInfoRequest.

        资源类型，枚举类：scaling_group_tag。scaling_group_tag表示资源类型为伸缩组。

        :return: The resource_type of this DeleteScalingTagInfoRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this DeleteScalingTagInfoRequest.

        资源类型，枚举类：scaling_group_tag。scaling_group_tag表示资源类型为伸缩组。

        :param resource_type: The resource_type of this DeleteScalingTagInfoRequest.
        :type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this DeleteScalingTagInfoRequest.

        资源ID。

        :return: The resource_id of this DeleteScalingTagInfoRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this DeleteScalingTagInfoRequest.

        资源ID。

        :param resource_id: The resource_id of this DeleteScalingTagInfoRequest.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def body(self):
        """Gets the body of this DeleteScalingTagInfoRequest.


        :return: The body of this DeleteScalingTagInfoRequest.
        :rtype: DeleteTagsOption
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DeleteScalingTagInfoRequest.


        :param body: The body of this DeleteScalingTagInfoRequest.
        :type: DeleteTagsOption
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
        if not isinstance(other, DeleteScalingTagInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
