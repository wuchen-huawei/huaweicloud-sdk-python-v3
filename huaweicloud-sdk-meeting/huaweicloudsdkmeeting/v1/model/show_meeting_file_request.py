# coding: utf-8

import pprint
import re

import six





class ShowMeetingFileRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_request_id': 'str',
        'accept_language': 'str',
        'file_code': 'str'
    }

    attribute_map = {
        'x_request_id': 'X-Request-Id',
        'accept_language': 'Accept-Language',
        'file_code': 'file_code'
    }

    def __init__(self, x_request_id=None, accept_language=None, file_code=None):
        """ShowMeetingFileRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_request_id = None
        self._accept_language = None
        self._file_code = None
        self.discriminator = None

        if x_request_id is not None:
            self.x_request_id = x_request_id
        if accept_language is not None:
            self.accept_language = accept_language
        self.file_code = file_code

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowMeetingFileRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用uuId，若不携带，则后台自动生成

        :return: The x_request_id of this ShowMeetingFileRequest.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowMeetingFileRequest.

        请求requestId，用来标识一路请求，用于问题跟踪定位，建议使用uuId，若不携带，则后台自动生成

        :param x_request_id: The x_request_id of this ShowMeetingFileRequest.
        :type: str
        """
        self._x_request_id = x_request_id

    @property
    def accept_language(self):
        """Gets the accept_language of this ShowMeetingFileRequest.

        语言参数，默认为中文zh_CN, 英文为en_US

        :return: The accept_language of this ShowMeetingFileRequest.
        :rtype: str
        """
        return self._accept_language

    @accept_language.setter
    def accept_language(self, accept_language):
        """Sets the accept_language of this ShowMeetingFileRequest.

        语言参数，默认为中文zh_CN, 英文为en_US

        :param accept_language: The accept_language of this ShowMeetingFileRequest.
        :type: str
        """
        self._accept_language = accept_language

    @property
    def file_code(self):
        """Gets the file_code of this ShowMeetingFileRequest.

        会议纪要文件码

        :return: The file_code of this ShowMeetingFileRequest.
        :rtype: str
        """
        return self._file_code

    @file_code.setter
    def file_code(self, file_code):
        """Sets the file_code of this ShowMeetingFileRequest.

        会议纪要文件码

        :param file_code: The file_code of this ShowMeetingFileRequest.
        :type: str
        """
        self._file_code = file_code

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
        if not isinstance(other, ShowMeetingFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
