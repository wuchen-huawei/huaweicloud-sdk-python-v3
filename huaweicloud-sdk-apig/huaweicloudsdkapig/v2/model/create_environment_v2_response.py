# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateEnvironmentV2Response(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'create_time': 'datetime',
        'name': 'str',
        'remark': 'str',
        'id': 'str'
    }

    attribute_map = {
        'create_time': 'create_time',
        'name': 'name',
        'remark': 'remark',
        'id': 'id'
    }

    def __init__(self, create_time=None, name=None, remark=None, id=None):
        """CreateEnvironmentV2Response - a model defined in huaweicloud sdk"""
        
        super(CreateEnvironmentV2Response, self).__init__()

        self._create_time = None
        self._name = None
        self._remark = None
        self._id = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if name is not None:
            self.name = name
        if remark is not None:
            self.remark = remark
        if id is not None:
            self.id = id

    @property
    def create_time(self):
        """Gets the create_time of this CreateEnvironmentV2Response.

        创建时间

        :return: The create_time of this CreateEnvironmentV2Response.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateEnvironmentV2Response.

        创建时间

        :param create_time: The create_time of this CreateEnvironmentV2Response.
        :type: datetime
        """
        self._create_time = create_time

    @property
    def name(self):
        """Gets the name of this CreateEnvironmentV2Response.

        环境名称

        :return: The name of this CreateEnvironmentV2Response.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateEnvironmentV2Response.

        环境名称

        :param name: The name of this CreateEnvironmentV2Response.
        :type: str
        """
        self._name = name

    @property
    def remark(self):
        """Gets the remark of this CreateEnvironmentV2Response.

        描述信息

        :return: The remark of this CreateEnvironmentV2Response.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this CreateEnvironmentV2Response.

        描述信息

        :param remark: The remark of this CreateEnvironmentV2Response.
        :type: str
        """
        self._remark = remark

    @property
    def id(self):
        """Gets the id of this CreateEnvironmentV2Response.

        环境id

        :return: The id of this CreateEnvironmentV2Response.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateEnvironmentV2Response.

        环境id

        :param id: The id of this CreateEnvironmentV2Response.
        :type: str
        """
        self._id = id

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
        if not isinstance(other, CreateEnvironmentV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
