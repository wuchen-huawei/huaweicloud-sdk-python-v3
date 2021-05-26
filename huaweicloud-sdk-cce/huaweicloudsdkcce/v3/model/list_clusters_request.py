# coding: utf-8

import pprint
import re

import six





class ListClustersRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'error_status': 'str',
        'detail': 'str',
        'status': 'str',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'error_status': 'errorStatus',
        'detail': 'detail',
        'status': 'status',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, error_status=None, detail=None, status=None, type=None, version=None):
        """ListClustersRequest - a model defined in huaweicloud sdk"""
        
        

        self._error_status = None
        self._detail = None
        self._status = None
        self._type = None
        self._version = None
        self.discriminator = None

        if error_status is not None:
            self.error_status = error_status
        if detail is not None:
            self.detail = detail
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def error_status(self):
        """Gets the error_status of this ListClustersRequest.

        集群状态兼容Error参数，用于API平滑切换。 兼容场景下，errorStatus为空则屏蔽Error状态为Deleting状态。

        :return: The error_status of this ListClustersRequest.
        :rtype: str
        """
        return self._error_status

    @error_status.setter
    def error_status(self, error_status):
        """Sets the error_status of this ListClustersRequest.

        集群状态兼容Error参数，用于API平滑切换。 兼容场景下，errorStatus为空则屏蔽Error状态为Deleting状态。

        :param error_status: The error_status of this ListClustersRequest.
        :type: str
        """
        self._error_status = error_status

    @property
    def detail(self):
        """Gets the detail of this ListClustersRequest.

        查询集群详细信息。若设置为true，获取集群下节点总数(totalNodesNumber)、正常节点数(activeNodesNumber)、CPU总量(totalNodesCPU)、内存总量(totalNodesMemory)、已安装插件列表(installedAddonInstances)，已安装插件列表中包含名称(addonTemplateName)、版本号(version)、插件的状态信息(status)，放入到annotation中。

        :return: The detail of this ListClustersRequest.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ListClustersRequest.

        查询集群详细信息。若设置为true，获取集群下节点总数(totalNodesNumber)、正常节点数(activeNodesNumber)、CPU总量(totalNodesCPU)、内存总量(totalNodesMemory)、已安装插件列表(installedAddonInstances)，已安装插件列表中包含名称(addonTemplateName)、版本号(version)、插件的状态信息(status)，放入到annotation中。

        :param detail: The detail of this ListClustersRequest.
        :type: str
        """
        self._detail = detail

    @property
    def status(self):
        """Gets the status of this ListClustersRequest.

        集群状态，取值如下 - Available：可用，表示集群处于正常状态。 - Unavailable：不可用，表示集群异常，需手动删除或联系管理员删除。 - ScalingUp：扩容中，表示集群正处于扩容过程中。 - ScalingDown：缩容中，表示集群正处于缩容过程中。 - Creating：创建中，表示集群正处于创建过程中。 - Deleting：删除中，表示集群正处于删除过程中。 - Upgrading：升级中，表示集群正处于升级过程中。 - Resizing：规格变更中，表示集群正处于变更规格中。 - Empty：集群无任何资源

        :return: The status of this ListClustersRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListClustersRequest.

        集群状态，取值如下 - Available：可用，表示集群处于正常状态。 - Unavailable：不可用，表示集群异常，需手动删除或联系管理员删除。 - ScalingUp：扩容中，表示集群正处于扩容过程中。 - ScalingDown：缩容中，表示集群正处于缩容过程中。 - Creating：创建中，表示集群正处于创建过程中。 - Deleting：删除中，表示集群正处于删除过程中。 - Upgrading：升级中，表示集群正处于升级过程中。 - Resizing：规格变更中，表示集群正处于变更规格中。 - Empty：集群无任何资源

        :param status: The status of this ListClustersRequest.
        :type: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ListClustersRequest.

        集群类型： - VirtualMachine：CCE集群 - ARM64：鲲鹏集群

        :return: The type of this ListClustersRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListClustersRequest.

        集群类型： - VirtualMachine：CCE集群 - ARM64：鲲鹏集群

        :param type: The type of this ListClustersRequest.
        :type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this ListClustersRequest.

        集群版本过滤

        :return: The version of this ListClustersRequest.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListClustersRequest.

        集群版本过滤

        :param version: The version of this ListClustersRequest.
        :type: str
        """
        self._version = version

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
        if not isinstance(other, ListClustersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
