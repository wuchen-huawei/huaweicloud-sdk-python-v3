# coding: utf-8

import pprint
import re

import six





class ShowHisMeetingDetailRequest:


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
        'offset': 'int',
        'limit': 'int',
        'search_key': 'str',
        'user_uuid': 'str',
        'x_type': 'int',
        'x_query_type': 'int',
        'x_authorization_type': 'str',
        'x_site_id': 'str'
    }

    attribute_map = {
        'conf_uuid': 'confUUID',
        'offset': 'offset',
        'limit': 'limit',
        'search_key': 'searchKey',
        'user_uuid': 'userUUID',
        'x_type': 'X-Type',
        'x_query_type': 'X-Query-Type',
        'x_authorization_type': 'X-Authorization-Type',
        'x_site_id': 'X-Site-Id'
    }

    def __init__(self, conf_uuid=None, offset=None, limit=None, search_key=None, user_uuid=None, x_type=None, x_query_type=None, x_authorization_type=None, x_site_id=None):
        """ShowHisMeetingDetailRequest - a model defined in huaweicloud sdk"""
        
        

        self._conf_uuid = None
        self._offset = None
        self._limit = None
        self._search_key = None
        self._user_uuid = None
        self._x_type = None
        self._x_query_type = None
        self._x_authorization_type = None
        self._x_site_id = None
        self.discriminator = None

        self.conf_uuid = conf_uuid
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search_key is not None:
            self.search_key = search_key
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if x_type is not None:
            self.x_type = x_type
        if x_query_type is not None:
            self.x_query_type = x_query_type
        if x_authorization_type is not None:
            self.x_authorization_type = x_authorization_type
        if x_site_id is not None:
            self.x_site_id = x_site_id

    @property
    def conf_uuid(self):
        """Gets the conf_uuid of this ShowHisMeetingDetailRequest.

        会议UUID。

        :return: The conf_uuid of this ShowHisMeetingDetailRequest.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        """Sets the conf_uuid of this ShowHisMeetingDetailRequest.

        会议UUID。

        :param conf_uuid: The conf_uuid of this ShowHisMeetingDetailRequest.
        :type: str
        """
        self._conf_uuid = conf_uuid

    @property
    def offset(self):
        """Gets the offset of this ShowHisMeetingDetailRequest.

        指定返回的与会者列表的记录索引。该值必须大于等于0；默认为0。

        :return: The offset of this ShowHisMeetingDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowHisMeetingDetailRequest.

        指定返回的与会者列表的记录索引。该值必须大于等于0；默认为0。

        :param offset: The offset of this ShowHisMeetingDetailRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowHisMeetingDetailRequest.

        指定返回的与会者记录数，默认是20。

        :return: The limit of this ShowHisMeetingDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowHisMeetingDetailRequest.

        指定返回的与会者记录数，默认是20。

        :param limit: The limit of this ShowHisMeetingDetailRequest.
        :type: int
        """
        self._limit = limit

    @property
    def search_key(self):
        """Gets the search_key of this ShowHisMeetingDetailRequest.

        根据会议主题，预定人和云会议室会议id关键词的字符串，查询历史会议信息。

        :return: The search_key of this ShowHisMeetingDetailRequest.
        :rtype: str
        """
        return self._search_key

    @search_key.setter
    def search_key(self, search_key):
        """Sets the search_key of this ShowHisMeetingDetailRequest.

        根据会议主题，预定人和云会议室会议id关键词的字符串，查询历史会议信息。

        :param search_key: The search_key of this ShowHisMeetingDetailRequest.
        :type: str
        """
        self._search_key = search_key

    @property
    def user_uuid(self):
        """Gets the user_uuid of this ShowHisMeetingDetailRequest.

        用户的UUID（已在USG注册过的）。

        :return: The user_uuid of this ShowHisMeetingDetailRequest.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this ShowHisMeetingDetailRequest.

        用户的UUID（已在USG注册过的）。

        :param user_uuid: The user_uuid of this ShowHisMeetingDetailRequest.
        :type: str
        """
        self._user_uuid = user_uuid

    @property
    def x_type(self):
        """Gets the x_type of this ShowHisMeetingDetailRequest.

        默认值为0。 0: 不区分会议室和与会人。 1：分页查询区分会议室和与会人，结果合并返回。 2：单独查询会议室与与会人，结果也是单独返回。

        :return: The x_type of this ShowHisMeetingDetailRequest.
        :rtype: int
        """
        return self._x_type

    @x_type.setter
    def x_type(self, x_type):
        """Sets the x_type of this ShowHisMeetingDetailRequest.

        默认值为0。 0: 不区分会议室和与会人。 1：分页查询区分会议室和与会人，结果合并返回。 2：单独查询会议室与与会人，结果也是单独返回。

        :param x_type: The x_type of this ShowHisMeetingDetailRequest.
        :type: int
        """
        self._x_type = x_type

    @property
    def x_query_type(self):
        """Gets the x_query_type of this ShowHisMeetingDetailRequest.

        当X-Type为2时，该字段有效。默认值为0。 0: 查询与会人。 1：查询终端。

        :return: The x_query_type of this ShowHisMeetingDetailRequest.
        :rtype: int
        """
        return self._x_query_type

    @x_query_type.setter
    def x_query_type(self, x_query_type):
        """Sets the x_query_type of this ShowHisMeetingDetailRequest.

        当X-Type为2时，该字段有效。默认值为0。 0: 查询与会人。 1：查询终端。

        :param x_query_type: The x_query_type of this ShowHisMeetingDetailRequest.
        :type: int
        """
        self._x_query_type = x_query_type

    @property
    def x_authorization_type(self):
        """Gets the x_authorization_type of this ShowHisMeetingDetailRequest.

        标识是否为第三方portal过来的请求。

        :return: The x_authorization_type of this ShowHisMeetingDetailRequest.
        :rtype: str
        """
        return self._x_authorization_type

    @x_authorization_type.setter
    def x_authorization_type(self, x_authorization_type):
        """Sets the x_authorization_type of this ShowHisMeetingDetailRequest.

        标识是否为第三方portal过来的请求。

        :param x_authorization_type: The x_authorization_type of this ShowHisMeetingDetailRequest.
        :type: str
        """
        self._x_authorization_type = x_authorization_type

    @property
    def x_site_id(self):
        """Gets the x_site_id of this ShowHisMeetingDetailRequest.

        用于区分到哪个HCSO站点鉴权。

        :return: The x_site_id of this ShowHisMeetingDetailRequest.
        :rtype: str
        """
        return self._x_site_id

    @x_site_id.setter
    def x_site_id(self, x_site_id):
        """Sets the x_site_id of this ShowHisMeetingDetailRequest.

        用于区分到哪个HCSO站点鉴权。

        :param x_site_id: The x_site_id of this ShowHisMeetingDetailRequest.
        :type: str
        """
        self._x_site_id = x_site_id

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
        if not isinstance(other, ShowHisMeetingDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
