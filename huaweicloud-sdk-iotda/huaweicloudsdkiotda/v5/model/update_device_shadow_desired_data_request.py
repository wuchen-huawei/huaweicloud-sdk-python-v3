# coding: utf-8

import pprint
import re

import six





class UpdateDeviceShadowDesiredDataRequest:


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
        'device_id': 'str',
        'body': 'UpdateDesireds'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'device_id': 'device_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, device_id=None, body=None):
        """UpdateDeviceShadowDesiredDataRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._device_id = None
        self._body = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        self.device_id = device_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this UpdateDeviceShadowDesiredDataRequest.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this UpdateDeviceShadowDesiredDataRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this UpdateDeviceShadowDesiredDataRequest.

        实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this UpdateDeviceShadowDesiredDataRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def device_id(self):
        """Gets the device_id of this UpdateDeviceShadowDesiredDataRequest.

        设备ID，用于唯一标识一个设备。在注册设备时直接指定，或者由物联网平台分配获得。由物联网平台分配时，生成规则为\"product_id\" + \"_\" + \"node_id\"拼接而成。

        :return: The device_id of this UpdateDeviceShadowDesiredDataRequest.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this UpdateDeviceShadowDesiredDataRequest.

        设备ID，用于唯一标识一个设备。在注册设备时直接指定，或者由物联网平台分配获得。由物联网平台分配时，生成规则为\"product_id\" + \"_\" + \"node_id\"拼接而成。

        :param device_id: The device_id of this UpdateDeviceShadowDesiredDataRequest.
        :type: str
        """
        self._device_id = device_id

    @property
    def body(self):
        """Gets the body of this UpdateDeviceShadowDesiredDataRequest.


        :return: The body of this UpdateDeviceShadowDesiredDataRequest.
        :rtype: UpdateDesireds
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateDeviceShadowDesiredDataRequest.


        :param body: The body of this UpdateDeviceShadowDesiredDataRequest.
        :type: UpdateDesireds
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
        if not isinstance(other, UpdateDeviceShadowDesiredDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
