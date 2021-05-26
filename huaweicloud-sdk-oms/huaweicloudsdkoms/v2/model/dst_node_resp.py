# coding: utf-8

import pprint
import re

import six





class DstNodeResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'region': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'region': 'region'
    }

    def __init__(self, bucket=None, region=None):
        """DstNodeResp - a model defined in huaweicloud sdk"""
        
        

        self._bucket = None
        self._region = None
        self.discriminator = None

        if bucket is not None:
            self.bucket = bucket
        if region is not None:
            self.region = region

    @property
    def bucket(self):
        """Gets the bucket of this DstNodeResp.

        目的端桶的名称。

        :return: The bucket of this DstNodeResp.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this DstNodeResp.

        目的端桶的名称。

        :param bucket: The bucket of this DstNodeResp.
        :type: str
        """
        self._bucket = bucket

    @property
    def region(self):
        """Gets the region of this DstNodeResp.

        目的端桶所处的区域。  请与Endpoint对应的区域保持一致。

        :return: The region of this DstNodeResp.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this DstNodeResp.

        目的端桶所处的区域。  请与Endpoint对应的区域保持一致。

        :param region: The region of this DstNodeResp.
        :type: str
        """
        self._region = region

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
        if not isinstance(other, DstNodeResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
