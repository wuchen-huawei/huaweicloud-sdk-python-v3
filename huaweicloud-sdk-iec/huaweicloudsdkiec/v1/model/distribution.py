# coding: utf-8

import pprint
import re

import six





class Distribution:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'area': 'str',
        'city': 'str',
        'operator': 'str',
        'province': 'str',
        'site_id': 'str',
        'pool_id': 'str',
        'stack_count': 'int',
        'city_short_name': 'str'
    }

    attribute_map = {
        'area': 'area',
        'city': 'city',
        'operator': 'operator',
        'province': 'province',
        'site_id': 'site_id',
        'pool_id': 'pool_id',
        'stack_count': 'stack_count',
        'city_short_name': 'city_short_name'
    }

    def __init__(self, area=None, city=None, operator=None, province=None, site_id=None, pool_id=None, stack_count=None, city_short_name=None):
        """Distribution - a model defined in huaweicloud sdk"""
        
        

        self._area = None
        self._city = None
        self._operator = None
        self._province = None
        self._site_id = None
        self._pool_id = None
        self._stack_count = None
        self._city_short_name = None
        self.discriminator = None

        if area is not None:
            self.area = area
        if city is not None:
            self.city = city
        if operator is not None:
            self.operator = operator
        if province is not None:
            self.province = province
        if site_id is not None:
            self.site_id = site_id
        if pool_id is not None:
            self.pool_id = pool_id
        if stack_count is not None:
            self.stack_count = stack_count
        if city_short_name is not None:
            self.city_short_name = city_short_name

    @property
    def area(self):
        """Gets the area of this Distribution.

        所在大区名称。

        :return: The area of this Distribution.
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this Distribution.

        所在大区名称。

        :param area: The area of this Distribution.
        :type: str
        """
        self._area = area

    @property
    def city(self):
        """Gets the city of this Distribution.

        所在城市名称。

        :return: The city of this Distribution.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Distribution.

        所在城市名称。

        :param city: The city of this Distribution.
        :type: str
        """
        self._city = city

    @property
    def operator(self):
        """Gets the operator of this Distribution.

        所属运营商名称。

        :return: The operator of this Distribution.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this Distribution.

        所属运营商名称。

        :param operator: The operator of this Distribution.
        :type: str
        """
        self._operator = operator

    @property
    def province(self):
        """Gets the province of this Distribution.

        所属省份名称。

        :return: The province of this Distribution.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this Distribution.

        所属省份名称。

        :param province: The province of this Distribution.
        :type: str
        """
        self._province = province

    @property
    def site_id(self):
        """Gets the site_id of this Distribution.

        站点ID。

        :return: The site_id of this Distribution.
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this Distribution.

        站点ID。

        :param site_id: The site_id of this Distribution.
        :type: str
        """
        self._site_id = site_id

    @property
    def pool_id(self):
        """Gets the pool_id of this Distribution.

        线路ID。多线路场景下，将在该线路下创建弹性公网IP。

        :return: The pool_id of this Distribution.
        :rtype: str
        """
        return self._pool_id

    @pool_id.setter
    def pool_id(self, pool_id):
        """Sets the pool_id of this Distribution.

        线路ID。多线路场景下，将在该线路下创建弹性公网IP。

        :param pool_id: The pool_id of this Distribution.
        :type: str
        """
        self._pool_id = pool_id

    @property
    def stack_count(self):
        """Gets the stack_count of this Distribution.

        资源组配置模板数目

        :return: The stack_count of this Distribution.
        :rtype: int
        """
        return self._stack_count

    @stack_count.setter
    def stack_count(self, stack_count):
        """Sets the stack_count of this Distribution.

        资源组配置模板数目

        :param stack_count: The stack_count of this Distribution.
        :type: int
        """
        self._stack_count = stack_count

    @property
    def city_short_name(self):
        """Gets the city_short_name of this Distribution.

        城市简称。

        :return: The city_short_name of this Distribution.
        :rtype: str
        """
        return self._city_short_name

    @city_short_name.setter
    def city_short_name(self, city_short_name):
        """Sets the city_short_name of this Distribution.

        城市简称。

        :param city_short_name: The city_short_name of this Distribution.
        :type: str
        """
        self._city_short_name = city_short_name

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
        if not isinstance(other, Distribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
