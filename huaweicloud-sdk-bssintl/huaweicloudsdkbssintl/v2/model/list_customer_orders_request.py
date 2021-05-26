# coding: utf-8

import pprint
import re

import six





class ListCustomerOrdersRequest:


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
        'customer_id': 'str',
        'create_time_begin': 'str',
        'create_time_end': 'str',
        'service_type_code': 'str',
        'status': 'int',
        'order_type': 'str',
        'limit': 'int',
        'offset': 'int',
        'order_by': 'str',
        'payment_time_begin': 'str',
        'payment_time_end': 'str',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'order_id': 'order_id',
        'customer_id': 'customer_id',
        'create_time_begin': 'create_time_begin',
        'create_time_end': 'create_time_end',
        'service_type_code': 'service_type_code',
        'status': 'status',
        'order_type': 'order_type',
        'limit': 'limit',
        'offset': 'offset',
        'order_by': 'order_by',
        'payment_time_begin': 'payment_time_begin',
        'payment_time_end': 'payment_time_end',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, order_id=None, customer_id=None, create_time_begin=None, create_time_end=None, service_type_code=None, status=None, order_type=None, limit=None, offset=None, order_by=None, payment_time_begin=None, payment_time_end=None, indirect_partner_id=None):
        """ListCustomerOrdersRequest - a model defined in huaweicloud sdk"""
        
        

        self._order_id = None
        self._customer_id = None
        self._create_time_begin = None
        self._create_time_end = None
        self._service_type_code = None
        self._status = None
        self._order_type = None
        self._limit = None
        self._offset = None
        self._order_by = None
        self._payment_time_begin = None
        self._payment_time_end = None
        self._indirect_partner_id = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if customer_id is not None:
            self.customer_id = customer_id
        if create_time_begin is not None:
            self.create_time_begin = create_time_begin
        if create_time_end is not None:
            self.create_time_end = create_time_end
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if status is not None:
            self.status = status
        if order_type is not None:
            self.order_type = order_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if order_by is not None:
            self.order_by = order_by
        if payment_time_begin is not None:
            self.payment_time_begin = payment_time_begin
        if payment_time_end is not None:
            self.payment_time_end = payment_time_end
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def order_id(self):
        """Gets the order_id of this ListCustomerOrdersRequest.

        |参数名称：订单ID。| |参数的约束及描述：|

        :return: The order_id of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ListCustomerOrdersRequest.

        |参数名称：订单ID。| |参数的约束及描述：|

        :param order_id: The order_id of this ListCustomerOrdersRequest.
        :type: str
        """
        self._order_id = order_id

    @property
    def customer_id(self):
        """Gets the customer_id of this ListCustomerOrdersRequest.

        |参数名称：客户账号ID。| |参数的约束及描述：|

        :return: The customer_id of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ListCustomerOrdersRequest.

        |参数名称：客户账号ID。| |参数的约束及描述：|

        :param customer_id: The customer_id of this ListCustomerOrdersRequest.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def create_time_begin(self):
        """Gets the create_time_begin of this ListCustomerOrdersRequest.

        |参数名称：订单创建开始时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2020-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数的约束及描述：|

        :return: The create_time_begin of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._create_time_begin

    @create_time_begin.setter
    def create_time_begin(self, create_time_begin):
        """Sets the create_time_begin of this ListCustomerOrdersRequest.

        |参数名称：订单创建开始时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2020-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数的约束及描述：|

        :param create_time_begin: The create_time_begin of this ListCustomerOrdersRequest.
        :type: str
        """
        self._create_time_begin = create_time_begin

    @property
    def create_time_end(self):
        """Gets the create_time_end of this ListCustomerOrdersRequest.

        |参数名称：订单创建结束时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2020-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数的约束及描述：|

        :return: The create_time_end of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._create_time_end

    @create_time_end.setter
    def create_time_end(self, create_time_end):
        """Sets the create_time_end of this ListCustomerOrdersRequest.

        |参数名称：订单创建结束时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2020-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数的约束及描述：|

        :param create_time_end: The create_time_end of this ListCustomerOrdersRequest.
        :type: str
        """
        self._create_time_end = create_time_end

    @property
    def service_type_code(self):
        """Gets the service_type_code of this ListCustomerOrdersRequest.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。| |参数的约束及描述：|

        :return: The service_type_code of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this ListCustomerOrdersRequest.

        |参数名称：云服务类型编码，例如ECS的云服务类型编码为“hws.service.type.ec2”。具体请参见云服务类型云服务类型云服务类型云服务类型。| |参数的约束及描述：|

        :param service_type_code: The service_type_code of this ListCustomerOrdersRequest.
        :type: str
        """
        self._service_type_code = service_type_code

    @property
    def status(self):
        """Gets the status of this ListCustomerOrdersRequest.

        |参数名称：订单状态。1：待审核3：处理中4：已取消5：已完成6：待支付9：待确认| |参数的约束及描述：|

        :return: The status of this ListCustomerOrdersRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListCustomerOrdersRequest.

        |参数名称：订单状态。1：待审核3：处理中4：已取消5：已完成6：待支付9：待确认| |参数的约束及描述：|

        :param status: The status of this ListCustomerOrdersRequest.
        :type: int
        """
        self._status = status

    @property
    def order_type(self):
        """Gets the order_type of this ListCustomerOrdersRequest.

        |参数名称：订单类型。1：开通2：续订3：变更4：退订10：包周期转按需11：按需转包周期12：赠送13：试用14：转商用15：费用调整| |参数的约束及描述：|

        :return: The order_type of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this ListCustomerOrdersRequest.

        |参数名称：订单类型。1：开通2：续订3：变更4：退订10：包周期转按需11：按需转包周期12：赠送13：试用14：转商用15：费用调整| |参数的约束及描述：|

        :param order_type: The order_type of this ListCustomerOrdersRequest.
        :type: str
        """
        self._order_type = order_type

    @property
    def limit(self):
        """Gets the limit of this ListCustomerOrdersRequest.

        |参数名称：每次查询的大小，默认为10| |参数的约束及描述：最大值100|

        :return: The limit of this ListCustomerOrdersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCustomerOrdersRequest.

        |参数名称：每次查询的大小，默认为10| |参数的约束及描述：最大值100|

        :param limit: The limit of this ListCustomerOrdersRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListCustomerOrdersRequest.

        |参数名称：偏移量，从0开始，默认为0| |参数的约束及描述：|

        :return: The offset of this ListCustomerOrdersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCustomerOrdersRequest.

        |参数名称：偏移量，从0开始，默认为0| |参数的约束及描述：|

        :param offset: The offset of this ListCustomerOrdersRequest.
        :type: int
        """
        self._offset = offset

    @property
    def order_by(self):
        """Gets the order_by of this ListCustomerOrdersRequest.

        |参数名称：查询的订单列表排序。支持3中多个响应参数进行排序，但每次只能用一个。缺省或者带+为升序，带-表示倒序。例如：按照创建时间升序排序表示为+createTime| |参数的约束及描述：|

        :return: The order_by of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        """Sets the order_by of this ListCustomerOrdersRequest.

        |参数名称：查询的订单列表排序。支持3中多个响应参数进行排序，但每次只能用一个。缺省或者带+为升序，带-表示倒序。例如：按照创建时间升序排序表示为+createTime| |参数的约束及描述：|

        :param order_by: The order_by of this ListCustomerOrdersRequest.
        :type: str
        """
        self._order_by = order_by

    @property
    def payment_time_begin(self):
        """Gets the payment_time_begin of this ListCustomerOrdersRequest.

        |参数名称：订单支付开始时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数的约束及描述：|

        :return: The payment_time_begin of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._payment_time_begin

    @payment_time_begin.setter
    def payment_time_begin(self, payment_time_begin):
        """Sets the payment_time_begin of this ListCustomerOrdersRequest.

        |参数名称：订单支付开始时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数的约束及描述：|

        :param payment_time_begin: The payment_time_begin of this ListCustomerOrdersRequest.
        :type: str
        """
        self._payment_time_begin = payment_time_begin

    @property
    def payment_time_end(self):
        """Gets the payment_time_end of this ListCustomerOrdersRequest.

        |参数名称：订单支付结束时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数的约束及描述：|

        :return: The payment_time_end of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._payment_time_end

    @payment_time_end.setter
    def payment_time_end(self, payment_time_end):
        """Sets the payment_time_end of this ListCustomerOrdersRequest.

        |参数名称：订单支付结束时间。UTC时间，格式：yyyy-MM-ddTHH:mm:ssZ，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。| |参数的约束及描述：|

        :param payment_time_end: The payment_time_end of this ListCustomerOrdersRequest.
        :type: str
        """
        self._payment_time_end = payment_time_end

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListCustomerOrdersRequest.

        |参数名称：二级经销商ID，只有伙伴用自身token调用的时候，该字段才有含义。| |参数的约束及描述：|

        :return: The indirect_partner_id of this ListCustomerOrdersRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListCustomerOrdersRequest.

        |参数名称：二级经销商ID，只有伙伴用自身token调用的时候，该字段才有含义。| |参数的约束及描述：|

        :param indirect_partner_id: The indirect_partner_id of this ListCustomerOrdersRequest.
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
        if not isinstance(other, ListCustomerOrdersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
