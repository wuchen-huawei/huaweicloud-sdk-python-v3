# coding: utf-8

import pprint
import re

import six





class KeystoneShowSecurityComplianceByOptionRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'option': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'option': 'option'
    }

    def __init__(self, domain_id=None, option=None):
        """KeystoneShowSecurityComplianceByOptionRequest - a model defined in huaweicloud sdk"""
        
        

        self._domain_id = None
        self._option = None
        self.discriminator = None

        self.domain_id = domain_id
        self.option = option

    @property
    def domain_id(self):
        """Gets the domain_id of this KeystoneShowSecurityComplianceByOptionRequest.

        待查询的账号ID，获取方式请参见：[获取账号、IAM用户、项目、用户组、委托的名称和ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :return: The domain_id of this KeystoneShowSecurityComplianceByOptionRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this KeystoneShowSecurityComplianceByOptionRequest.

        待查询的账号ID，获取方式请参见：[获取账号、IAM用户、项目、用户组、委托的名称和ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :param domain_id: The domain_id of this KeystoneShowSecurityComplianceByOptionRequest.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def option(self):
        """Gets the option of this KeystoneShowSecurityComplianceByOptionRequest.

        查询条件。该字段内容为：password_regex或password_regex_description。    password_regex：密码强度策略的正则表达式；password_regex_description：密码强度策略的描述。

        :return: The option of this KeystoneShowSecurityComplianceByOptionRequest.
        :rtype: str
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this KeystoneShowSecurityComplianceByOptionRequest.

        查询条件。该字段内容为：password_regex或password_regex_description。    password_regex：密码强度策略的正则表达式；password_regex_description：密码强度策略的描述。

        :param option: The option of this KeystoneShowSecurityComplianceByOptionRequest.
        :type: str
        """
        self._option = option

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
        if not isinstance(other, KeystoneShowSecurityComplianceByOptionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
