# coding: utf-8

import pprint
import re

import six





class ListPostpaidBillSumRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bill_cycle': 'str'
    }

    attribute_map = {
        'bill_cycle': 'bill_cycle'
    }

    def __init__(self, bill_cycle=None):
        """ListPostpaidBillSumRequest - a model defined in huaweicloud sdk"""
        
        

        self._bill_cycle = None
        self.discriminator = None

        self.bill_cycle = bill_cycle

    @property
    def bill_cycle(self):
        """Gets the bill_cycle of this ListPostpaidBillSumRequest.

        |参数名称：账期，格式YYYY-MM示例：2020-07| |参数的约束及描述：|

        :return: The bill_cycle of this ListPostpaidBillSumRequest.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        """Sets the bill_cycle of this ListPostpaidBillSumRequest.

        |参数名称：账期，格式YYYY-MM示例：2020-07| |参数的约束及描述：|

        :param bill_cycle: The bill_cycle of this ListPostpaidBillSumRequest.
        :type: str
        """
        self._bill_cycle = bill_cycle

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
        if not isinstance(other, ListPostpaidBillSumRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
