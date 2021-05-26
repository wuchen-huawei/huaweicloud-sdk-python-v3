# coding: utf-8

import pprint
import re

import six





class RecordDownloadInfoBO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'conf_uuid': 'str',
        'urls': 'list[RecordDownloadUrlDO]'
    }

    attribute_map = {
        'conf_uuid': 'confUuid',
        'urls': 'urls'
    }

    def __init__(self, conf_uuid=None, urls=None):
        """RecordDownloadInfoBO - a model defined in huaweicloud sdk"""
        
        

        self._conf_uuid = None
        self._urls = None
        self.discriminator = None

        if conf_uuid is not None:
            self.conf_uuid = conf_uuid
        if urls is not None:
            self.urls = urls

    @property
    def conf_uuid(self):
        """Gets the conf_uuid of this RecordDownloadInfoBO.

        会议UUID

        :return: The conf_uuid of this RecordDownloadInfoBO.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        """Sets the conf_uuid of this RecordDownloadInfoBO.

        会议UUID

        :param conf_uuid: The conf_uuid of this RecordDownloadInfoBO.
        :type: str
        """
        self._conf_uuid = conf_uuid

    @property
    def urls(self):
        """Gets the urls of this RecordDownloadInfoBO.

        录制文件下载URL

        :return: The urls of this RecordDownloadInfoBO.
        :rtype: list[RecordDownloadUrlDO]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this RecordDownloadInfoBO.

        录制文件下载URL

        :param urls: The urls of this RecordDownloadInfoBO.
        :type: list[RecordDownloadUrlDO]
        """
        self._urls = urls

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
        if not isinstance(other, RecordDownloadInfoBO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
