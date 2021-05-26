# coding: utf-8

import pprint
import re

import six





class CreateInstanceBy3rdRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_label': 'str',
        'body': 'InstanceEdgeParam'
    }

    attribute_map = {
        'instance_label': 'instance_label',
        'body': 'body'
    }

    def __init__(self, instance_label=None, body=None):
        """CreateInstanceBy3rdRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_label = None
        self._body = None
        self.discriminator = None

        if instance_label is not None:
            self.instance_label = instance_label
        if body is not None:
            self.body = body

    @property
    def instance_label(self):
        """Gets the instance_label of this CreateInstanceBy3rdRequest.

        实例标签（不同的第三方需要和CloudIDE服务共同设定标签）。不传默认为classroom

        :return: The instance_label of this CreateInstanceBy3rdRequest.
        :rtype: str
        """
        return self._instance_label

    @instance_label.setter
    def instance_label(self, instance_label):
        """Sets the instance_label of this CreateInstanceBy3rdRequest.

        实例标签（不同的第三方需要和CloudIDE服务共同设定标签）。不传默认为classroom

        :param instance_label: The instance_label of this CreateInstanceBy3rdRequest.
        :type: str
        """
        self._instance_label = instance_label

    @property
    def body(self):
        """Gets the body of this CreateInstanceBy3rdRequest.


        :return: The body of this CreateInstanceBy3rdRequest.
        :rtype: InstanceEdgeParam
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateInstanceBy3rdRequest.


        :param body: The body of this CreateInstanceBy3rdRequest.
        :type: InstanceEdgeParam
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
        if not isinstance(other, CreateInstanceBy3rdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
