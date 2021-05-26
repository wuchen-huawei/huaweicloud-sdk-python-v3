# coding: utf-8

import pprint
import re

import six





class KeystoneListPermissionsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'domain_id': 'str',
        'page': 'int',
        'per_page': 'int'
    }

    attribute_map = {
        'name': 'name',
        'domain_id': 'domain_id',
        'page': 'page',
        'per_page': 'per_page'
    }

    def __init__(self, name=None, domain_id=None, page=None, per_page=None):
        """KeystoneListPermissionsRequest - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._domain_id = None
        self._page = None
        self._per_page = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if domain_id is not None:
            self.domain_id = domain_id
        if page is not None:
            self.page = page
        if per_page is not None:
            self.per_page = per_page

    @property
    def name(self):
        """Gets the name of this KeystoneListPermissionsRequest.

        权限名，获取方式请参见：[获取权限名、权限ID](https://support.huaweicloud.com/api-iam/iam_10_0001.html)。

        :return: The name of this KeystoneListPermissionsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KeystoneListPermissionsRequest.

        权限名，获取方式请参见：[获取权限名、权限ID](https://support.huaweicloud.com/api-iam/iam_10_0001.html)。

        :param name: The name of this KeystoneListPermissionsRequest.
        :type: str
        """
        self._name = name

    @property
    def domain_id(self):
        """Gets the domain_id of this KeystoneListPermissionsRequest.

        账号ID，获取方式请参见：[获取账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。    > - 如果填写此参数，则返回账号下所有自定义策略。 > - 如果不填写此参数，则返回所有系统权限（包含系统策略和系统角色）。

        :return: The domain_id of this KeystoneListPermissionsRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this KeystoneListPermissionsRequest.

        账号ID，获取方式请参见：[获取账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。    > - 如果填写此参数，则返回账号下所有自定义策略。 > - 如果不填写此参数，则返回所有系统权限（包含系统策略和系统角色）。

        :param domain_id: The domain_id of this KeystoneListPermissionsRequest.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def page(self):
        """Gets the page of this KeystoneListPermissionsRequest.

        分页查询时数据的页数，查询值最小为1，默认值为1。需要与per_page同时使用。

        :return: The page of this KeystoneListPermissionsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this KeystoneListPermissionsRequest.

        分页查询时数据的页数，查询值最小为1，默认值为1。需要与per_page同时使用。

        :param page: The page of this KeystoneListPermissionsRequest.
        :type: int
        """
        self._page = page

    @property
    def per_page(self):
        """Gets the per_page of this KeystoneListPermissionsRequest.

        分页查询时每页的数据个数，取值范围为[1,300], 默认值为300。需要与page同时使用。

        :return: The per_page of this KeystoneListPermissionsRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this KeystoneListPermissionsRequest.

        分页查询时每页的数据个数，取值范围为[1,300], 默认值为300。需要与page同时使用。

        :param per_page: The per_page of this KeystoneListPermissionsRequest.
        :type: int
        """
        self._per_page = per_page

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
        if not isinstance(other, KeystoneListPermissionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
