# coding: utf-8

import pprint
import re

import six





class KeystoneShowRegionRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'region_id': 'str'
    }

    attribute_map = {
        'region_id': 'region_id'
    }

    def __init__(self, region_id=None):
        """KeystoneShowRegionRequest - a model defined in huaweicloud sdk"""
        
        

        self._region_id = None
        self.discriminator = None

        self.region_id = region_id

    @property
    def region_id(self):
        """Gets the region_id of this KeystoneShowRegionRequest.

        待查询的区域ID。可以使用[查询区域列表](https://support.huaweicloud.com/api-iam/iam_05_0001.html)接口获取，控制台获取方法请参见：[获取区域ID](https://console.huaweicloud.com/iam/?agencyId=d15f57bd355d4514bd9618bd648dd432®ion=cn-east-2&locale=zh-cn#/iam/projects)

        :return: The region_id of this KeystoneShowRegionRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this KeystoneShowRegionRequest.

        待查询的区域ID。可以使用[查询区域列表](https://support.huaweicloud.com/api-iam/iam_05_0001.html)接口获取，控制台获取方法请参见：[获取区域ID](https://console.huaweicloud.com/iam/?agencyId=d15f57bd355d4514bd9618bd648dd432®ion=cn-east-2&locale=zh-cn#/iam/projects)

        :param region_id: The region_id of this KeystoneShowRegionRequest.
        :type: str
        """
        self._region_id = region_id

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
        if not isinstance(other, KeystoneShowRegionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
