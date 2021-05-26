# coding: utf-8

import pprint
import re

import six





class ListIssuedPartnerCouponsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'coupon_id': 'str',
        'customer_id': 'str',
        'order_id': 'str',
        'coupon_type': 'int',
        'status': 'int',
        'create_time_begin': 'str',
        'create_time_end': 'str',
        'effective_time_begin': 'str',
        'effective_time_end': 'str',
        'expire_time_begin': 'str',
        'expire_time_end': 'str',
        'offset': 'int',
        'limit': 'int',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'coupon_id': 'coupon_id',
        'customer_id': 'customer_id',
        'order_id': 'order_id',
        'coupon_type': 'coupon_type',
        'status': 'status',
        'create_time_begin': 'create_time_begin',
        'create_time_end': 'create_time_end',
        'effective_time_begin': 'effective_time_begin',
        'effective_time_end': 'effective_time_end',
        'expire_time_begin': 'expire_time_begin',
        'expire_time_end': 'expire_time_end',
        'offset': 'offset',
        'limit': 'limit',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, coupon_id=None, customer_id=None, order_id=None, coupon_type=None, status=None, create_time_begin=None, create_time_end=None, effective_time_begin=None, effective_time_end=None, expire_time_begin=None, expire_time_end=None, offset=None, limit=None, indirect_partner_id=None):
        """ListIssuedPartnerCouponsRequest - a model defined in huaweicloud sdk"""
        
        

        self._coupon_id = None
        self._customer_id = None
        self._order_id = None
        self._coupon_type = None
        self._status = None
        self._create_time_begin = None
        self._create_time_end = None
        self._effective_time_begin = None
        self._effective_time_end = None
        self._expire_time_begin = None
        self._expire_time_end = None
        self._offset = None
        self._limit = None
        self._indirect_partner_id = None
        self.discriminator = None

        if coupon_id is not None:
            self.coupon_id = coupon_id
        if customer_id is not None:
            self.customer_id = customer_id
        if order_id is not None:
            self.order_id = order_id
        if coupon_type is not None:
            self.coupon_type = coupon_type
        if status is not None:
            self.status = status
        if create_time_begin is not None:
            self.create_time_begin = create_time_begin
        if create_time_end is not None:
            self.create_time_end = create_time_end
        if effective_time_begin is not None:
            self.effective_time_begin = effective_time_begin
        if effective_time_end is not None:
            self.effective_time_end = effective_time_end
        if expire_time_begin is not None:
            self.expire_time_begin = expire_time_begin
        if expire_time_end is not None:
            self.expire_time_end = expire_time_end
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def coupon_id(self):
        """Gets the coupon_id of this ListIssuedPartnerCouponsRequest.

        优惠券ID。

        :return: The coupon_id of this ListIssuedPartnerCouponsRequest.
        :rtype: str
        """
        return self._coupon_id

    @coupon_id.setter
    def coupon_id(self, coupon_id):
        """Sets the coupon_id of this ListIssuedPartnerCouponsRequest.

        优惠券ID。

        :param coupon_id: The coupon_id of this ListIssuedPartnerCouponsRequest.
        :type: str
        """
        self._coupon_id = coupon_id

    @property
    def customer_id(self):
        """Gets the customer_id of this ListIssuedPartnerCouponsRequest.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :return: The customer_id of this ListIssuedPartnerCouponsRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ListIssuedPartnerCouponsRequest.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :param customer_id: The customer_id of this ListIssuedPartnerCouponsRequest.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def order_id(self):
        """Gets the order_id of this ListIssuedPartnerCouponsRequest.

        订单ID。

        :return: The order_id of this ListIssuedPartnerCouponsRequest.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ListIssuedPartnerCouponsRequest.

        订单ID。

        :param order_id: The order_id of this ListIssuedPartnerCouponsRequest.
        :type: str
        """
        self._order_id = order_id

    @property
    def coupon_type(self):
        """Gets the coupon_type of this ListIssuedPartnerCouponsRequest.

        优惠券类型： 1：代金券4：现金券

        :return: The coupon_type of this ListIssuedPartnerCouponsRequest.
        :rtype: int
        """
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, coupon_type):
        """Sets the coupon_type of this ListIssuedPartnerCouponsRequest.

        优惠券类型： 1：代金券4：现金券

        :param coupon_type: The coupon_type of this ListIssuedPartnerCouponsRequest.
        :type: int
        """
        self._coupon_type = coupon_type

    @property
    def status(self):
        """Gets the status of this ListIssuedPartnerCouponsRequest.

        客户优惠券实例状态： 1：未激活2：可使用3：已使用4：已过期5：已回收

        :return: The status of this ListIssuedPartnerCouponsRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListIssuedPartnerCouponsRequest.

        客户优惠券实例状态： 1：未激活2：可使用3：已使用4：已过期5：已回收

        :param status: The status of this ListIssuedPartnerCouponsRequest.
        :type: int
        """
        self._status = status

    @property
    def create_time_begin(self):
        """Gets the create_time_begin of this ListIssuedPartnerCouponsRequest.

        创建时间（开始）。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。 输入这个条件，会查询出创建时间大于这个时间的记录。

        :return: The create_time_begin of this ListIssuedPartnerCouponsRequest.
        :rtype: str
        """
        return self._create_time_begin

    @create_time_begin.setter
    def create_time_begin(self, create_time_begin):
        """Sets the create_time_begin of this ListIssuedPartnerCouponsRequest.

        创建时间（开始）。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。 输入这个条件，会查询出创建时间大于这个时间的记录。

        :param create_time_begin: The create_time_begin of this ListIssuedPartnerCouponsRequest.
        :type: str
        """
        self._create_time_begin = create_time_begin

    @property
    def create_time_end(self):
        """Gets the create_time_end of this ListIssuedPartnerCouponsRequest.

        创建时间（结束）。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。 输入这个条件，会查询出创建时间小于这个时间的记录。

        :return: The create_time_end of this ListIssuedPartnerCouponsRequest.
        :rtype: str
        """
        return self._create_time_end

    @create_time_end.setter
    def create_time_end(self, create_time_end):
        """Sets the create_time_end of this ListIssuedPartnerCouponsRequest.

        创建时间（结束）。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。 输入这个条件，会查询出创建时间小于这个时间的记录。

        :param create_time_end: The create_time_end of this ListIssuedPartnerCouponsRequest.
        :type: str
        """
        self._create_time_end = create_time_end

    @property
    def effective_time_begin(self):
        """Gets the effective_time_begin of this ListIssuedPartnerCouponsRequest.

        生效时间（开始）。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。 输入这个条件，会查询出生效时间大于这个时间的记录。

        :return: The effective_time_begin of this ListIssuedPartnerCouponsRequest.
        :rtype: str
        """
        return self._effective_time_begin

    @effective_time_begin.setter
    def effective_time_begin(self, effective_time_begin):
        """Sets the effective_time_begin of this ListIssuedPartnerCouponsRequest.

        生效时间（开始）。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。 输入这个条件，会查询出生效时间大于这个时间的记录。

        :param effective_time_begin: The effective_time_begin of this ListIssuedPartnerCouponsRequest.
        :type: str
        """
        self._effective_time_begin = effective_time_begin

    @property
    def effective_time_end(self):
        """Gets the effective_time_end of this ListIssuedPartnerCouponsRequest.

        生效时间（结束）。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。 输入这个条件，会查询出生效时间小于这个时间的记录。

        :return: The effective_time_end of this ListIssuedPartnerCouponsRequest.
        :rtype: str
        """
        return self._effective_time_end

    @effective_time_end.setter
    def effective_time_end(self, effective_time_end):
        """Sets the effective_time_end of this ListIssuedPartnerCouponsRequest.

        生效时间（结束）。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。 输入这个条件，会查询出生效时间小于这个时间的记录。

        :param effective_time_end: The effective_time_end of this ListIssuedPartnerCouponsRequest.
        :type: str
        """
        self._effective_time_end = effective_time_end

    @property
    def expire_time_begin(self):
        """Gets the expire_time_begin of this ListIssuedPartnerCouponsRequest.

        失效时间（开始）。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。 输入这个条件，会查询出失效时间大于这个时间的记录。

        :return: The expire_time_begin of this ListIssuedPartnerCouponsRequest.
        :rtype: str
        """
        return self._expire_time_begin

    @expire_time_begin.setter
    def expire_time_begin(self, expire_time_begin):
        """Sets the expire_time_begin of this ListIssuedPartnerCouponsRequest.

        失效时间（开始）。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。 输入这个条件，会查询出失效时间大于这个时间的记录。

        :param expire_time_begin: The expire_time_begin of this ListIssuedPartnerCouponsRequest.
        :type: str
        """
        self._expire_time_begin = expire_time_begin

    @property
    def expire_time_end(self):
        """Gets the expire_time_end of this ListIssuedPartnerCouponsRequest.

        失效时间（结束）。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。 输入这个条件，会查询出失效时间小于这个时间的记录。

        :return: The expire_time_end of this ListIssuedPartnerCouponsRequest.
        :rtype: str
        """
        return self._expire_time_end

    @expire_time_end.setter
    def expire_time_end(self, expire_time_end):
        """Sets the expire_time_end of this ListIssuedPartnerCouponsRequest.

        失效时间（结束）。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。 输入这个条件，会查询出失效时间小于这个时间的记录。

        :param expire_time_end: The expire_time_end of this ListIssuedPartnerCouponsRequest.
        :type: str
        """
        self._expire_time_end = expire_time_end

    @property
    def offset(self):
        """Gets the offset of this ListIssuedPartnerCouponsRequest.

        偏移量，从0开始。默认值为0。

        :return: The offset of this ListIssuedPartnerCouponsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListIssuedPartnerCouponsRequest.

        偏移量，从0开始。默认值为0。

        :param offset: The offset of this ListIssuedPartnerCouponsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListIssuedPartnerCouponsRequest.

        查询的每页数量。默认值为10。

        :return: The limit of this ListIssuedPartnerCouponsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListIssuedPartnerCouponsRequest.

        查询的每页数量。默认值为10。

        :param limit: The limit of this ListIssuedPartnerCouponsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListIssuedPartnerCouponsRequest.

        精英服务商ID。 华为云伙伴能力中心（一级经销商）查询精英服务商发放给子客户的优惠券时，需要携带该参数；否则只能查询发放给自己子客户的优惠券。

        :return: The indirect_partner_id of this ListIssuedPartnerCouponsRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListIssuedPartnerCouponsRequest.

        精英服务商ID。 华为云伙伴能力中心（一级经销商）查询精英服务商发放给子客户的优惠券时，需要携带该参数；否则只能查询发放给自己子客户的优惠券。

        :param indirect_partner_id: The indirect_partner_id of this ListIssuedPartnerCouponsRequest.
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
        if not isinstance(other, ListIssuedPartnerCouponsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
