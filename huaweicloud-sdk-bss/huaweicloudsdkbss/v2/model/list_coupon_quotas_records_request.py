# coding: utf-8

import pprint
import re

import six





class ListCouponQuotasRecordsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'indirect_partner_id': 'str',
        'quota_id': 'str',
        'operation_time_begin': 'str',
        'operation_time_end': 'str',
        'parent_quota_id': 'str',
        'operation_type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'indirect_partner_id': 'indirect_partner_id',
        'quota_id': 'quota_id',
        'operation_time_begin': 'operation_time_begin',
        'operation_time_end': 'operation_time_end',
        'parent_quota_id': 'parent_quota_id',
        'operation_type': 'operation_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, indirect_partner_id=None, quota_id=None, operation_time_begin=None, operation_time_end=None, parent_quota_id=None, operation_type=None, offset=None, limit=None):
        """ListCouponQuotasRecordsRequest - a model defined in huaweicloud sdk"""
        
        

        self._indirect_partner_id = None
        self._quota_id = None
        self._operation_time_begin = None
        self._operation_time_end = None
        self._parent_quota_id = None
        self._operation_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id
        if quota_id is not None:
            self.quota_id = quota_id
        if operation_time_begin is not None:
            self.operation_time_begin = operation_time_begin
        if operation_time_end is not None:
            self.operation_time_end = operation_time_end
        if parent_quota_id is not None:
            self.parent_quota_id = parent_quota_id
        if operation_type is not None:
            self.operation_type = operation_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListCouponQuotasRecordsRequest.

        精英服务商ID。 为空表示查询所有的代金券额度发放回收记录。不为空表示仅查询与该精英服务商相关的代金券额度发放回收记录。 默认查询所有精英服务商的代金券额度发放回收记录。

        :return: The indirect_partner_id of this ListCouponQuotasRecordsRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListCouponQuotasRecordsRequest.

        精英服务商ID。 为空表示查询所有的代金券额度发放回收记录。不为空表示仅查询与该精英服务商相关的代金券额度发放回收记录。 默认查询所有精英服务商的代金券额度发放回收记录。

        :param indirect_partner_id: The indirect_partner_id of this ListCouponQuotasRecordsRequest.
        :type: str
        """
        self._indirect_partner_id = indirect_partner_id

    @property
    def quota_id(self):
        """Gets the quota_id of this ListCouponQuotasRecordsRequest.

        精英服务商的代金券额度ID。 即华为云伙伴能力中心给精英服务商发放代金券额度时，产生的精英服务商的代金券额度ID，或者从精英服务商回收代金券额度时，精英服务商的代金券额度ID。

        :return: The quota_id of this ListCouponQuotasRecordsRequest.
        :rtype: str
        """
        return self._quota_id

    @quota_id.setter
    def quota_id(self, quota_id):
        """Sets the quota_id of this ListCouponQuotasRecordsRequest.

        精英服务商的代金券额度ID。 即华为云伙伴能力中心给精英服务商发放代金券额度时，产生的精英服务商的代金券额度ID，或者从精英服务商回收代金券额度时，精英服务商的代金券额度ID。

        :param quota_id: The quota_id of this ListCouponQuotasRecordsRequest.
        :type: str
        """
        self._quota_id = quota_id

    @property
    def operation_time_begin(self):
        """Gets the operation_time_begin of this ListCouponQuotasRecordsRequest.

        查询条件：操作起始时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。

        :return: The operation_time_begin of this ListCouponQuotasRecordsRequest.
        :rtype: str
        """
        return self._operation_time_begin

    @operation_time_begin.setter
    def operation_time_begin(self, operation_time_begin):
        """Sets the operation_time_begin of this ListCouponQuotasRecordsRequest.

        查询条件：操作起始时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。

        :param operation_time_begin: The operation_time_begin of this ListCouponQuotasRecordsRequest.
        :type: str
        """
        self._operation_time_begin = operation_time_begin

    @property
    def operation_time_end(self):
        """Gets the operation_time_end of this ListCouponQuotasRecordsRequest.

        查询条件：操作截止时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。

        :return: The operation_time_end of this ListCouponQuotasRecordsRequest.
        :rtype: str
        """
        return self._operation_time_end

    @operation_time_end.setter
    def operation_time_end(self, operation_time_end):
        """Sets the operation_time_end of this ListCouponQuotasRecordsRequest.

        查询条件：操作截止时间。 UTC时间，格式：yyyy-MM-dd'T'HH:mm:ss'Z'，如“2019-05-06T08:05:01Z”。其中，HH范围是0～23，mm和ss范围是0～59。

        :param operation_time_end: The operation_time_end of this ListCouponQuotasRecordsRequest.
        :type: str
        """
        self._operation_time_end = operation_time_end

    @property
    def parent_quota_id(self):
        """Gets the parent_quota_id of this ListCouponQuotasRecordsRequest.

        父额度ID。 这即华为云伙伴能力中心给精英服务商发放代金券额度时，华为云伙伴能力中心的额度ID，或者从精英服务商回收代金券额度时，回收的华为云伙伴能力中心的额度ID。

        :return: The parent_quota_id of this ListCouponQuotasRecordsRequest.
        :rtype: str
        """
        return self._parent_quota_id

    @parent_quota_id.setter
    def parent_quota_id(self, parent_quota_id):
        """Sets the parent_quota_id of this ListCouponQuotasRecordsRequest.

        父额度ID。 这即华为云伙伴能力中心给精英服务商发放代金券额度时，华为云伙伴能力中心的额度ID，或者从精英服务商回收代金券额度时，回收的华为云伙伴能力中心的额度ID。

        :param parent_quota_id: The parent_quota_id of this ListCouponQuotasRecordsRequest.
        :type: str
        """
        self._parent_quota_id = parent_quota_id

    @property
    def operation_type(self):
        """Gets the operation_type of this ListCouponQuotasRecordsRequest.

        操作类型。 10：发放额度11：回收额度

        :return: The operation_type of this ListCouponQuotasRecordsRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this ListCouponQuotasRecordsRequest.

        操作类型。 10：发放额度11：回收额度

        :param operation_type: The operation_type of this ListCouponQuotasRecordsRequest.
        :type: str
        """
        self._operation_type = operation_type

    @property
    def offset(self):
        """Gets the offset of this ListCouponQuotasRecordsRequest.

        偏移量，从0开始，默认值为0。

        :return: The offset of this ListCouponQuotasRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCouponQuotasRecordsRequest.

        偏移量，从0开始，默认值为0。

        :param offset: The offset of this ListCouponQuotasRecordsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListCouponQuotasRecordsRequest.

        每次查询的数目。默认值为10。

        :return: The limit of this ListCouponQuotasRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCouponQuotasRecordsRequest.

        每次查询的数目。默认值为10。

        :param limit: The limit of this ListCouponQuotasRecordsRequest.
        :type: int
        """
        self._limit = limit

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
        if not isinstance(other, ListCouponQuotasRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
