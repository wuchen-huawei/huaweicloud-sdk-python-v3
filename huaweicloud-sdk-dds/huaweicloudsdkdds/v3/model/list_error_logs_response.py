# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListErrorLogsResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'error_log_list': 'list[ErrorlogResult]',
        'total_record': 'int'
    }

    attribute_map = {
        'error_log_list': 'error_log_list',
        'total_record': 'total_record'
    }

    def __init__(self, error_log_list=None, total_record=None):
        """ListErrorLogsResponse - a model defined in huaweicloud sdk"""
        
        super(ListErrorLogsResponse, self).__init__()

        self._error_log_list = None
        self._total_record = None
        self.discriminator = None

        if error_log_list is not None:
            self.error_log_list = error_log_list
        if total_record is not None:
            self.total_record = total_record

    @property
    def error_log_list(self):
        """Gets the error_log_list of this ListErrorLogsResponse.

        具体信息。

        :return: The error_log_list of this ListErrorLogsResponse.
        :rtype: list[ErrorlogResult]
        """
        return self._error_log_list

    @error_log_list.setter
    def error_log_list(self, error_log_list):
        """Sets the error_log_list of this ListErrorLogsResponse.

        具体信息。

        :param error_log_list: The error_log_list of this ListErrorLogsResponse.
        :type: list[ErrorlogResult]
        """
        self._error_log_list = error_log_list

    @property
    def total_record(self):
        """Gets the total_record of this ListErrorLogsResponse.

        数据库版本总记录数。

        :return: The total_record of this ListErrorLogsResponse.
        :rtype: int
        """
        return self._total_record

    @total_record.setter
    def total_record(self, total_record):
        """Sets the total_record of this ListErrorLogsResponse.

        数据库版本总记录数。

        :param total_record: The total_record of this ListErrorLogsResponse.
        :type: int
        """
        self._total_record = total_record

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
        if not isinstance(other, ListErrorLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
