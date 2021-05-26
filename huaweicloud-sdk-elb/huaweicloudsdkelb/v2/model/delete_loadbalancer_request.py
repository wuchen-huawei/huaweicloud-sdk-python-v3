# coding: utf-8

import pprint
import re

import six





class DeleteLoadbalancerRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'loadbalancer_id': 'str',
        'cascade': 'bool'
    }

    attribute_map = {
        'loadbalancer_id': 'loadbalancer_id',
        'cascade': 'cascade'
    }

    def __init__(self, loadbalancer_id=None, cascade=None):
        """DeleteLoadbalancerRequest - a model defined in huaweicloud sdk"""
        
        

        self._loadbalancer_id = None
        self._cascade = None
        self.discriminator = None

        self.loadbalancer_id = loadbalancer_id
        if cascade is not None:
            self.cascade = cascade

    @property
    def loadbalancer_id(self):
        """Gets the loadbalancer_id of this DeleteLoadbalancerRequest.

        负载均衡器id

        :return: The loadbalancer_id of this DeleteLoadbalancerRequest.
        :rtype: str
        """
        return self._loadbalancer_id

    @loadbalancer_id.setter
    def loadbalancer_id(self, loadbalancer_id):
        """Sets the loadbalancer_id of this DeleteLoadbalancerRequest.

        负载均衡器id

        :param loadbalancer_id: The loadbalancer_id of this DeleteLoadbalancerRequest.
        :type: str
        """
        self._loadbalancer_id = loadbalancer_id

    @property
    def cascade(self):
        """Gets the cascade of this DeleteLoadbalancerRequest.

        （不再支持）级联删除负载均衡器

        :return: The cascade of this DeleteLoadbalancerRequest.
        :rtype: bool
        """
        return self._cascade

    @cascade.setter
    def cascade(self, cascade):
        """Sets the cascade of this DeleteLoadbalancerRequest.

        （不再支持）级联删除负载均衡器

        :param cascade: The cascade of this DeleteLoadbalancerRequest.
        :type: bool
        """
        self._cascade = cascade

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
        if not isinstance(other, DeleteLoadbalancerRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
