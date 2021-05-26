# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowCustomerMonthlySumResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'bill_sums': 'list[BillSumRecordInfoV2]',
        'consume_amount': 'float',
        'debt_amount': 'float',
        'coupon_amount': 'float',
        'flexipurchase_coupon_amount': 'float',
        'stored_value_card_amount': 'float',
        'cash_amount': 'float',
        'credit_amount': 'float',
        'writeoff_amount': 'float',
        'measure_id': 'int',
        'currency': 'str'
    }

    attribute_map = {
        'total_count': 'total_count',
        'bill_sums': 'bill_sums',
        'consume_amount': 'consume_amount',
        'debt_amount': 'debt_amount',
        'coupon_amount': 'coupon_amount',
        'flexipurchase_coupon_amount': 'flexipurchase_coupon_amount',
        'stored_value_card_amount': 'stored_value_card_amount',
        'cash_amount': 'cash_amount',
        'credit_amount': 'credit_amount',
        'writeoff_amount': 'writeoff_amount',
        'measure_id': 'measure_id',
        'currency': 'currency'
    }

    def __init__(self, total_count=None, bill_sums=None, consume_amount=None, debt_amount=None, coupon_amount=None, flexipurchase_coupon_amount=None, stored_value_card_amount=None, cash_amount=None, credit_amount=None, writeoff_amount=None, measure_id=None, currency=None):
        """ShowCustomerMonthlySumResponse - a model defined in huaweicloud sdk"""
        
        super(ShowCustomerMonthlySumResponse, self).__init__()

        self._total_count = None
        self._bill_sums = None
        self._consume_amount = None
        self._debt_amount = None
        self._coupon_amount = None
        self._flexipurchase_coupon_amount = None
        self._stored_value_card_amount = None
        self._cash_amount = None
        self._credit_amount = None
        self._writeoff_amount = None
        self._measure_id = None
        self._currency = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if bill_sums is not None:
            self.bill_sums = bill_sums
        if consume_amount is not None:
            self.consume_amount = consume_amount
        if debt_amount is not None:
            self.debt_amount = debt_amount
        if coupon_amount is not None:
            self.coupon_amount = coupon_amount
        if flexipurchase_coupon_amount is not None:
            self.flexipurchase_coupon_amount = flexipurchase_coupon_amount
        if stored_value_card_amount is not None:
            self.stored_value_card_amount = stored_value_card_amount
        if cash_amount is not None:
            self.cash_amount = cash_amount
        if credit_amount is not None:
            self.credit_amount = credit_amount
        if writeoff_amount is not None:
            self.writeoff_amount = writeoff_amount
        if measure_id is not None:
            self.measure_id = measure_id
        if currency is not None:
            self.currency = currency

    @property
    def total_count(self):
        """Gets the total_count of this ShowCustomerMonthlySumResponse.

        总条数，必须大于等于0。

        :return: The total_count of this ShowCustomerMonthlySumResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ShowCustomerMonthlySumResponse.

        总条数，必须大于等于0。

        :param total_count: The total_count of this ShowCustomerMonthlySumResponse.
        :type: int
        """
        self._total_count = total_count

    @property
    def bill_sums(self):
        """Gets the bill_sums of this ShowCustomerMonthlySumResponse.

        账单记录，具体参考表2。

        :return: The bill_sums of this ShowCustomerMonthlySumResponse.
        :rtype: list[BillSumRecordInfoV2]
        """
        return self._bill_sums

    @bill_sums.setter
    def bill_sums(self, bill_sums):
        """Sets the bill_sums of this ShowCustomerMonthlySumResponse.

        账单记录，具体参考表2。

        :param bill_sums: The bill_sums of this ShowCustomerMonthlySumResponse.
        :type: list[BillSumRecordInfoV2]
        """
        self._bill_sums = bill_sums

    @property
    def consume_amount(self):
        """Gets the consume_amount of this ShowCustomerMonthlySumResponse.

        总金额（包含退订）。

        :return: The consume_amount of this ShowCustomerMonthlySumResponse.
        :rtype: float
        """
        return self._consume_amount

    @consume_amount.setter
    def consume_amount(self, consume_amount):
        """Sets the consume_amount of this ShowCustomerMonthlySumResponse.

        总金额（包含退订）。

        :param consume_amount: The consume_amount of this ShowCustomerMonthlySumResponse.
        :type: float
        """
        self._consume_amount = consume_amount

    @property
    def debt_amount(self):
        """Gets the debt_amount of this ShowCustomerMonthlySumResponse.

        总欠费金额。

        :return: The debt_amount of this ShowCustomerMonthlySumResponse.
        :rtype: float
        """
        return self._debt_amount

    @debt_amount.setter
    def debt_amount(self, debt_amount):
        """Sets the debt_amount of this ShowCustomerMonthlySumResponse.

        总欠费金额。

        :param debt_amount: The debt_amount of this ShowCustomerMonthlySumResponse.
        :type: float
        """
        self._debt_amount = debt_amount

    @property
    def coupon_amount(self):
        """Gets the coupon_amount of this ShowCustomerMonthlySumResponse.

        代金券金额。

        :return: The coupon_amount of this ShowCustomerMonthlySumResponse.
        :rtype: float
        """
        return self._coupon_amount

    @coupon_amount.setter
    def coupon_amount(self, coupon_amount):
        """Sets the coupon_amount of this ShowCustomerMonthlySumResponse.

        代金券金额。

        :param coupon_amount: The coupon_amount of this ShowCustomerMonthlySumResponse.
        :type: float
        """
        self._coupon_amount = coupon_amount

    @property
    def flexipurchase_coupon_amount(self):
        """Gets the flexipurchase_coupon_amount of this ShowCustomerMonthlySumResponse.

        现金券金额，预留。

        :return: The flexipurchase_coupon_amount of this ShowCustomerMonthlySumResponse.
        :rtype: float
        """
        return self._flexipurchase_coupon_amount

    @flexipurchase_coupon_amount.setter
    def flexipurchase_coupon_amount(self, flexipurchase_coupon_amount):
        """Sets the flexipurchase_coupon_amount of this ShowCustomerMonthlySumResponse.

        现金券金额，预留。

        :param flexipurchase_coupon_amount: The flexipurchase_coupon_amount of this ShowCustomerMonthlySumResponse.
        :type: float
        """
        self._flexipurchase_coupon_amount = flexipurchase_coupon_amount

    @property
    def stored_value_card_amount(self):
        """Gets the stored_value_card_amount of this ShowCustomerMonthlySumResponse.

        储值卡金额，预留。

        :return: The stored_value_card_amount of this ShowCustomerMonthlySumResponse.
        :rtype: float
        """
        return self._stored_value_card_amount

    @stored_value_card_amount.setter
    def stored_value_card_amount(self, stored_value_card_amount):
        """Sets the stored_value_card_amount of this ShowCustomerMonthlySumResponse.

        储值卡金额，预留。

        :param stored_value_card_amount: The stored_value_card_amount of this ShowCustomerMonthlySumResponse.
        :type: float
        """
        self._stored_value_card_amount = stored_value_card_amount

    @property
    def cash_amount(self):
        """Gets the cash_amount of this ShowCustomerMonthlySumResponse.

        现金账户金额。

        :return: The cash_amount of this ShowCustomerMonthlySumResponse.
        :rtype: float
        """
        return self._cash_amount

    @cash_amount.setter
    def cash_amount(self, cash_amount):
        """Sets the cash_amount of this ShowCustomerMonthlySumResponse.

        现金账户金额。

        :param cash_amount: The cash_amount of this ShowCustomerMonthlySumResponse.
        :type: float
        """
        self._cash_amount = cash_amount

    @property
    def credit_amount(self):
        """Gets the credit_amount of this ShowCustomerMonthlySumResponse.

        信用账户金额。

        :return: The credit_amount of this ShowCustomerMonthlySumResponse.
        :rtype: float
        """
        return self._credit_amount

    @credit_amount.setter
    def credit_amount(self, credit_amount):
        """Sets the credit_amount of this ShowCustomerMonthlySumResponse.

        信用账户金额。

        :param credit_amount: The credit_amount of this ShowCustomerMonthlySumResponse.
        :type: float
        """
        self._credit_amount = credit_amount

    @property
    def writeoff_amount(self):
        """Gets the writeoff_amount of this ShowCustomerMonthlySumResponse.

        欠费核销金额。

        :return: The writeoff_amount of this ShowCustomerMonthlySumResponse.
        :rtype: float
        """
        return self._writeoff_amount

    @writeoff_amount.setter
    def writeoff_amount(self, writeoff_amount):
        """Sets the writeoff_amount of this ShowCustomerMonthlySumResponse.

        欠费核销金额。

        :param writeoff_amount: The writeoff_amount of this ShowCustomerMonthlySumResponse.
        :type: float
        """
        self._writeoff_amount = writeoff_amount

    @property
    def measure_id(self):
        """Gets the measure_id of this ShowCustomerMonthlySumResponse.

        金额单位。 1：元

        :return: The measure_id of this ShowCustomerMonthlySumResponse.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this ShowCustomerMonthlySumResponse.

        金额单位。 1：元

        :param measure_id: The measure_id of this ShowCustomerMonthlySumResponse.
        :type: int
        """
        self._measure_id = measure_id

    @property
    def currency(self):
        """Gets the currency of this ShowCustomerMonthlySumResponse.

        币种。 CNY：人民币。

        :return: The currency of this ShowCustomerMonthlySumResponse.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ShowCustomerMonthlySumResponse.

        币种。 CNY：人民币。

        :param currency: The currency of this ShowCustomerMonthlySumResponse.
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
        if not isinstance(other, ShowCustomerMonthlySumResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
