# coding: utf-8

import pprint
import re

import six





class ShowSinkTaskDetailRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'connector_id': 'str',
        'task_id': 'str'
    }

    attribute_map = {
        'connector_id': 'connector_id',
        'task_id': 'task_id'
    }

    def __init__(self, connector_id=None, task_id=None):
        """ShowSinkTaskDetailRequest - a model defined in huaweicloud sdk"""
        
        

        self._connector_id = None
        self._task_id = None
        self.discriminator = None

        self.connector_id = connector_id
        self.task_id = task_id

    @property
    def connector_id(self):
        """Gets the connector_id of this ShowSinkTaskDetailRequest.

        实例转储ID。 请参考[实例生命周期][查询实例]接口返回的数据。

        :return: The connector_id of this ShowSinkTaskDetailRequest.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this ShowSinkTaskDetailRequest.

        实例转储ID。 请参考[实例生命周期][查询实例]接口返回的数据。

        :param connector_id: The connector_id of this ShowSinkTaskDetailRequest.
        :type: str
        """
        self._connector_id = connector_id

    @property
    def task_id(self):
        """Gets the task_id of this ShowSinkTaskDetailRequest.

        转储任务ID。

        :return: The task_id of this ShowSinkTaskDetailRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ShowSinkTaskDetailRequest.

        转储任务ID。

        :param task_id: The task_id of this ShowSinkTaskDetailRequest.
        :type: str
        """
        self._task_id = task_id

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
        if not isinstance(other, ShowSinkTaskDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
