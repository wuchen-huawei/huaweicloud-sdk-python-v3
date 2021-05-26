# coding: utf-8

import pprint
import re

import six





class ShowPtrRecordSetRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'floatingip_id': 'str'
    }

    attribute_map = {
        'region': 'region',
        'floatingip_id': 'floatingip_id'
    }

    def __init__(self, region=None, floatingip_id=None):
        """ShowPtrRecordSetRequest - a model defined in huaweicloud sdk"""
        
        

        self._region = None
        self._floatingip_id = None
        self.discriminator = None

        self.region = region
        self.floatingip_id = floatingip_id

    @property
    def region(self):
        """Gets the region of this ShowPtrRecordSetRequest.

        租户的区域信息。 

        :return: The region of this ShowPtrRecordSetRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowPtrRecordSetRequest.

        租户的区域信息。 

        :param region: The region of this ShowPtrRecordSetRequest.
        :type: str
        """
        self._region = region

    @property
    def floatingip_id(self):
        """Gets the floatingip_id of this ShowPtrRecordSetRequest.

        弹性IP的ID。

        :return: The floatingip_id of this ShowPtrRecordSetRequest.
        :rtype: str
        """
        return self._floatingip_id

    @floatingip_id.setter
    def floatingip_id(self, floatingip_id):
        """Sets the floatingip_id of this ShowPtrRecordSetRequest.

        弹性IP的ID。

        :param floatingip_id: The floatingip_id of this ShowPtrRecordSetRequest.
        :type: str
        """
        self._floatingip_id = floatingip_id

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
        if not isinstance(other, ShowPtrRecordSetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
