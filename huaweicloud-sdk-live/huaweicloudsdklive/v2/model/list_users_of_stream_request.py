# coding: utf-8

import pprint
import re

import six





class ListUsersOfStreamRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'play_domain': 'str',
        'app': 'str',
        'stream': 'str',
        'isp': 'list[str]',
        'region': 'list[str]',
        'interval': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'play_domain': 'play_domain',
        'app': 'app',
        'stream': 'stream',
        'isp': 'isp',
        'region': 'region',
        'interval': 'interval',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, play_domain=None, app=None, stream=None, isp=None, region=None, interval=None, start_time=None, end_time=None):
        """ListUsersOfStreamRequest - a model defined in huaweicloud sdk"""
        
        

        self._play_domain = None
        self._app = None
        self._stream = None
        self._isp = None
        self._region = None
        self._interval = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.play_domain = play_domain
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if isp is not None:
            self.isp = isp
        if region is not None:
            self.region = region
        if interval is not None:
            self.interval = interval
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def play_domain(self):
        """Gets the play_domain of this ListUsersOfStreamRequest.

        播放域名。 

        :return: The play_domain of this ListUsersOfStreamRequest.
        :rtype: str
        """
        return self._play_domain

    @play_domain.setter
    def play_domain(self, play_domain):
        """Sets the play_domain of this ListUsersOfStreamRequest.

        播放域名。 

        :param play_domain: The play_domain of this ListUsersOfStreamRequest.
        :type: str
        """
        self._play_domain = play_domain

    @property
    def app(self):
        """Gets the app of this ListUsersOfStreamRequest.

        app名。 

        :return: The app of this ListUsersOfStreamRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ListUsersOfStreamRequest.

        app名。 

        :param app: The app of this ListUsersOfStreamRequest.
        :type: str
        """
        self._app = app

    @property
    def stream(self):
        """Gets the stream of this ListUsersOfStreamRequest.

        流名。 

        :return: The stream of this ListUsersOfStreamRequest.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this ListUsersOfStreamRequest.

        流名。 

        :param stream: The stream of this ListUsersOfStreamRequest.
        :type: str
        """
        self._stream = stream

    @property
    def isp(self):
        """Gets the isp of this ListUsersOfStreamRequest.

        运营商列表，取值如下： - \"CMCC ：移动\" - \"CTCC ： 电信\" - \"CUCC ：联通\" - \"OTHER: 其他\"  不填写查询所有运营商。 

        :return: The isp of this ListUsersOfStreamRequest.
        :rtype: list[str]
        """
        return self._isp

    @isp.setter
    def isp(self, isp):
        """Sets the isp of this ListUsersOfStreamRequest.

        运营商列表，取值如下： - \"CMCC ：移动\" - \"CTCC ： 电信\" - \"CUCC ：联通\" - \"OTHER: 其他\"  不填写查询所有运营商。 

        :param isp: The isp of this ListUsersOfStreamRequest.
        :type: list[str]
        """
        self._isp = isp

    @property
    def region(self):
        """Gets the region of this ListUsersOfStreamRequest.

        区域列表。具体取值请参考[省份名称缩写](live_03_0043.xml)，不填写查询所有区域。 

        :return: The region of this ListUsersOfStreamRequest.
        :rtype: list[str]
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListUsersOfStreamRequest.

        区域列表。具体取值请参考[省份名称缩写](live_03_0043.xml)，不填写查询所有区域。 

        :param region: The region of this ListUsersOfStreamRequest.
        :type: list[str]
        """
        self._region = region

    @property
    def interval(self):
        """Gets the interval of this ListUsersOfStreamRequest.

        查询数据的时间粒度，支持60（默认值）, 300秒。不传值时，使用默认值60秒。 

        :return: The interval of this ListUsersOfStreamRequest.
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this ListUsersOfStreamRequest.

        查询数据的时间粒度，支持60（默认值）, 300秒。不传值时，使用默认值60秒。 

        :param interval: The interval of this ListUsersOfStreamRequest.
        :type: int
        """
        self._interval = interval

    @property
    def start_time(self):
        """Gets the start_time of this ListUsersOfStreamRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度31天，最大查询周期90天。  若参数为空，默认查询7天数据。 

        :return: The start_time of this ListUsersOfStreamRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ListUsersOfStreamRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度31天，最大查询周期90天。  若参数为空，默认查询7天数据。 

        :param start_time: The start_time of this ListUsersOfStreamRequest.
        :type: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ListUsersOfStreamRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间。结束时间需大于起始时间。 

        :return: The end_time of this ListUsersOfStreamRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListUsersOfStreamRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。格式为：YYYY-MM-DDThh:mm:ssZ。  若参数为空，默认为当前时间。结束时间需大于起始时间。 

        :param end_time: The end_time of this ListUsersOfStreamRequest.
        :type: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListUsersOfStreamRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
