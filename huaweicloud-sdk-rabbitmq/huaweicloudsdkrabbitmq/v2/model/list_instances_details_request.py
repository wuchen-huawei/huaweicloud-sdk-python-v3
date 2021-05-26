# coding: utf-8

import pprint
import re

import six





class ListInstancesDetailsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'engine': 'str',
        'name': 'str',
        'instance_id': 'str',
        'status': 'str',
        'include_failure': 'str',
        'exact_match_name': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'engine': 'engine',
        'name': 'name',
        'instance_id': 'instance_id',
        'status': 'status',
        'include_failure': 'include_failure',
        'exact_match_name': 'exact_match_name',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, engine=None, name=None, instance_id=None, status=None, include_failure=None, exact_match_name=None, enterprise_project_id=None):
        """ListInstancesDetailsRequest - a model defined in huaweicloud sdk"""
        
        

        self._engine = None
        self._name = None
        self._instance_id = None
        self._status = None
        self._include_failure = None
        self._exact_match_name = None
        self._enterprise_project_id = None
        self.discriminator = None

        if engine is not None:
            self.engine = engine
        if name is not None:
            self.name = name
        if instance_id is not None:
            self.instance_id = instance_id
        if status is not None:
            self.status = status
        if include_failure is not None:
            self.include_failure = include_failure
        if exact_match_name is not None:
            self.exact_match_name = exact_match_name
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def engine(self):
        """Gets the engine of this ListInstancesDetailsRequest.

        引擎类型：rabbitmq，参数缺失查询所有实例。

        :return: The engine of this ListInstancesDetailsRequest.
        :rtype: str
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this ListInstancesDetailsRequest.

        引擎类型：rabbitmq，参数缺失查询所有实例。

        :param engine: The engine of this ListInstancesDetailsRequest.
        :type: str
        """
        self._engine = engine

    @property
    def name(self):
        """Gets the name of this ListInstancesDetailsRequest.

        实例名称。

        :return: The name of this ListInstancesDetailsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListInstancesDetailsRequest.

        实例名称。

        :param name: The name of this ListInstancesDetailsRequest.
        :type: str
        """
        self._name = name

    @property
    def instance_id(self):
        """Gets the instance_id of this ListInstancesDetailsRequest.

        实例ID。

        :return: The instance_id of this ListInstancesDetailsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListInstancesDetailsRequest.

        实例ID。

        :param instance_id: The instance_id of this ListInstancesDetailsRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def status(self):
        """Gets the status of this ListInstancesDetailsRequest.

        实例状态。详细状态说明见[实例状态说明](https://support.huaweicloud.com/api-rabbitmq/rabbitmq-api-180514012.html)。

        :return: The status of this ListInstancesDetailsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListInstancesDetailsRequest.

        实例状态。详细状态说明见[实例状态说明](https://support.huaweicloud.com/api-rabbitmq/rabbitmq-api-180514012.html)。

        :param status: The status of this ListInstancesDetailsRequest.
        :type: str
        """
        self._status = status

    @property
    def include_failure(self):
        """Gets the include_failure of this ListInstancesDetailsRequest.

        是否返回创建失败的实例数。  当参数值为“true”时，返回创建失败的实例数。参数值为“false”或者其他值，不返回创建失败的实例数。

        :return: The include_failure of this ListInstancesDetailsRequest.
        :rtype: str
        """
        return self._include_failure

    @include_failure.setter
    def include_failure(self, include_failure):
        """Sets the include_failure of this ListInstancesDetailsRequest.

        是否返回创建失败的实例数。  当参数值为“true”时，返回创建失败的实例数。参数值为“false”或者其他值，不返回创建失败的实例数。

        :param include_failure: The include_failure of this ListInstancesDetailsRequest.
        :type: str
        """
        self._include_failure = include_failure

    @property
    def exact_match_name(self):
        """Gets the exact_match_name of this ListInstancesDetailsRequest.

        是否按照实例名称进行精确匹配查询。  默认为“false”，表示模糊匹配实例名称查询。若参数值为“true”表示按照实例名称进行精确匹配查询。

        :return: The exact_match_name of this ListInstancesDetailsRequest.
        :rtype: str
        """
        return self._exact_match_name

    @exact_match_name.setter
    def exact_match_name(self, exact_match_name):
        """Sets the exact_match_name of this ListInstancesDetailsRequest.

        是否按照实例名称进行精确匹配查询。  默认为“false”，表示模糊匹配实例名称查询。若参数值为“true”表示按照实例名称进行精确匹配查询。

        :param exact_match_name: The exact_match_name of this ListInstancesDetailsRequest.
        :type: str
        """
        self._exact_match_name = exact_match_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListInstancesDetailsRequest.

        企业项目ID。

        :return: The enterprise_project_id of this ListInstancesDetailsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListInstancesDetailsRequest.

        企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListInstancesDetailsRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListInstancesDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
