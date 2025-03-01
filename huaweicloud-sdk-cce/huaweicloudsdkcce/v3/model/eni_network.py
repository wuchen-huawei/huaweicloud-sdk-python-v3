# coding: utf-8

import pprint
import re

import six





class EniNetwork:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'eni_subnet_id': 'str',
        'eni_subnet_cidr': 'str'
    }

    attribute_map = {
        'eni_subnet_id': 'eniSubnetId',
        'eni_subnet_cidr': 'eniSubnetCIDR'
    }

    def __init__(self, eni_subnet_id=None, eni_subnet_cidr=None):
        """EniNetwork - a model defined in huaweicloud sdk"""
        
        

        self._eni_subnet_id = None
        self._eni_subnet_cidr = None
        self.discriminator = None

        self.eni_subnet_id = eni_subnet_id
        self.eni_subnet_cidr = eni_subnet_cidr

    @property
    def eni_subnet_id(self):
        """Gets the eni_subnet_id of this EniNetwork.

        用于创建控制节点的subnet的IPv4网络ID(暂不支持IPv6)。获取方法如下：- 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找IPv4网络ID。- 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)](tag:hws)[[查询子网列表](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_subnet01_0003.html)](tag:hws_hk)

        :return: The eni_subnet_id of this EniNetwork.
        :rtype: str
        """
        return self._eni_subnet_id

    @eni_subnet_id.setter
    def eni_subnet_id(self, eni_subnet_id):
        """Sets the eni_subnet_id of this EniNetwork.

        用于创建控制节点的subnet的IPv4网络ID(暂不支持IPv6)。获取方法如下：- 方法1：登录虚拟私有云服务的控制台界面，单击VPC下的子网，进入子网详情页面，查找IPv4网络ID。- 方法2：通过虚拟私有云服务的API接口查询，具体操作可参考[[查询子网列表](https://support.huaweicloud.com/api-vpc/vpc_subnet01_0003.html)](tag:hws)[[查询子网列表](https://support.huaweicloud.com/intl/zh-cn/api-vpc/vpc_subnet01_0003.html)](tag:hws_hk)

        :param eni_subnet_id: The eni_subnet_id of this EniNetwork.
        :type: str
        """
        self._eni_subnet_id = eni_subnet_id

    @property
    def eni_subnet_cidr(self):
        """Gets the eni_subnet_cidr of this EniNetwork.

        ENI子网CIDR

        :return: The eni_subnet_cidr of this EniNetwork.
        :rtype: str
        """
        return self._eni_subnet_cidr

    @eni_subnet_cidr.setter
    def eni_subnet_cidr(self, eni_subnet_cidr):
        """Sets the eni_subnet_cidr of this EniNetwork.

        ENI子网CIDR

        :param eni_subnet_cidr: The eni_subnet_cidr of this EniNetwork.
        :type: str
        """
        self._eni_subnet_cidr = eni_subnet_cidr

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
        if not isinstance(other, EniNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
