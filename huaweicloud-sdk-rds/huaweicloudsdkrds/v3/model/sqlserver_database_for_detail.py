# coding: utf-8

import pprint
import re

import six





class SqlserverDatabaseForDetail:


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
        'character_set': 'str',
        'state': 'str'
    }

    attribute_map = {
        'name': 'name',
        'character_set': 'character_set',
        'state': 'state'
    }

    def __init__(self, name=None, character_set=None, state=None):
        """SqlserverDatabaseForDetail - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._character_set = None
        self._state = None
        self.discriminator = None

        self.name = name
        self.character_set = character_set
        self.state = state

    @property
    def name(self):
        """Gets the name of this SqlserverDatabaseForDetail.

        数据库名称。

        :return: The name of this SqlserverDatabaseForDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SqlserverDatabaseForDetail.

        数据库名称。

        :param name: The name of this SqlserverDatabaseForDetail.
        :type: str
        """
        self._name = name

    @property
    def character_set(self):
        """Gets the character_set of this SqlserverDatabaseForDetail.

        数据库使用的字符集，例如Chinese_PRC_CI_AS等。

        :return: The character_set of this SqlserverDatabaseForDetail.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """Sets the character_set of this SqlserverDatabaseForDetail.

        数据库使用的字符集，例如Chinese_PRC_CI_AS等。

        :param character_set: The character_set of this SqlserverDatabaseForDetail.
        :type: str
        """
        self._character_set = character_set

    @property
    def state(self):
        """Gets the state of this SqlserverDatabaseForDetail.

        数据库状态。取值如下:  Creating:表示创建中。 Running:表示使用中。 Deleting:表示删除中。 NotExists:表示不存在。

        :return: The state of this SqlserverDatabaseForDetail.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SqlserverDatabaseForDetail.

        数据库状态。取值如下:  Creating:表示创建中。 Running:表示使用中。 Deleting:表示删除中。 NotExists:表示不存在。

        :param state: The state of this SqlserverDatabaseForDetail.
        :type: str
        """
        self._state = state

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
        if not isinstance(other, SqlserverDatabaseForDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
