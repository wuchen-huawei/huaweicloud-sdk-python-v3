# coding: utf-8

import pprint
import re

import six





class CinderExportToImageRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'volume_id': 'str',
        'body': 'CinderExportToImageRequestBody'
    }

    attribute_map = {
        'volume_id': 'volume_id',
        'body': 'body'
    }

    def __init__(self, volume_id=None, body=None):
        """CinderExportToImageRequest - a model defined in huaweicloud sdk"""
        
        

        self._volume_id = None
        self._body = None
        self.discriminator = None

        self.volume_id = volume_id
        if body is not None:
            self.body = body

    @property
    def volume_id(self):
        """Gets the volume_id of this CinderExportToImageRequest.

        云硬盘ID。

        :return: The volume_id of this CinderExportToImageRequest.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this CinderExportToImageRequest.

        云硬盘ID。

        :param volume_id: The volume_id of this CinderExportToImageRequest.
        :type: str
        """
        self._volume_id = volume_id

    @property
    def body(self):
        """Gets the body of this CinderExportToImageRequest.


        :return: The body of this CinderExportToImageRequest.
        :rtype: CinderExportToImageRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CinderExportToImageRequest.


        :param body: The body of this CinderExportToImageRequest.
        :type: CinderExportToImageRequestBody
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
        if not isinstance(other, CinderExportToImageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
