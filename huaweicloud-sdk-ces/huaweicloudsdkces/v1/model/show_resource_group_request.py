# coding: utf-8

import pprint
import re

import six





class ShowResourceGroupRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'status': 'str',
        'namespace': 'str',
        'dname': 'str',
        'start': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'group_id': 'group_id',
        'status': 'status',
        'namespace': 'namespace',
        'dname': 'dname',
        'start': 'start',
        'limit': 'limit'
    }

    def __init__(self, group_id=None, status=None, namespace=None, dname=None, start=None, limit=None):
        """ShowResourceGroupRequest - a model defined in huaweicloud sdk"""
        
        

        self._group_id = None
        self._status = None
        self._namespace = None
        self._dname = None
        self._start = None
        self._limit = None
        self.discriminator = None

        self.group_id = group_id
        if status is not None:
            self.status = status
        if namespace is not None:
            self.namespace = namespace
        if dname is not None:
            self.dname = dname
        if start is not None:
            self.start = start
        if limit is not None:
            self.limit = limit

    @property
    def group_id(self):
        """Gets the group_id of this ShowResourceGroupRequest.

        资源分组ID。

        :return: The group_id of this ShowResourceGroupRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ShowResourceGroupRequest.

        资源分组ID。

        :param group_id: The group_id of this ShowResourceGroupRequest.
        :type: str
        """
        self._group_id = group_id

    @property
    def status(self):
        """Gets the status of this ShowResourceGroupRequest.

        资源健康状态，值可为health、unhealth、no_alarm_rule；health表示健康，

        :return: The status of this ShowResourceGroupRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowResourceGroupRequest.

        资源健康状态，值可为health、unhealth、no_alarm_rule；health表示健康，

        :param status: The status of this ShowResourceGroupRequest.
        :type: str
        """
        self._status = status

    @property
    def namespace(self):
        """Gets the namespace of this ShowResourceGroupRequest.

        资源类型，即命名空间，如弹性云服务器的资源命名空间为：SYS.ECS；各服务命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The namespace of this ShowResourceGroupRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ShowResourceGroupRequest.

        资源类型，即命名空间，如弹性云服务器的资源命名空间为：SYS.ECS；各服务命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param namespace: The namespace of this ShowResourceGroupRequest.
        :type: str
        """
        self._namespace = namespace

    @property
    def dname(self):
        """Gets the dname of this ShowResourceGroupRequest.

        资源维度，如：弹性云服务器，则维度为instance_id，各资源的监控维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The dname of this ShowResourceGroupRequest.
        :rtype: str
        """
        return self._dname

    @dname.setter
    def dname(self, dname):
        """Sets the dname of this ShowResourceGroupRequest.

        资源维度，如：弹性云服务器，则维度为instance_id，各资源的监控维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param dname: The dname of this ShowResourceGroupRequest.
        :type: str
        """
        self._dname = dname

    @property
    def start(self):
        """Gets the start of this ShowResourceGroupRequest.

        分页起始值，类型为integer，默认值为0。

        :return: The start of this ShowResourceGroupRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ShowResourceGroupRequest.

        分页起始值，类型为integer，默认值为0。

        :param start: The start of this ShowResourceGroupRequest.
        :type: str
        """
        self._start = start

    @property
    def limit(self):
        """Gets the limit of this ShowResourceGroupRequest.

        单次查询的条数限制，取值范围(0,100]，默认值为100， 用于限制结果数据条数。

        :return: The limit of this ShowResourceGroupRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowResourceGroupRequest.

        单次查询的条数限制，取值范围(0,100]，默认值为100， 用于限制结果数据条数。

        :param limit: The limit of this ShowResourceGroupRequest.
        :type: str
        """
        self._limit = limit

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
        if not isinstance(other, ShowResourceGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
