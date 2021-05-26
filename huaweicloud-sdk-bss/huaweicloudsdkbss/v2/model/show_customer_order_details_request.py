# coding: utf-8

import pprint
import re

import six





class ShowCustomerOrderDetailsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'order_id': 'order_id',
        'limit': 'limit',
        'offset': 'offset',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, order_id=None, limit=None, offset=None, indirect_partner_id=None):
        """ShowCustomerOrderDetailsRequest - a model defined in huaweicloud sdk"""
        
        

        self._order_id = None
        self._limit = None
        self._offset = None
        self._indirect_partner_id = None
        self.discriminator = None

        self.order_id = order_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def order_id(self):
        """Gets the order_id of this ShowCustomerOrderDetailsRequest.

        订单ID。 查询订单列表时系统会返回订单ID。

        :return: The order_id of this ShowCustomerOrderDetailsRequest.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ShowCustomerOrderDetailsRequest.

        订单ID。 查询订单列表时系统会返回订单ID。

        :param order_id: The order_id of this ShowCustomerOrderDetailsRequest.
        :type: str
        """
        self._order_id = order_id

    @property
    def limit(self):
        """Gets the limit of this ShowCustomerOrderDetailsRequest.

        每页大小。默认值为10。

        :return: The limit of this ShowCustomerOrderDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowCustomerOrderDetailsRequest.

        每页大小。默认值为10。

        :param limit: The limit of this ShowCustomerOrderDetailsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowCustomerOrderDetailsRequest.

        偏移量，从0开始。默认值为0。

        :return: The offset of this ShowCustomerOrderDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowCustomerOrderDetailsRequest.

        偏移量，从0开始。默认值为0。

        :param offset: The offset of this ShowCustomerOrderDetailsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ShowCustomerOrderDetailsRequest.

        精英服务商ID。 华为云伙伴能力中心（一级经销商）查询精英服务商的客户订单详情时，需要携带该参数；否则只能查询自己客户的订单详情。

        :return: The indirect_partner_id of this ShowCustomerOrderDetailsRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ShowCustomerOrderDetailsRequest.

        精英服务商ID。 华为云伙伴能力中心（一级经销商）查询精英服务商的客户订单详情时，需要携带该参数；否则只能查询自己客户的订单详情。

        :param indirect_partner_id: The indirect_partner_id of this ShowCustomerOrderDetailsRequest.
        :type: str
        """
        self._indirect_partner_id = indirect_partner_id

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
        if not isinstance(other, ShowCustomerOrderDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
