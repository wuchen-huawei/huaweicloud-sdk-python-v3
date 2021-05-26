# coding: utf-8

import pprint
import re

import six





class ListPartnerCouponsRecordRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'operation_types': 'list[str]',
        'quota_id': 'str',
        'quota_type': 'int',
        'coupon_ids': 'list[str]',
        'customer_id': 'str',
        'operation_time_begin': 'str',
        'operation_time_end': 'str',
        'result': 'str',
        'offset': 'int',
        'limit': 'int',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'operation_types': 'operation_types',
        'quota_id': 'quota_id',
        'quota_type': 'quota_type',
        'coupon_ids': 'coupon_ids',
        'customer_id': 'customer_id',
        'operation_time_begin': 'operation_time_begin',
        'operation_time_end': 'operation_time_end',
        'result': 'result',
        'offset': 'offset',
        'limit': 'limit',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, operation_types=None, quota_id=None, quota_type=None, coupon_ids=None, customer_id=None, operation_time_begin=None, operation_time_end=None, result=None, offset=None, limit=None, indirect_partner_id=None):
        """ListPartnerCouponsRecordRequest - a model defined in huaweicloud sdk"""
        
        

        self._operation_types = None
        self._quota_id = None
        self._quota_type = None
        self._coupon_ids = None
        self._customer_id = None
        self._operation_time_begin = None
        self._operation_time_end = None
        self._result = None
        self._offset = None
        self._limit = None
        self._indirect_partner_id = None
        self.discriminator = None

        if operation_types is not None:
            self.operation_types = operation_types
        if quota_id is not None:
            self.quota_id = quota_id
        if quota_type is not None:
            self.quota_type = quota_type
        if coupon_ids is not None:
            self.coupon_ids = coupon_ids
        if customer_id is not None:
            self.customer_id = customer_id
        if operation_time_begin is not None:
            self.operation_time_begin = operation_time_begin
        if operation_time_end is not None:
            self.operation_time_end = operation_time_end
        if result is not None:
            self.result = result
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def operation_types(self):
        """Gets the operation_types of this ListPartnerCouponsRecordRequest.

        操作类型。 1：发放2：手动回收3：解绑自动回收4：过期回收5：退订回收6：退款充值撤销7：建立关联回收

        :return: The operation_types of this ListPartnerCouponsRecordRequest.
        :rtype: list[str]
        """
        return self._operation_types

    @operation_types.setter
    def operation_types(self, operation_types):
        """Sets the operation_types of this ListPartnerCouponsRecordRequest.

        操作类型。 1：发放2：手动回收3：解绑自动回收4：过期回收5：退订回收6：退款充值撤销7：建立关联回收

        :param operation_types: The operation_types of this ListPartnerCouponsRecordRequest.
        :type: list[str]
        """
        self._operation_types = operation_types

    @property
    def quota_id(self):
        """Gets the quota_id of this ListPartnerCouponsRecordRequest.

        额度ID。 请从“查询优惠券额度”接口的响应参数中获取。

        :return: The quota_id of this ListPartnerCouponsRecordRequest.
        :rtype: str
        """
        return self._quota_id

    @quota_id.setter
    def quota_id(self, quota_id):
        """Sets the quota_id of this ListPartnerCouponsRecordRequest.

        额度ID。 请从“查询优惠券额度”接口的响应参数中获取。

        :param quota_id: The quota_id of this ListPartnerCouponsRecordRequest.
        :type: str
        """
        self._quota_id = quota_id

    @property
    def quota_type(self):
        """Gets the quota_type of this ListPartnerCouponsRecordRequest.

        额度类型： 0：代金券额度1：现金券额度

        :return: The quota_type of this ListPartnerCouponsRecordRequest.
        :rtype: int
        """
        return self._quota_type

    @quota_type.setter
    def quota_type(self, quota_type):
        """Sets the quota_type of this ListPartnerCouponsRecordRequest.

        额度类型： 0：代金券额度1：现金券额度

        :param quota_type: The quota_type of this ListPartnerCouponsRecordRequest.
        :type: int
        """
        self._quota_type = quota_type

    @property
    def coupon_ids(self):
        """Gets the coupon_ids of this ListPartnerCouponsRecordRequest.

        代金券ID列表。 请从“发放优惠券”接口的响应参数中获取。

        :return: The coupon_ids of this ListPartnerCouponsRecordRequest.
        :rtype: list[str]
        """
        return self._coupon_ids

    @coupon_ids.setter
    def coupon_ids(self, coupon_ids):
        """Sets the coupon_ids of this ListPartnerCouponsRecordRequest.

        代金券ID列表。 请从“发放优惠券”接口的响应参数中获取。

        :param coupon_ids: The coupon_ids of this ListPartnerCouponsRecordRequest.
        :type: list[str]
        """
        self._coupon_ids = coupon_ids

    @property
    def customer_id(self):
        """Gets the customer_id of this ListPartnerCouponsRecordRequest.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :return: The customer_id of this ListPartnerCouponsRecordRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ListPartnerCouponsRecordRequest.

        客户账号ID。您可以调用查询客户列表接口获取customer_id。

        :param customer_id: The customer_id of this ListPartnerCouponsRecordRequest.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def operation_time_begin(self):
        """Gets the operation_time_begin of this ListPartnerCouponsRecordRequest.

        操作时间（开始）。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。 输入这个条件，会查询出操作时间大于这个时间的记录。

        :return: The operation_time_begin of this ListPartnerCouponsRecordRequest.
        :rtype: str
        """
        return self._operation_time_begin

    @operation_time_begin.setter
    def operation_time_begin(self, operation_time_begin):
        """Sets the operation_time_begin of this ListPartnerCouponsRecordRequest.

        操作时间（开始）。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。 输入这个条件，会查询出操作时间大于这个时间的记录。

        :param operation_time_begin: The operation_time_begin of this ListPartnerCouponsRecordRequest.
        :type: str
        """
        self._operation_time_begin = operation_time_begin

    @property
    def operation_time_end(self):
        """Gets the operation_time_end of this ListPartnerCouponsRecordRequest.

        操作时间（结束）。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。 输入这个条件，会查询出操作时间小于这个时间的记录。

        :return: The operation_time_end of this ListPartnerCouponsRecordRequest.
        :rtype: str
        """
        return self._operation_time_end

    @operation_time_end.setter
    def operation_time_end(self, operation_time_end):
        """Sets the operation_time_end of this ListPartnerCouponsRecordRequest.

        操作时间（结束）。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。 其中，HH范围是0～23，mm和ss范围是0～59。 输入这个条件，会查询出操作时间小于这个时间的记录。

        :param operation_time_end: The operation_time_end of this ListPartnerCouponsRecordRequest.
        :type: str
        """
        self._operation_time_end = operation_time_end

    @property
    def result(self):
        """Gets the result of this ListPartnerCouponsRecordRequest.

        操作结果： 0：成功-1：失败（非0的记录）

        :return: The result of this ListPartnerCouponsRecordRequest.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ListPartnerCouponsRecordRequest.

        操作结果： 0：成功-1：失败（非0的记录）

        :param result: The result of this ListPartnerCouponsRecordRequest.
        :type: str
        """
        self._result = result

    @property
    def offset(self):
        """Gets the offset of this ListPartnerCouponsRecordRequest.

        偏移量，从0开始。默认值为0。

        :return: The offset of this ListPartnerCouponsRecordRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPartnerCouponsRecordRequest.

        偏移量，从0开始。默认值为0。

        :param offset: The offset of this ListPartnerCouponsRecordRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPartnerCouponsRecordRequest.

        每页记录数。默认值为10。

        :return: The limit of this ListPartnerCouponsRecordRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPartnerCouponsRecordRequest.

        每页记录数。默认值为10。

        :param limit: The limit of this ListPartnerCouponsRecordRequest.
        :type: int
        """
        self._limit = limit

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListPartnerCouponsRecordRequest.

        精英服务商ID。 华为云伙伴能力中心（一级经销商）查询精英服务商发放给子客户的优惠券发放记录时，需要携带该参数，否则只能查询发给自己子客户的优惠券发放记录。

        :return: The indirect_partner_id of this ListPartnerCouponsRecordRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListPartnerCouponsRecordRequest.

        精英服务商ID。 华为云伙伴能力中心（一级经销商）查询精英服务商发放给子客户的优惠券发放记录时，需要携带该参数，否则只能查询发给自己子客户的优惠券发放记录。

        :param indirect_partner_id: The indirect_partner_id of this ListPartnerCouponsRecordRequest.
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
        if not isinstance(other, ListPartnerCouponsRecordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
