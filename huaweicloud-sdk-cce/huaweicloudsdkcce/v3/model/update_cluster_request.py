# coding: utf-8

import pprint
import re

import six





class UpdateClusterRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'error_status': 'str',
        'body': 'ClusterInformation'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'error_status': 'errorStatus',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, error_status=None, body=None):
        """UpdateClusterRequest - a model defined in huaweicloud sdk"""
        
        

        self._cluster_id = None
        self._error_status = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if error_status is not None:
            self.error_status = error_status
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        """Gets the cluster_id of this UpdateClusterRequest.

        集群 ID，获取方式请参见[[如何获取接口URI中参数](https://support.huaweicloud.com/api-cce/cce_02_0271.html)](tag:hws)[[如何获取接口URI中参数](https://support.huaweicloud.com/intl/zh-cn/api-cce/cce_02_0271.html)](tag:hws_hk)

        :return: The cluster_id of this UpdateClusterRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this UpdateClusterRequest.

        集群 ID，获取方式请参见[[如何获取接口URI中参数](https://support.huaweicloud.com/api-cce/cce_02_0271.html)](tag:hws)[[如何获取接口URI中参数](https://support.huaweicloud.com/intl/zh-cn/api-cce/cce_02_0271.html)](tag:hws_hk)

        :param cluster_id: The cluster_id of this UpdateClusterRequest.
        :type: str
        """
        self._cluster_id = cluster_id

    @property
    def error_status(self):
        """Gets the error_status of this UpdateClusterRequest.

        集群状态兼容Error参数，用于API平滑切换。 兼容场景下，errorStatus为空则屏蔽Error状态为Deleting状态。

        :return: The error_status of this UpdateClusterRequest.
        :rtype: str
        """
        return self._error_status

    @error_status.setter
    def error_status(self, error_status):
        """Sets the error_status of this UpdateClusterRequest.

        集群状态兼容Error参数，用于API平滑切换。 兼容场景下，errorStatus为空则屏蔽Error状态为Deleting状态。

        :param error_status: The error_status of this UpdateClusterRequest.
        :type: str
        """
        self._error_status = error_status

    @property
    def body(self):
        """Gets the body of this UpdateClusterRequest.


        :return: The body of this UpdateClusterRequest.
        :rtype: ClusterInformation
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateClusterRequest.


        :param body: The body of this UpdateClusterRequest.
        :type: ClusterInformation
        """
        self._body = body

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
        if not isinstance(other, UpdateClusterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
