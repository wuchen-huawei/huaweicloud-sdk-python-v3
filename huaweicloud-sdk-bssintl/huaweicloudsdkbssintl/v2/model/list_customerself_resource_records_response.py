# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListCustomerselfResourceRecordsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'fee_records': 'list[ResFeeRecordV2]',
        'total_count': 'int',
        'currency': 'str'
    }

    attribute_map = {
        'fee_records': 'fee_records',
        'total_count': 'total_count',
        'currency': 'currency'
    }

    def __init__(self, fee_records=None, total_count=None, currency=None):
        """ListCustomerselfResourceRecordsResponse - a model defined in huaweicloud sdk"""
        
        super(ListCustomerselfResourceRecordsResponse, self).__init__()

        self._fee_records = None
        self._total_count = None
        self._currency = None
        self.discriminator = None

        if fee_records is not None:
            self.fee_records = fee_records
        if total_count is not None:
            self.total_count = total_count
        if currency is not None:
            self.currency = currency

    @property
    def fee_records(self):
        """Gets the fee_records of this ListCustomerselfResourceRecordsResponse.

        |参数名称：资源费用记录数据。具体请参见表 ResFeeRecordV2。| |参数约束以及描述：资源费用记录数据。具体请参见表 ResFeeRecordV2。|

        :return: The fee_records of this ListCustomerselfResourceRecordsResponse.
        :rtype: list[ResFeeRecordV2]
        """
        return self._fee_records

    @fee_records.setter
    def fee_records(self, fee_records):
        """Sets the fee_records of this ListCustomerselfResourceRecordsResponse.

        |参数名称：资源费用记录数据。具体请参见表 ResFeeRecordV2。| |参数约束以及描述：资源费用记录数据。具体请参见表 ResFeeRecordV2。|

        :param fee_records: The fee_records of this ListCustomerselfResourceRecordsResponse.
        :type: list[ResFeeRecordV2]
        """
        self._fee_records = fee_records

    @property
    def total_count(self):
        """Gets the total_count of this ListCustomerselfResourceRecordsResponse.

        |参数名称：结果集数量，只有成功才返回这个参数。| |参数的约束及描述：结果集数量，只有成功才返回这个参数。|

        :return: The total_count of this ListCustomerselfResourceRecordsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListCustomerselfResourceRecordsResponse.

        |参数名称：结果集数量，只有成功才返回这个参数。| |参数的约束及描述：结果集数量，只有成功才返回这个参数。|

        :param total_count: The total_count of this ListCustomerselfResourceRecordsResponse.
        :type: int
        """
        self._total_count = total_count

    @property
    def currency(self):
        """Gets the currency of this ListCustomerselfResourceRecordsResponse.

        |参数名称：货币单位代码：CNY：人民币USD：美元| |参数约束及描述：货币单位代码：CNY：人民币USD：美元|

        :return: The currency of this ListCustomerselfResourceRecordsResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ListCustomerselfResourceRecordsResponse.

        |参数名称：货币单位代码：CNY：人民币USD：美元| |参数约束及描述：货币单位代码：CNY：人民币USD：美元|

        :param currency: The currency of this ListCustomerselfResourceRecordsResponse.
        :type: str
        """
        self._currency = currency

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
        if not isinstance(other, ListCustomerselfResourceRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
