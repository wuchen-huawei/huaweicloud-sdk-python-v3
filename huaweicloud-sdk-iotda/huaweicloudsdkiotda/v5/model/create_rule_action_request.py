# coding: utf-8

import pprint
import re

import six





class CreateRuleActionRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'x_lb_service': 'str',
        'body': 'AddActionReq'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'x_lb_service': 'x-LB-Service',
        'body': 'body'
    }

    def __init__(self, instance_id=None, x_lb_service=None, body=None):
        """CreateRuleActionRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._x_lb_service = None
        self._body = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if x_lb_service is not None:
            self.x_lb_service = x_lb_service
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this CreateRuleActionRequest.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this CreateRuleActionRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this CreateRuleActionRequest.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this CreateRuleActionRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def x_lb_service(self):
        """Gets the x_lb_service of this CreateRuleActionRequest.

        此参数定义了lbservice

        :return: The x_lb_service of this CreateRuleActionRequest.
        :rtype: str
        """
        return self._x_lb_service

    @x_lb_service.setter
    def x_lb_service(self, x_lb_service):
        """Sets the x_lb_service of this CreateRuleActionRequest.

        此参数定义了lbservice

        :param x_lb_service: The x_lb_service of this CreateRuleActionRequest.
        :type: str
        """
        self._x_lb_service = x_lb_service

    @property
    def body(self):
        """Gets the body of this CreateRuleActionRequest.


        :return: The body of this CreateRuleActionRequest.
        :rtype: AddActionReq
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateRuleActionRequest.


        :param body: The body of this CreateRuleActionRequest.
        :type: AddActionReq
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
        if not isinstance(other, CreateRuleActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
