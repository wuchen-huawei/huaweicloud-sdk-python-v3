# coding: utf-8

import pprint
import re

import six





class ListRecordConfigsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'app_name': 'str',
        'stream_name': 'str',
        'page': 'int',
        'size': 'int',
        'record_type': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'app_name': 'app_name',
        'stream_name': 'stream_name',
        'page': 'page',
        'size': 'size',
        'record_type': 'record_type'
    }

    def __init__(self, domain=None, app_name=None, stream_name=None, page=None, size=None, record_type=None):
        """ListRecordConfigsRequest - a model defined in huaweicloud sdk"""
        
        

        self._domain = None
        self._app_name = None
        self._stream_name = None
        self._page = None
        self._size = None
        self._record_type = None
        self.discriminator = None

        self.domain = domain
        if app_name is not None:
            self.app_name = app_name
        if stream_name is not None:
            self.stream_name = stream_name
        if page is not None:
            self.page = page
        if size is not None:
            self.size = size
        if record_type is not None:
            self.record_type = record_type

    @property
    def domain(self):
        """Gets the domain of this ListRecordConfigsRequest.

        直播播放域名

        :return: The domain of this ListRecordConfigsRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this ListRecordConfigsRequest.

        直播播放域名

        :param domain: The domain of this ListRecordConfigsRequest.
        :type: str
        """
        self._domain = domain

    @property
    def app_name(self):
        """Gets the app_name of this ListRecordConfigsRequest.

        流应用名称

        :return: The app_name of this ListRecordConfigsRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ListRecordConfigsRequest.

        流应用名称

        :param app_name: The app_name of this ListRecordConfigsRequest.
        :type: str
        """
        self._app_name = app_name

    @property
    def stream_name(self):
        """Gets the stream_name of this ListRecordConfigsRequest.

        流名

        :return: The stream_name of this ListRecordConfigsRequest.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """Sets the stream_name of this ListRecordConfigsRequest.

        流名

        :param stream_name: The stream_name of this ListRecordConfigsRequest.
        :type: str
        """
        self._stream_name = stream_name

    @property
    def page(self):
        """Gets the page of this ListRecordConfigsRequest.

        分页编号。 默认为0。 

        :return: The page of this ListRecordConfigsRequest.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListRecordConfigsRequest.

        分页编号。 默认为0。 

        :param page: The page of this ListRecordConfigsRequest.
        :type: int
        """
        self._page = page

    @property
    def size(self):
        """Gets the size of this ListRecordConfigsRequest.

        每页记录数。 取值范围：1-100。 默认为10。 

        :return: The size of this ListRecordConfigsRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ListRecordConfigsRequest.

        每页记录数。 取值范围：1-100。 默认为10。 

        :param size: The size of this ListRecordConfigsRequest.
        :type: int
        """
        self._size = size

    @property
    def record_type(self):
        """Gets the record_type of this ListRecordConfigsRequest.

        录制类型 configer_record：按照配置录制

        :return: The record_type of this ListRecordConfigsRequest.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this ListRecordConfigsRequest.

        录制类型 configer_record：按照配置录制

        :param record_type: The record_type of this ListRecordConfigsRequest.
        :type: str
        """
        self._record_type = record_type

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
        if not isinstance(other, ListRecordConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
