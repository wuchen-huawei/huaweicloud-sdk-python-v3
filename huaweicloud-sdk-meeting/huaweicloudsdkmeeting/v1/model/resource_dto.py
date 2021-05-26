# coding: utf-8

import pprint
import re

import six





class ResourceDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'type_id': 'str',
        'count': 'int',
        'expire_date': 'int'
    }

    attribute_map = {
        'type': 'type',
        'type_id': 'typeId',
        'count': 'count',
        'expire_date': 'expireDate'
    }

    def __init__(self, type=None, type_id=None, count=None, expire_date=None):
        """ResourceDTO - a model defined in huaweicloud sdk"""
        
        

        self._type = None
        self._type_id = None
        self._count = None
        self._expire_date = None
        self.discriminator = None

        self.type = type
        if type_id is not None:
            self.type_id = type_id
        self.count = count
        self.expire_date = expire_date

    @property
    def type(self):
        """Gets the type of this ResourceDTO.

        资源类型，前台通过查询接口返回该sp支持售卖的资源在界面上做相应屏蔽，当前为枚举类型. - VMR        - 云会议室 - CONF_CALL  - 会议并发数 - HARD_1080P - 1080P硬终端 - HARD_720P  - 720P硬终端 - SOFT       - 软终端用户数 - ROOM       - 大屏软终端 - LIVE       - 直播推流 - RECORD     - 录播空间 - HARD_THIRD_PARTY - 第三方硬终端账号 - HUAWEI_VISION -智慧屏 - IDEA_HUB   - ideahub

        :return: The type of this ResourceDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceDTO.

        资源类型，前台通过查询接口返回该sp支持售卖的资源在界面上做相应屏蔽，当前为枚举类型. - VMR        - 云会议室 - CONF_CALL  - 会议并发数 - HARD_1080P - 1080P硬终端 - HARD_720P  - 720P硬终端 - SOFT       - 软终端用户数 - ROOM       - 大屏软终端 - LIVE       - 直播推流 - RECORD     - 录播空间 - HARD_THIRD_PARTY - 第三方硬终端账号 - HUAWEI_VISION -智慧屏 - IDEA_HUB   - ideahub

        :param type: The type of this ResourceDTO.
        :type: str
        """
        self._type = type

    @property
    def type_id(self):
        """Gets the type_id of this ResourceDTO.

        类型标识，比如资源类型为vmr，vmr又分为5方，10方等，该参数为vmrPkgId，用来区分子类别，详见如下： - vmr10:ff808081699b56d40169c410d5080179 - vmr50:ff808081699b56cb0169c411a0980152 - vmr100:ff808081699b56cb0169c41167850151 - vmr200:ff808081699b56d40169c410913d0178 - vmr25:ff808081699b56d40169c4111fe5017a - vmr300:ff8080816b9ec3ab016bdff237962e83 - vmr400:ff8080816b9ec475016bdff37efc279f - vmr500:ff8080816b9ec3ab016bdff338542e84

        :return: The type_id of this ResourceDTO.
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this ResourceDTO.

        类型标识，比如资源类型为vmr，vmr又分为5方，10方等，该参数为vmrPkgId，用来区分子类别，详见如下： - vmr10:ff808081699b56d40169c410d5080179 - vmr50:ff808081699b56cb0169c411a0980152 - vmr100:ff808081699b56cb0169c41167850151 - vmr200:ff808081699b56d40169c410913d0178 - vmr25:ff808081699b56d40169c4111fe5017a - vmr300:ff8080816b9ec3ab016bdff237962e83 - vmr400:ff8080816b9ec475016bdff37efc279f - vmr500:ff8080816b9ec3ab016bdff338542e84

        :param type_id: The type_id of this ResourceDTO.
        :type: str
        """
        self._type_id = type_id

    @property
    def count(self):
        """Gets the count of this ResourceDTO.

        资源数量

        :return: The count of this ResourceDTO.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ResourceDTO.

        资源数量

        :param count: The count of this ResourceDTO.
        :type: int
        """
        self._count = count

    @property
    def expire_date(self):
        """Gets the expire_date of this ResourceDTO.

        到期时间,utc时间戳

        :return: The expire_date of this ResourceDTO.
        :rtype: int
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """Sets the expire_date of this ResourceDTO.

        到期时间,utc时间戳

        :param expire_date: The expire_date of this ResourceDTO.
        :type: int
        """
        self._expire_date = expire_date

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
        if not isinstance(other, ResourceDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
