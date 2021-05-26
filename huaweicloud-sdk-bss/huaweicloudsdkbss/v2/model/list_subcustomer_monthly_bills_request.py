# coding: utf-8

import pprint
import re

import six





class ListSubcustomerMonthlyBillsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'customer_id': 'str',
        'cycle': 'str',
        'cloud_service_type': 'str',
        'charge_mode': 'str',
        'offset': 'int',
        'limit': 'int',
        'bill_type': 'str',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'cycle': 'cycle',
        'cloud_service_type': 'cloud_service_type',
        'charge_mode': 'charge_mode',
        'offset': 'offset',
        'limit': 'limit',
        'bill_type': 'bill_type',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, customer_id=None, cycle=None, cloud_service_type=None, charge_mode=None, offset=None, limit=None, bill_type=None, indirect_partner_id=None):
        """ListSubcustomerMonthlyBillsRequest - a model defined in huaweicloud sdk"""
        
        

        self._customer_id = None
        self._cycle = None
        self._cloud_service_type = None
        self._charge_mode = None
        self._offset = None
        self._limit = None
        self._bill_type = None
        self._indirect_partner_id = None
        self.discriminator = None

        if customer_id is not None:
            self.customer_id = customer_id
        self.cycle = cycle
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        self.charge_mode = charge_mode
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if bill_type is not None:
            self.bill_type = bill_type
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def customer_id(self):
        """Gets the customer_id of this ListSubcustomerMonthlyBillsRequest.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :return: The customer_id of this ListSubcustomerMonthlyBillsRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ListSubcustomerMonthlyBillsRequest.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :param customer_id: The customer_id of this ListSubcustomerMonthlyBillsRequest.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def cycle(self):
        """Gets the cycle of this ListSubcustomerMonthlyBillsRequest.

        消费时间。 格式固定为YYYY-MM。 示例：2018-08

        :return: The cycle of this ListSubcustomerMonthlyBillsRequest.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this ListSubcustomerMonthlyBillsRequest.

        消费时间。 格式固定为YYYY-MM。 示例：2018-08

        :param cycle: The cycle of this ListSubcustomerMonthlyBillsRequest.
        :type: str
        """
        self._cycle = cycle

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this ListSubcustomerMonthlyBillsRequest.

        云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。您可以调用查询云服务类型列表接口获取。

        :return: The cloud_service_type of this ListSubcustomerMonthlyBillsRequest.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this ListSubcustomerMonthlyBillsRequest.

        云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。您可以调用查询云服务类型列表接口获取。

        :param cloud_service_type: The cloud_service_type of this ListSubcustomerMonthlyBillsRequest.
        :type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ListSubcustomerMonthlyBillsRequest.

        计费模式。 1：包年/包月3：按需

        :return: The charge_mode of this ListSubcustomerMonthlyBillsRequest.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ListSubcustomerMonthlyBillsRequest.

        计费模式。 1：包年/包月3：按需

        :param charge_mode: The charge_mode of this ListSubcustomerMonthlyBillsRequest.
        :type: str
        """
        self._charge_mode = charge_mode

    @property
    def offset(self):
        """Gets the offset of this ListSubcustomerMonthlyBillsRequest.

        偏移量，从0开始。默认值为0。

        :return: The offset of this ListSubcustomerMonthlyBillsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSubcustomerMonthlyBillsRequest.

        偏移量，从0开始。默认值为0。

        :param offset: The offset of this ListSubcustomerMonthlyBillsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSubcustomerMonthlyBillsRequest.

        每页个数。默认值为10。

        :return: The limit of this ListSubcustomerMonthlyBillsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSubcustomerMonthlyBillsRequest.

        每页个数。默认值为10。

        :param limit: The limit of this ListSubcustomerMonthlyBillsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def bill_type(self):
        """Gets the bill_type of this ListSubcustomerMonthlyBillsRequest.

        账单类型。 0：消费1：退订2：华为核销

        :return: The bill_type of this ListSubcustomerMonthlyBillsRequest.
        :rtype: str
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this ListSubcustomerMonthlyBillsRequest.

        账单类型。 0：消费1：退订2：华为核销

        :param bill_type: The bill_type of this ListSubcustomerMonthlyBillsRequest.
        :type: str
        """
        self._bill_type = bill_type

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListSubcustomerMonthlyBillsRequest.

        精英服务商ID。

        :return: The indirect_partner_id of this ListSubcustomerMonthlyBillsRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListSubcustomerMonthlyBillsRequest.

        精英服务商ID。

        :param indirect_partner_id: The indirect_partner_id of this ListSubcustomerMonthlyBillsRequest.
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
        if not isinstance(other, ListSubcustomerMonthlyBillsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
