# coding: utf-8

import pprint
import re

import six





class DeleteNatGatewayRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'nat_gateway_id': 'str'
    }

    attribute_map = {
        'nat_gateway_id': 'nat_gateway_id'
    }

    def __init__(self, nat_gateway_id=None):
        """DeleteNatGatewayRequest - a model defined in huaweicloud sdk"""
        
        

        self._nat_gateway_id = None
        self.discriminator = None

        self.nat_gateway_id = nat_gateway_id

    @property
    def nat_gateway_id(self):
        """Gets the nat_gateway_id of this DeleteNatGatewayRequest.

        公网NAT网关实例的ID。

        :return: The nat_gateway_id of this DeleteNatGatewayRequest.
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        """Sets the nat_gateway_id of this DeleteNatGatewayRequest.

        公网NAT网关实例的ID。

        :param nat_gateway_id: The nat_gateway_id of this DeleteNatGatewayRequest.
        :type: str
        """
        self._nat_gateway_id = nat_gateway_id

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
        if not isinstance(other, DeleteNatGatewayRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
