# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListClustersResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'kind': 'str',
        'api_version': 'str',
        'items': 'list[V3Cluster]'
    }

    attribute_map = {
        'kind': 'kind',
        'api_version': 'apiVersion',
        'items': 'items'
    }

    def __init__(self, kind=None, api_version=None, items=None):
        """ListClustersResponse - a model defined in huaweicloud sdk"""
        
        super(ListClustersResponse, self).__init__()

        self._kind = None
        self._api_version = None
        self._items = None
        self.discriminator = None

        if kind is not None:
            self.kind = kind
        if api_version is not None:
            self.api_version = api_version
        if items is not None:
            self.items = items

    @property
    def kind(self):
        """Gets the kind of this ListClustersResponse.

        Api type

        :return: The kind of this ListClustersResponse.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ListClustersResponse.

        Api type

        :param kind: The kind of this ListClustersResponse.
        :type: str
        """
        self._kind = kind

    @property
    def api_version(self):
        """Gets the api_version of this ListClustersResponse.

        API version

        :return: The api_version of this ListClustersResponse.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ListClustersResponse.

        API version

        :param api_version: The api_version of this ListClustersResponse.
        :type: str
        """
        self._api_version = api_version

    @property
    def items(self):
        """Gets the items of this ListClustersResponse.

        集群对象列表，包含了当前项目下所有集群的详细信息。您可通过items.metadata.name下的值来找到对应的集群。

        :return: The items of this ListClustersResponse.
        :rtype: list[V3Cluster]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ListClustersResponse.

        集群对象列表，包含了当前项目下所有集群的详细信息。您可通过items.metadata.name下的值来找到对应的集群。

        :param items: The items of this ListClustersResponse.
        :type: list[V3Cluster]
        """
        self._items = items

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
        if not isinstance(other, ListClustersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
