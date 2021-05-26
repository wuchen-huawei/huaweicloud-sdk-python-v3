# coding: utf-8

import pprint
import re

import six





class DeleteScalingNotificationRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_group_id': 'str',
        'topic_urn': 'str'
    }

    attribute_map = {
        'scaling_group_id': 'scaling_group_id',
        'topic_urn': 'topic_urn'
    }

    def __init__(self, scaling_group_id=None, topic_urn=None):
        """DeleteScalingNotificationRequest - a model defined in huaweicloud sdk"""
        
        

        self._scaling_group_id = None
        self._topic_urn = None
        self.discriminator = None

        self.scaling_group_id = scaling_group_id
        self.topic_urn = topic_urn

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this DeleteScalingNotificationRequest.

        伸缩组标识。

        :return: The scaling_group_id of this DeleteScalingNotificationRequest.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this DeleteScalingNotificationRequest.

        伸缩组标识。

        :param scaling_group_id: The scaling_group_id of this DeleteScalingNotificationRequest.
        :type: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def topic_urn(self):
        """Gets the topic_urn of this DeleteScalingNotificationRequest.

        SMN服务中Topic的唯一的资源标识。

        :return: The topic_urn of this DeleteScalingNotificationRequest.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this DeleteScalingNotificationRequest.

        SMN服务中Topic的唯一的资源标识。

        :param topic_urn: The topic_urn of this DeleteScalingNotificationRequest.
        :type: str
        """
        self._topic_urn = topic_urn

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
        if not isinstance(other, DeleteScalingNotificationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
